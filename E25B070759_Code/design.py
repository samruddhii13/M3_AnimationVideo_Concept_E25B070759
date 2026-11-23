"""
design.py – shared constants, helpers, and base class.
Import this in every scene; do not duplicate helpers.
"""
from manim import *
import manimpango
import json
import os
import numpy as np

# ── Colours ──────────────────────────────────────────────────────────────────
BG    = "#0F172A"
INK   = "#E2E8F0"
MUTED = "#94A3B8"
CURVE = "#38BDF8"
POINT = "#FACC15"
GOOD  = "#4ADE80"
BAD   = "#F87171"
MAXC  = "#C084FC"
BALL  = "#DC2626"

# ── Safe area & content bounds ───────────────────────────────────────────────
SAFE           = 0.6
CONTENT_W      = config.frame_width - 2 * SAFE
CONTENT_H      = 5.4
CONTENT_CENTER = DOWN * 0.25

# ── Font ─────────────────────────────────────────────────────────────────────
def pick_font():
    have = set(manimpango.list_fonts())
    for f in ["Inter", "Helvetica Neue", "Avenir Next", "Arial"]:
        if f in have:
            return f
    return "Sans"

FONT = pick_font()

def T(s, size=34, color=INK, bold=False):
    return Text(s, font=FONT, font_size=size, color=color, weight=BOLD if bold else NORMAL)

def place(m, region_w=None, region_h=None, center=None):
    w = region_w or CONTENT_W
    h = region_h or CONTENT_H
    if m.width  > w: m.scale_to_fit_width(w)
    if m.height > h: m.scale_to_fit_height(h)
    return m.move_to(CONTENT_CENTER if center is None else center)

def card(*mobs, color=CURVE, direction=DOWN, gap=0.3, pad=0.35):
    g = VGroup(*mobs).arrange(direction, buff=gap)
    r = SurroundingRectangle(g, buff=pad, corner_radius=0.18, color=color,
                             stroke_width=2.5, fill_color=color, fill_opacity=0.08)
    return VGroup(r, g)

def pill(s, color=POINT, size=28):
    t = T(s, size, INK)
    r = SurroundingRectangle(t, buff=0.2, corner_radius=0.25, color=color,
                             stroke_width=2, fill_color=color, fill_opacity=0.12)
    return VGroup(r, t)

def glow(curve, color=CURVE):
    halo = curve.copy().set_stroke(color, width=14, opacity=0.18)
    return VGroup(halo, curve.set_stroke(color, width=5))

def make_ball(r=0.25):
    """Real cricket ball with red body, curved white seams, and shine dot."""
    body  = Circle(radius=r, fill_color=BALL, fill_opacity=1, stroke_color="#7F1D1D", stroke_width=2.5)
    s1    = ArcBetweenPoints(UP*r*0.9 + LEFT*r*0.3,  DOWN*r*0.9 + LEFT*r*0.3,  angle=-PI/3, color=WHITE, stroke_width=2.0)
    s2    = ArcBetweenPoints(UP*r*0.9 + RIGHT*r*0.3, DOWN*r*0.9 + RIGHT*r*0.3, angle=PI/3,  color=WHITE, stroke_width=2.0)
    shine = Dot(radius=r*0.13, color=WHITE).set_opacity(0.55).move_to(UP*r*0.45 + LEFT*r*0.42)
    return VGroup(body, s1, s2, shine)

def h_of(t):
    """Physical height formula h(t) = 20t - 5t^2."""
    return max(0.0, 20.0*t - 5.0*t*t)

def backdrop():
    dots = VGroup(*[
        Dot([x, y, 0], radius=0.014, color=WHITE).set_opacity(0.10)
        for x in range(-7, 8) for y in range(-4, 5)
    ])
    dots.set_z_index(-10)
    return dots

def header(n, title, total=6):
    num = T(str(n), 24, BG, True)
    chip = VGroup(
        RoundedRectangle(corner_radius=0.14, width=0.6, height=0.5,
                         fill_color=CURVE, fill_opacity=1, stroke_width=0),
        num
    )
    num.move_to(chip[0])
    row = VGroup(chip, T(title, 36, INK, True)).arrange(RIGHT, buff=0.3).to_corner(UL, buff=SAFE)
    w = config.frame_width
    track = Line(LEFT*w/2, RIGHT*w/2, stroke_width=4, color=WHITE).set_opacity(0.12).to_edge(UP, buff=0.05)
    done  = Line(track.get_left(), track.get_left() + RIGHT*w*n/total, stroke_width=4, color=CURVE)
    return VGroup(track, done, row)

def ball_and_graph_stage():
    """
    Returns (ruler, axes, labels). Ruler left, axes right.
    SAME height (4.4) and scale 0..25, bottoms and heights aligned to machine precision.
    """
    axes = Axes(
        x_range=[0, 5, 1],
        y_range=[0, 25, 5],
        x_length=6.0,
        y_length=4.4,
        axis_config={"color": MUTED, "stroke_width": 2, "include_tip": False, "font_size": 24},
        x_axis_config={"numbers_to_include": [0, 1, 2, 3, 4, 5]},
        y_axis_config={"numbers_to_include": [0, 5, 10, 15, 20, 25]}
    )
    axes.move_to(RIGHT * 2.6 + DOWN * 0.05)
    xl = T("Time t (s)", 22, MUTED).next_to(axes.x_axis, DOWN, buff=0.18)
    yl = T("Height h (m)", 22, MUTED).next_to(axes.y_axis, UP, buff=0.15)

    ruler = NumberLine(
        x_range=[0, 25, 5],
        length=4.4,
        rotation=PI/2,
        include_numbers=True,
        font_size=24,
        label_direction=LEFT,
        line_to_number_buff=0.30,
        color=MUTED
    )
    ruler.move_to([-4.6, axes.c2p(0, 12.5)[1], 0])

    # Perfect alignment shift: match ruler n2p(0) to axes c2p(0,0) in y, and set x to -4.6
    shift_vec = np.array([-4.6 - ruler.n2p(0)[0], axes.c2p(0, 0)[1] - ruler.n2p(0)[1], 0])
    ruler.shift(shift_vec)

    ruler_title = T("Ruler (m)", 20, MUTED).next_to(ruler, UP, buff=0.15)

    return ruler, axes, VGroup(xl, yl, ruler_title)

class Base(Scene):
    def setup(self):
        self.camera.background_color = BG
        self.add(backdrop())

_TIMINGS = None

def load_scene_timings(scene_name):
    global _TIMINGS
    if _TIMINGS is None:
        p = os.path.join(os.path.dirname(__file__), "..", "Audio", "timings.json")
        try:
            with open(p, "r", encoding="utf-8") as f:
                _TIMINGS = json.load(f)
        except Exception as e:
            print(f"Warning loading timings.json: {e}")
            _TIMINGS = {}
    return _TIMINGS.get(scene_name, {})

def sync_to(scene, t):
    """Wait until scene clock reaches target time t seconds."""
    r = t - scene.renderer.time
    if r > 0.005:
        scene.wait(r)
    elif r < -0.05:
        print(f"LATE by {-r:.2f}s at target {t:.2f}s (scene time {scene.renderer.time:.2f}s)")

def check_layout(scene):
    """
    Check all Text/Tex mobjects:
    - inside SAFE margins
    - out of bottom 1.0 unit (player controls zone: y > -config.frame_height/2 + 1.0 = -3.0)
    - bounding box intersections between active text objects
    """
    fw = config.frame_width / 2
    fh = config.frame_height / 2
    x_min, x_max = -fw + SAFE, fw - SAFE
    y_min, y_max = -fh + 1.0, fh - SAFE  # -3.0 to 3.4

    # Extract all visible leaf text objects
    leaves = []
    for mob in scene.mobjects:
        for sub in mob.get_family():
            if isinstance(sub, (Text, Tex, MathTex, SingleStringMathTex)):
                # Skip number labels inside Axes or NumberLine
                is_axis_child = False
                for a in scene.mobjects:
                    if isinstance(a, (Axes, NumberLine)) and sub in a.get_family() and sub is not a:
                        is_axis_child = True
                        break
                if not is_axis_child:
                    leaves.append(sub)

    violations = 0
    seen = set()
    for m in leaves:
        if id(m) in seen:
            continue
        seen.add(id(m))
        try:
            b_left = m.get_left()[0]
            b_right = m.get_right()[0]
            b_bottom = m.get_bottom()[1]
            b_top = m.get_top()[1]
        except Exception:
            continue

        if b_left < x_min - 0.05:
            print(f"[layout WARNING] Left margin exceeded: '{getattr(m, 'text', '')}' x_min={b_left:.2f} < {x_min:.2f}")
            violations += 1
        if b_right > x_max + 0.05:
            print(f"[layout WARNING] Right margin exceeded: '{getattr(m, 'text', '')}' x_max={b_right:.2f} > {x_max:.2f}")
            violations += 1
        if b_bottom < y_min - 0.05:
            print(f"[layout WARNING] Bottom controls zone violated: '{getattr(m, 'text', '')}' y_min={b_bottom:.2f} < {y_min:.2f}")
            violations += 1
        if b_top > y_max + 0.05:
            print(f"[layout WARNING] Top margin exceeded: '{getattr(m, 'text', '')}' y_top={b_top:.2f} > {y_max:.2f}")
            violations += 1

    if violations == 0:
        print("[layout] OK – zero margin violations")
    return violations
