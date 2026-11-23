"""Scene 4 – Key Features of the Graph.
Template B: left = permanent parabola, right = sequential feature cards.
"""
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from design import *

AUDIO_DIR = os.path.join(os.path.dirname(__file__), "..", "Audio")

def _load_scene_timings(scene_key):
    p = os.path.join(AUDIO_DIR, "timings.json")
    if not os.path.exists(p):
        return [], 0.0
    with open(p) as f:
        d = json.load(f)
    sc = d.get(scene_key, {})
    return sc.get("sentences", []), sc.get("total_duration", 0.0)

class Scene4Features(Base):
    def construct(self):
        sents, total_dur = _load_scene_timings("scene4")

        hdr = header(4, "Key Features")
        self.add(hdr)

        def h(t): return 20*t - 5*t**2

        # ── Permanent left axes ───────────────────────────────────────────────
        sync_to(self, sents[0]["start"])
        ax = Axes(
            x_range=[0,5,1], y_range=[0,25,5],
            x_length=5.6, y_length=4.2,
            axis_config={"color": INK, "stroke_width": 2,
                         "include_tip": True, "tip_length": 0.18},
            x_axis_config={"numbers_to_include": [0,1,2,3,4,5]},
            y_axis_config={"numbers_to_include": [0,5,10,15,20,25]},
        )
        x_lbl = ax.get_x_axis_label(
            Text("t (s)", font=FONT, font_size=20, color=MUTED),
            edge=RIGHT, direction=RIGHT, buff=0.15)
        y_lbl = ax.get_y_axis_label(
            Text("h (m)", font=FONT, font_size=20, color=MUTED),
            edge=UP, direction=UP, buff=0.15)
        ax_grp = VGroup(ax, x_lbl, y_lbl)
        place(ax_grp, 5.8, 4.8, LEFT * 3.4 + DOWN * 0.25)

        curve_glow = glow(ax.plot(h, x_range=[0,4,0.05], color=CURVE), CURVE)
        self.play(Create(ax_grp), Create(curve_glow), run_time=1.2)

        RC = RIGHT * 3.4 + DOWN * 0.25
        RW = 5.8

        # ─── STEP 1: Intercepts ───────────────────────────────────────────────
        sync_to(self, sents[1]["start"])
        int_title = T("Intercepts", 34, GOOD, bold=True)
        int_title.move_to(RC + UP * 1.7)

        d0 = Dot(ax.c2p(0,0), radius=0.12, color=GOOD)
        d4 = Dot(ax.c2p(4,0), radius=0.12, color=GOOD)
        l0 = T("h(0)=0", 24, GOOD).next_to(d0, UP+RIGHT, buff=0.08)
        l4 = T("h(4)=0", 24, GOOD).next_to(d4, UP+LEFT,  buff=0.08)

        int_math = VGroup(
            MathTex(r"h(t)=0 \Rightarrow 5t(4-t)=0", font_size=36, color=INK),
            MathTex(r"t=0 \quad\text{or}\quad t=4", font_size=36, color=GOOD),
        ).arrange(DOWN, buff=0.22)
        int_box = card(int_math, color=GOOD, pad=0.38)
        int_box.move_to(RC + DOWN * 0.3)
        if int_box.width > RW: int_box.scale_to_fit_width(RW)

        self.play(FadeIn(int_title), FadeIn(d0), FadeIn(d4), FadeIn(l0), FadeIn(l4),
                  FadeIn(int_box), run_time=0.8)

        # ─── STEP 2: Maximum ──────────────────────────────────────────────────
        sync_to(self, sents[7]["start"])
        self.play(FadeOut(int_title), FadeOut(d0), FadeOut(d4), FadeOut(l0), FadeOut(l4),
                  FadeOut(int_box), run_time=0.4)

        max_title = T("Maximum", 34, MAXC, bold=True).move_to(RC + UP * 1.7)

        d_max = Dot(ax.c2p(2,20), radius=0.12, color=MAXC)
        l_max = T("h(2)=20 m", 26, MAXC).next_to(d_max, RIGHT, buff=0.12)
        sym   = DashedLine(ax.c2p(2,0), ax.c2p(2,21),
                           color=MAXC, stroke_width=2, dash_length=0.15)

        max_math = VGroup(
            MathTex(r"h(t)=20-5(t-2)^2", font_size=36, color=INK),
            MathTex(r"\text{Max at }t=2 \Rightarrow h=20\,\text{m}", font_size=36, color=MAXC),
            T("Symmetric about t = 2", 26, MUTED),
        ).arrange(DOWN, buff=0.22)
        max_box = card(max_math, color=MAXC, pad=0.38)
        max_box.move_to(RC + DOWN * 0.4)
        if max_box.width > RW: max_box.scale_to_fit_width(RW)

        self.play(FadeIn(max_title), Create(sym), FadeIn(d_max), FadeIn(l_max), FadeIn(max_box), run_time=0.8)

        # ─── STEP 3: Domain & Range ───────────────────────────────────────────
        sync_to(self, sents[12]["start"])
        self.play(FadeOut(max_title), FadeOut(sym), FadeOut(d_max), FadeOut(l_max),
                  FadeOut(max_box), run_time=0.4)

        dr_title = T("Domain & Range", 34, CURVE, bold=True).move_to(RC + UP * 1.7)
        if dr_title.width > RW: dr_title.scale_to_fit_width(RW)

        t_seg = Line(ax.c2p(0,0), ax.c2p(4,0), stroke_width=6, color=CURVE)
        h_seg = Line(ax.c2p(0,0), ax.c2p(0,20), stroke_width=6, color=GOOD)

        dr_math = VGroup(
            VGroup(T("Domain:", 30, CURVE),
                   MathTex(r"[0,\,4]",  font_size=40, color=CURVE)).arrange(RIGHT, buff=0.3),
            VGroup(T("Range:",  30, GOOD),
                   MathTex(r"[0,\,20]", font_size=40, color=GOOD )).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        dr_box = card(dr_math, color=CURVE, pad=0.42)
        dr_box.move_to(RC + DOWN * 0.3)
        if dr_box.width > RW: dr_box.scale_to_fit_width(RW)

        self.play(FadeIn(dr_title), Create(t_seg), Create(h_seg), FadeIn(dr_box), run_time=0.8)

        # ─── STEP 4: Increasing / Decreasing ─────────────────────────────────
        sync_to(self, sents[15]["start"])
        self.play(FadeOut(dr_title), FadeOut(t_seg), FadeOut(h_seg), FadeOut(dr_box), run_time=0.4)

        id_title = T("Increasing & Decreasing", 32, INK, bold=True).move_to(RC + UP * 1.7)
        if id_title.width > RW: id_title.scale_to_fit_width(RW)

        inc_curve = ax.plot(h, x_range=[0,2,0.05], color=GOOD, stroke_width=5)
        dec_curve = ax.plot(h, x_range=[2,4,0.05], color=BAD,  stroke_width=5)
        # Stagger labels so they never overlap horizontally or vertically
        inc_lbl = pill("Increasing [0, 2] ↑", GOOD, 18).move_to(ax.c2p(1.0, 10.5))
        dec_lbl = pill("Decreasing [2, 4] ↓", BAD, 18).move_to(ax.c2p(3.0, 4.5))

        rate_rows = VGroup(
            T("[0,1]: Δh = +15 m/s  ↑", 26, GOOD),
            T("[1,2]: Δh =  +5 m/s  ↑", 26, GOOD),
            T("[2,3]: Δh =  −5 m/s  ↓", 26, BAD),
            T("[3,4]: Δh = −15 m/s  ↓", 26, BAD),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        rate_box = card(rate_rows, color=CURVE, pad=0.35)
        rate_box.move_to(RC + DOWN * 0.5)
        if rate_box.height > 3.0: rate_box.scale_to_fit_height(3.0)
        if rate_box.width  > RW:  rate_box.scale_to_fit_width(RW)
        if rate_box.get_bottom()[1] < -config.frame_height/2 + 1.2:
            rate_box.shift(UP * (-config.frame_height/2 + 1.2 - rate_box.get_bottom()[1]))

        self.play(FadeIn(id_title), run_time=0.4)
        self.play(Create(inc_curve), FadeIn(inc_lbl), run_time=0.8)
        self.play(Create(dec_curve), FadeIn(dec_lbl), run_time=0.8)
        self.play(FadeIn(rate_box), run_time=0.8)

        sync_to(self, total_dur + 0.15)
        check_layout(self)
