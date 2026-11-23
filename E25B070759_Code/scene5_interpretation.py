"""Scene 5 – Physical Interpretation / Story.
Template B: left = moving ball on ruler, right = parabola with callouts.
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

class Scene5Interpretation(Base):
    def construct(self):
        sents, total_dur = _load_scene_timings("scene5")

        hdr = header(5, "Physical Story")
        self.add(hdr)

        def h(t): return 20*t - 5*t**2

        # ── LEFT: vertical ruler ──────────────────────────────────────────────
        sync_to(self, sents[0]["start"])
        ruler_ax = Axes(
            x_range=[0,1,1], y_range=[0,25,5],
            x_length=0.5, y_length=4.2,
            axis_config={"color": MUTED, "stroke_width": 1.5,
                         "include_tip": True, "tip_length": 0.15},
            y_axis_config={"numbers_to_include": [0,5,10,15,20,25]},
        )
        ruler_lbl = Text("h (m)", font=FONT, font_size=20, color=MUTED)
        ruler_grp = VGroup(ruler_ax, ruler_lbl.next_to(ruler_ax, UP, buff=0.1))
        ruler_grp.move_to(LEFT * 5.5 + DOWN * 0.25)
        if ruler_grp.get_left()[0] < -config.frame_width/2 + SAFE:
            ruler_grp.shift(RIGHT * (-config.frame_width/2 + SAFE - ruler_grp.get_left()[0]))

        t_track = ValueTracker(0.0)
        ball = always_redraw(lambda: Dot(
            ruler_ax.c2p(0.5, h(t_track.get_value())),
            radius=0.14, color=CURVE
        ))
        ball_lbl = always_redraw(lambda: T(
            f"h={h(t_track.get_value()):.0f}m", 22, POINT
        ).next_to(ruler_ax.c2p(0.5, h(t_track.get_value())), RIGHT, buff=0.14))

        self.play(Create(ruler_grp), run_time=0.8)
        self.add(ball, ball_lbl)

        # ── RIGHT: parabola ───────────────────────────────────────────────────
        ax = Axes(
            x_range=[0,5,1], y_range=[0,25,5],
            x_length=5.2, y_length=4.0,
            axis_config={"color": INK, "stroke_width": 2,
                         "include_tip": True, "tip_length": 0.18},
            x_axis_config={"numbers_to_include": [0,1,2,3,4]},
            y_axis_config={"numbers_to_include": [0,10,20]},
        )
        x_lbl = ax.get_x_axis_label(
            Text("t (s)", font=FONT, font_size=20, color=MUTED),
            edge=RIGHT, direction=RIGHT, buff=0.15)
        y_lbl = ax.get_y_axis_label(
            Text("h (m)", font=FONT, font_size=20, color=MUTED),
            edge=UP, direction=UP, buff=0.15)
        ax_grp = VGroup(ax, x_lbl, y_lbl)
        place(ax_grp, 5.4, 4.6, RIGHT * 3.0 + DOWN * 0.25)

        curve_glow = glow(ax.plot(h, x_range=[0,4,0.05], color=CURVE), CURVE)
        graph_dot  = always_redraw(lambda: Dot(
            ax.c2p(t_track.get_value(), h(t_track.get_value())),
            radius=0.11, color=POINT
        ))

        self.play(Create(ax_grp), Create(curve_glow), run_time=1.0)
        self.add(graph_dot)

        # ── Rising: t 0→2 ────────────────────────────────────────────────────
        sync_to(self, sents[1]["start"])
        self.play(t_track.animate.set_value(2), run_time=2.5, rate_func=linear)

        # Peak callout
        sync_to(self, sents[2]["start"])
        peak_pt   = ax.c2p(2, 20)
        peak_card = card(
            T("Peak: t=2 s, h=20 m", 28, MAXC, bold=True),
            color=MAXC, pad=0.3
        )
        peak_card.move_to(RIGHT * 3.0 + UP * 1.3)
        if peak_card.get_top()[1] > config.frame_height/2 - SAFE:
            peak_card.shift(DOWN * (peak_card.get_top()[1] - config.frame_height/2 + SAFE + 0.1))
        peak_arr = Arrow(peak_card.get_bottom(), peak_pt + UP * 0.15,
                         buff=0.12, stroke_width=3, tip_length=0.18, color=MAXC)
        self.play(FadeIn(peak_card), GrowArrow(peak_arr), run_time=0.8)

        # ── Falling: t 2→4 ───────────────────────────────────────────────────
        sync_to(self, sents[3]["start"])
        self.play(FadeOut(peak_card), FadeOut(peak_arr), run_time=0.3)
        self.play(t_track.animate.set_value(4), run_time=2.5, rate_func=linear)

        # ── Two inputs, one output ────────────────────────────────────────────
        sync_to(self, sents[4]["start"])
        d1 = Dot(ax.c2p(1,15), radius=0.10, color=POINT)
        d3 = Dot(ax.c2p(3,15), radius=0.10, color=POINT)
        eq_card = card(
            T("h(1) = h(3) = 15 m", 28, POINT, bold=True),
            T("Two inputs → same output  (allowed)", 24, MUTED),
            color=POINT, pad=0.38
        )
        eq_card.move_to(RIGHT * 3.2 + DOWN * 1.1)
        if eq_card.width  > 5.6: eq_card.scale_to_fit_width(5.6)
        if eq_card.get_right()[0] > config.frame_width/2 - SAFE:
            eq_card.shift(LEFT * (eq_card.get_right()[0] - config.frame_width/2 + SAFE))
        if eq_card.get_bottom()[1] < -config.frame_height/2 + 1.2:
            eq_card.shift(UP * (-config.frame_height/2 + 1.2 - eq_card.get_bottom()[1]))
        self.play(FadeIn(d1), FadeIn(d3), FadeIn(eq_card), run_time=0.8)

        # ── Takeaway ──────────────────────────────────────────────────────────
        sync_to(self, sents[7]["start"])
        self.play(FadeOut(d1), FadeOut(d3), FadeOut(eq_card), run_time=0.3)
        takeaway = card(
            T("The graph encodes the entire flight", 30, INK, bold=True),
            T("in one picture.", 30, INK),
            color=CURVE, pad=0.42
        )
        takeaway.move_to(RIGHT * 3.2 + DOWN * 0.6)
        if takeaway.width > 5.6: takeaway.scale_to_fit_width(5.6)
        if takeaway.get_right()[0] > config.frame_width/2 - SAFE:
            takeaway.shift(LEFT * (takeaway.get_right()[0] - config.frame_width/2 + SAFE))
        if takeaway.get_bottom()[1] < -config.frame_height/2 + 1.2:
            takeaway.shift(UP * (-config.frame_height/2 + 1.2 - takeaway.get_bottom()[1]))
        self.play(FadeIn(takeaway), run_time=0.8)

        sync_to(self, total_dur + 0.15)
        check_layout(self)
