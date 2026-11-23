"""design.py – shared design system for the M3 animation project.
Import this in every scene instead of helpers.py.
"""
from manim import *
import manimpango

# ── Palette ──────────────────────────────────────────────────────────────────
BG   = "#0F172A"
INK  = "#E2E8F0"
MUTED= "#94A3B8"
CURVE= "#38BDF8"
POINT= "#FACC15"
GOOD = "#4ADE80"
BAD  = "#F87171"
MAXC = "#C084FC"

# ── Layout constants ─────────────────────────────────────────────────────────
SAFE      = 0.6                      # margin from every frame edge
CONTENT_W = 14.2 - 2 * SAFE         # ≈ 13.0
CONTENT_H = 5.4                      # free area under the header
CONTENT_CENTER = DOWN * 0.25

# ── Font ─────────────────────────────────────────────────────────────────────
def pick_font():
    have = set(manimpango.list_fonts())
    for f in ["Inter", "Helvetica Neue", "Avenir Next", "Arial"]:
        if f in have:
            return f
    return "Sans"

FONT = pick_font()

# ── Text helper ──────────────────────────────────────────────────────────────
def T(s, size=34, color=INK, bold=False):
    return Text(s, font=FONT, font_size=size, color=color,
                weight=BOLD if bold else NORMAL)

# ── Placement helper ─────────────────────────────────────────────────────────
def place(m, region_w=None, region_h=None, center=None):
    """Fit mobject inside a region and centre it there."""
    w = region_w if region_w is not None else CONTENT_W
    h = region_h if region_h is not None else CONTENT_H
    if m.width  > w: m.scale_to_fit_width(w)
    if m.height > h: m.scale_to_fit_height(h)
    return m.move_to(CONTENT_CENTER if center is None else center)

# ── Card helper ──────────────────────────────────────────────────────────────
def card(*mobs, color=CURVE, direction=DOWN, gap=0.3, pad=0.35):
    """Stack mobjects and wrap in a rounded box."""
    g = VGroup(*mobs).arrange(direction, buff=gap)
    r = SurroundingRectangle(g, buff=pad, corner_radius=0.18, color=color,
                             stroke_width=2.5, fill_color=color, fill_opacity=0.08)
    return VGroup(r, g)

# ── Pill helper ──────────────────────────────────────────────────────────────
def pill(s, color=POINT, size=28):
    t = T(s, size, INK)
    r = SurroundingRectangle(t, buff=0.2, corner_radius=0.25, color=color,
                             stroke_width=2, fill_color=color, fill_opacity=0.12)
    return VGroup(r, t)

# ── Glow helper ──────────────────────────────────────────────────────────────
def glow(curve, color=CURVE):
    halo = curve.copy().set_stroke(color, width=14, opacity=0.18)
    return VGroup(halo, curve.set_stroke(color, width=5))

# ── Dot-grid backdrop ────────────────────────────────────────────────────────
def backdrop():
    dots = VGroup(*[
        Dot([x, y, 0], radius=0.014, color=WHITE).set_opacity(0.10)
        for x in range(-7, 8) for y in range(-4, 5)
    ])
    dots.set_z_index(-10)
    return dots

# ── Scene header with progress bar ──────────────────────────────────────────
def header(n, title, total=6):
    num  = T(str(n), 24, BG, True)
    chip = VGroup(
        RoundedRectangle(corner_radius=0.14, width=0.6, height=0.5,
                         fill_color=CURVE, fill_opacity=1, stroke_width=0),
        num
    )
    num.move_to(chip[0])
    row  = VGroup(chip, T(title, 36, INK, True)).arrange(RIGHT, buff=0.3).to_corner(UL, buff=SAFE)
    w    = config.frame_width
    track = Line(LEFT*w/2, RIGHT*w/2, stroke_width=4, color=WHITE).set_opacity(0.12).to_edge(UP, buff=0.05)
    done  = Line(track.get_left(),
                 track.get_left() + RIGHT * w * n / total,
                 stroke_width=4, color=CURVE)
    return VGroup(track, done, row)

# ── Layout checker ──────────────────────────────────────────────────────────
def check_layout(scene, safe=SAFE, bottom_clear=1.0):
    """
    Report (a) text mobjects outside the safe frame area,
           (b) pairs of text mobjects whose bounding boxes intersect.
    Returns a list of problem description strings.
    """
    problems = []
    xmax =  config.frame_width  / 2 - safe
    ymax =  config.frame_height / 2 - safe
    ymin = -config.frame_height / 2 + bottom_clear

    def _collect(mob, depth=0):
        result = []
        if isinstance(mob, (Text, Tex, MathTex)):
            result.append(mob)
        for sub in mob.submobjects:
            result.extend(_collect(sub, depth+1))
        return result

    text_mobs = []
    for m in scene.mobjects:
        text_mobs.extend(_collect(m))

    # (a) out-of-bounds
    for m in text_mobs:
        label = getattr(m, 'original_text', None) or str(m)[:30]
        if (m.get_right()[0]  >  xmax or
            m.get_left()[0]   < -xmax or
            m.get_top()[1]    >  ymax or
            m.get_bottom()[1] <  ymin):
            msg = f"OUT_OF_BOUNDS: {type(m).__name__} center={[round(v,2) for v in m.get_center()]} text={label!r:.30}"
            print(msg)
            problems.append(msg)

    # (b) intersecting pairs
    for i, a in enumerate(text_mobs):
        for b in text_mobs[i+1:]:
            if (a.get_right()[0]  > b.get_left()[0]  and
                b.get_right()[0]  > a.get_left()[0]  and
                a.get_top()[1]    > b.get_bottom()[1] and
                b.get_top()[1]    > a.get_bottom()[1]):
                la = getattr(a, 'original_text', None) or str(a)[:20]
                lb = getattr(b, 'original_text', None) or str(b)[:20]
                msg = f"OVERLAP: {la!r:.20} vs {lb!r:.20}"
                print(msg)
                problems.append(msg)

    if not problems:
        print("check_layout: OK")
    return problems

# ── Scene synchronization helper ─────────────────────────────────────────────
def sync_to(scene, t):
    """Wait until the scene clock reaches t seconds (never negative)."""
    remaining = t - scene.renderer.time
    if remaining > 0.01:
        scene.wait(remaining)
    elif remaining < -0.05:
        print(f"LATE by {-remaining:.2f}s at target {t}")

# ── Base scene ───────────────────────────────────────────────────────────────
class Base(Scene):
    """Every scene subclasses this: navy background with a faint dot grid."""
    def setup(self):
        self.camera.background_color = BG
        self.add(backdrop())

