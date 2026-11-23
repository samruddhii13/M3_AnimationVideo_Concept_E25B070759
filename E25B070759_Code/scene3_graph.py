"""Scene 3 – The Graph & Vertical Line Test.
Template B: left = axes+parabola, right = VLT / circle counterexample.
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

class Scene3Graph(Base):
    def construct(self):
        sents, total_dur = _load_scene_timings("scene3")

        hdr = header(3, "The Graph & Vertical Line Test")
        self.add(hdr)

        def h(t): return 20*t - 5*t**2

        # ── LEFT: axes + parabola ─────────────────────────────────────────────
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
            Text("Time t (s)", font=FONT, font_size=20, color=MUTED),
            edge=RIGHT, direction=RIGHT, buff=0.15)
        y_lbl = ax.get_y_axis_label(
            Text("Height h (m)", font=FONT, font_size=20, color=MUTED),
            edge=UP, direction=UP, buff=0.15)
        ax_grp = VGroup(ax, x_lbl, y_lbl)
        place(ax_grp, 5.8, 4.8, LEFT * 3.4 + DOWN * 0.25)

        curve_glow = glow(ax.plot(h, x_range=[0,4,0.05], color=CURVE), CURVE)

        self.play(Create(ax_grp), run_time=1.0)
        self.play(Create(curve_glow), run_time=1.0)

        # ── Beats 1-6: table of values and points ────────────────────────────
        sync_to(self, sents[1]["start"])
        tbl_data = [(0,0),(1,15),(2,20),(3,15),(4,0)]
        hdr_row = VGroup(
            T("t (s)", 26, CURVE, bold=True),
            T("h(t) (m)", 26, GOOD,  bold=True),
        ).arrange(RIGHT, buff=0.6)
        tbl_rows = VGroup(*[
            VGroup(T(str(t), 26, INK), T(str(hv), 26, POINT)).arrange(RIGHT, buff=0.8)
            for t,hv in tbl_data
        ]).arrange(DOWN, buff=0.18)
        tbl = VGroup(hdr_row, tbl_rows).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        tbl_box = card(T("Table of Values", 28, INK, bold=True), tbl, color=CURVE, pad=0.35)
        # Place cleanly in the right region (Template B)
        tbl_box.move_to(RIGHT * 3.4 + UP * 0.5)
        if tbl_box.width > 5.6: tbl_box.scale_to_fit_width(5.6)

        dots = VGroup(*[Dot(ax.c2p(t,hv), radius=0.10, color=POINT) for t,hv in tbl_data])
        self.play(FadeIn(tbl_box), FadeIn(dots), run_time=0.8)

        # ── Beats 9-10: axis note ─────────────────────────────────────────────
        sync_to(self, sents[9]["start"])
        axis_note = T("Horizontal = time, Vertical = height (not ball path in space)", 24, MUTED)
        if axis_note.width > 5.8: axis_note.scale_to_fit_width(5.8)
        axis_note.move_to(LEFT * 3.4 + DOWN * 2.3)
        if axis_note.get_bottom()[1] < -config.frame_height/2 + 1.2:
            axis_note.shift(UP * (-config.frame_height/2 + 1.2 - axis_note.get_bottom()[1]))
        self.play(FadeIn(axis_note), run_time=0.8)

        # ── Beats 13-14: Vertical Line Test (parabola) ────────────────────────
        sync_to(self, sents[13]["start"])
        self.play(FadeOut(tbl_box), FadeOut(dots), FadeOut(axis_note), run_time=0.4)

        vlt_title = T("Vertical Line Test", 34, INK, bold=True)
        vlt_title.move_to(RIGHT * 3.4 + UP * 1.6)
        self.play(FadeIn(vlt_title), run_time=0.6)

        vl_x = ValueTracker(0.0)
        vline = always_redraw(lambda: ax.get_vertical_line(
            ax.c2p(vl_x.get_value(), h(min(vl_x.get_value(), 4.0))),
            line_config={"color": GOOD, "stroke_width": 3, "stroke_opacity": 0.85}
        ))
        self.add(vline)
        self.play(vl_x.animate.set_value(4), run_time=2.0, rate_func=linear)
        self.remove(vline)

        pass_lbl = pill("✓  h(t) PASSES the VLT", GOOD, 28)
        pass_lbl.move_to(RIGHT * 3.4 + UP * 0.6)
        self.play(FadeIn(pass_lbl), run_time=0.6)

        # ── Beat 15: circle counterexample ───────────────────────────────────
        sync_to(self, sents[15]["start"])
        cir_ax = Axes(
            x_range=[-4,4,1], y_range=[-4,4,1],
            x_length=2.6, y_length=2.6,
            axis_config={"color": MUTED, "stroke_width": 1.2, "include_tip": False},
        )
        cir_ax.move_to(RIGHT * 3.4 + DOWN * 1.2)
        r_px = cir_ax.get_x_unit_size() * 3
        circle = Circle(radius=r_px, color=BAD, stroke_width=3).move_to(cir_ax.get_origin())
        cir_lbl = T("x²+y²=9", 24, BAD).next_to(circle, RIGHT, buff=0.1)

        cv_line = Line(
            cir_ax.c2p(0,-3.1), cir_ax.c2p(0,3.1),
            stroke_width=2.5, color=BAD, stroke_opacity=0.7
        )
        top_dot = Dot(cir_ax.c2p(0, 3), radius=0.09, color=BAD)
        bot_dot = Dot(cir_ax.c2p(0,-3), radius=0.09, color=BAD)
        fail_lbl = pill("✗  Circle FAILS the VLT", BAD, 28)
        fail_lbl.move_to(RIGHT * 3.4 + DOWN * 2.55)
        if fail_lbl.get_bottom()[1] < -config.frame_height/2 + 1.2:
            fail_lbl.shift(UP * (-config.frame_height/2 + 1.2 - fail_lbl.get_bottom()[1]))

        self.play(Create(cir_ax), Create(circle), FadeIn(cir_lbl), run_time=0.8)
        self.play(Create(cv_line), FadeIn(top_dot), FadeIn(bot_dot), run_time=0.6)
        self.play(FadeIn(fail_lbl), run_time=0.6)

        sync_to(self, total_dur + 0.15)
        check_layout(self)
