"""
scene5_interpretation.py – Reading the graph: real-life meaning of each feature.
Total audio duration: 35.832 s.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from design import *

class Scene5Interpretation(Base):
    def construct(self):
        timings = load_scene_timings("scene5")
        total_audio = timings.get("total_duration", 35.832)

        hdr = header(5, "Reading the Graph as a Story", total=6)
        self.add(hdr)

        # ── Split-screen stage with full parabola visible ────────────────
        sync_to(self, 0.0)
        ruler, axes, lbls = ball_and_graph_stage()
        curve = axes.plot(lambda t: 20*t - 5*t**2, x_range=[0, 4, 0.03], stroke_color=CURVE, stroke_width=4.5)
        halo  = curve.copy().set_stroke(CURVE, width=12, opacity=0.18)

        t_val = ValueTracker(0.0)
        ball = always_redraw(
            lambda: make_ball(0.24).move_to(ruler.n2p(h_of(t_val.get_value())))
        )
        dot = always_redraw(
            lambda: Dot(axes.c2p(t_val.get_value(), h_of(t_val.get_value())), color=POINT, radius=0.13)
        )
        conn = always_redraw(
            lambda: DashedLine(
                ruler.n2p(h_of(t_val.get_value())) + RIGHT * 0.28,
                axes.c2p(t_val.get_value(), h_of(t_val.get_value())),
                dash_length=0.14, color=MUTED, stroke_opacity=0.6
            )
        )

        self.play(Create(ruler), Create(axes), FadeIn(lbls), Create(halo), Create(curve), run_time=1.4)
        self.play(FadeIn(ball), FadeIn(dot), FadeIn(conn), run_time=0.6)

        # Active highlight ring helper
        def highlight_ring(point, col=GOOD):
            return Circle(radius=0.32, color=col, stroke_width=3).move_to(point)

        # Active callout card in upper-right zone (safe from graph curve)
        active_card_box = VGroup()

        # ── Beat 1: (2.87s - 6.61s) "The starting point: height 0" ───────
        sync_to(self, 2.87)
        ring1 = highlight_ring(axes.c2p(0, 0), GOOD)
        p1 = card(
            T("1. Starting Point (t = 0)", 22, GOOD, bold=True),
            T("Leaves hand at height 0 m", 24, INK),
            color=GOOD, pad=0.2
        ).move_to(RIGHT * 3.4 + UP * 2.2)
        self.play(t_val.animate.set_value(0.0), Create(ring1), FadeIn(p1), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(ring1), FadeOut(p1), run_time=0.4)

        # ── Beat 2: (6.91s - 12.50s) "The peak: stops rising at 20 m, 2 s" ─
        sync_to(self, 6.91)
        ring2 = highlight_ring(axes.c2p(2, 20), MAXC)
        p2 = card(
            T("2. Peak Moment (t = 2 s)", 22, MAXC, bold=True),
            T("Stops rising: 20 m maximum", 24, INK),
            color=MAXC, pad=0.2
        ).move_to(RIGHT * 3.4 + UP * 2.2)
        self.play(t_val.animate.set_value(2.0), Create(ring2), FadeIn(p2), run_time=1.8, rate_func=linear)
        self.wait(2.2)
        self.play(FadeOut(ring2), FadeOut(p2), run_time=0.4)

        # ── Beat 3: (12.80s - 16.28s) "Lands after 4 s" ──────────────────
        sync_to(self, 12.80)
        ring3 = highlight_ring(axes.c2p(4, 0), BAD)
        p3 = card(
            T("3. Landing (t = 4 s)", 22, BAD, bold=True),
            T("Hits the ground at 4 seconds", 24, INK),
            color=BAD, pad=0.2
        ).move_to(RIGHT * 3.4 + UP * 2.2)
        self.play(t_val.animate.set_value(4.0), Create(ring3), FadeIn(p3), run_time=1.6, rate_func=linear)
        self.wait(1.0)
        self.play(FadeOut(ring3), FadeOut(p3), run_time=0.4)

        # ── Beat 4: (16.58s - 20.98s) "Symmetry: fall time = rise time" ──
        sync_to(self, 16.58)
        sym_line = DashedLine(axes.c2p(2, 0), axes.c2p(2, 21), color=CURVE, stroke_width=2.5)
        p4 = card(
            T("4. Symmetry", 22, CURVE, bold=True),
            T("Rise time = Fall time = 2 s", 24, INK),
            color=CURVE, pad=0.2
        ).move_to(RIGHT * 3.4 + UP * 2.2)
        self.play(Create(sym_line), FadeIn(p4), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(sym_line), FadeOut(p4), run_time=0.4)

        # ── Beat 5: (21.28s - 26.68s) "Domain: valid only for 0 <= t <= 4" ─
        sync_to(self, 21.28)
        dom_bracket = Line(axes.c2p(0, 0), axes.c2p(4, 0), color=POINT, stroke_width=7)
        p5 = card(
            T("5. Physical Domain", 22, POINT, bold=True),
            T("Model valid only for 0 ≤ t ≤ 4 s", 24, INK),
            color=POINT, pad=0.2
        ).move_to(RIGHT * 3.4 + UP * 2.2)
        self.play(Create(dom_bracket), FadeIn(p5), run_time=1.0)
        self.wait(2.5)
        self.play(FadeOut(dom_bracket), FadeOut(p5), run_time=0.4)

        # ── Beat 6 & 7: (26.98s - 35.83s) Concluding synthesis ───────────
        sync_to(self, 26.98)
        summary_pill = pill("The graph tells the complete physical story at a glance!", GOOD, 24).move_to(DOWN * 2.2)
        self.play(FadeIn(summary_pill), run_time=1.0)

        # Re-scrub ball 0 to 4 smoothly
        t_val.set_value(0.0)
        self.play(t_val.animate.set_value(4.0), run_time=4.0, rate_func=linear)

        # Hold until total audio length
        sync_to(self, total_audio)
        check_layout(self)
