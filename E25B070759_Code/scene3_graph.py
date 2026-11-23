"""
scene3_graph.py – Live ball-and-graph split-screen showpiece, VLT & circle test.
Total audio duration: 63.288 s.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from design import *

class Scene3Graph(Base):
    def construct(self):
        timings = load_scene_timings("scene3")
        total_audio = timings.get("total_duration", 63.288)

        hdr = header(3, "Plotting and Reading the Graph", total=6)
        self.add(hdr)

        # ── Beat 0 & 1: (0.00s - 9.32s) Build Split-Screen Stage ────────
        sync_to(self, 0.0)
        ruler, axes, lbls = ball_and_graph_stage()
        self.play(Create(ruler), Create(axes), FadeIn(lbls), run_time=1.8)

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
                dash_length=0.14, color=MUTED, stroke_opacity=0.65
            )
        )
        traced = TracedPath(
            lambda: axes.c2p(t_val.get_value(), h_of(t_val.get_value())),
            stroke_color=CURVE, stroke_width=4
        )

        readout = always_redraw(
            lambda: card(
                T(f"t = {t_val.get_value():.1f} s | h = {h_of(t_val.get_value()):.1f} m", 22, POINT),
                color=POINT, pad=0.18
            ).move_to(RIGHT * 4.6 + UP * 2.6)
        )

        self.play(FadeIn(ball), FadeIn(dot), FadeIn(conn), FadeIn(readout), run_time=0.8)
        self.add(traced)

        # ── Beats 2 to 6: (9.62s - 20.18s) Animate 5 Points with Pauses ──
        # Dropped points and coordinate pills
        fixed_dots  = VGroup()
        fixed_pills = VGroup()

        sample_pts = [
            (0.0, 9.62,  "(0, 0)",   UR, 0.12),
            (1.0, 11.80, "(1, 15)",  UL, 0.12),
            (2.0, 13.97, "(2, 20)",  UP, 0.18),
            (3.0, 16.14, "(3, 15)",  UR, 0.12),
            (4.0, 18.31, "(4, 0)",   DR, 0.12),
        ]

        # Initial point (0,0) at beat 2
        sync_to(self, 9.62)
        d0 = Dot(axes.c2p(0, 0), color=POINT, radius=0.14)
        p0 = pill("(0, 0)", POINT, 20).next_to(d0, UR, buff=0.12)
        fixed_dots.add(d0)
        fixed_pills.add(p0)
        self.play(FadeIn(d0), FadeIn(p0), run_time=0.5)

        for target_t, beat_start, label_str, dir_vec, buff_val in sample_pts[1:]:
            sync_to(self, beat_start - 1.2)
            # Move tracker to target time
            self.play(t_val.animate.set_value(target_t), run_time=1.1, rate_func=linear)
            sync_to(self, beat_start)
            d = Dot(axes.c2p(target_t, h_of(target_t)), color=POINT, radius=0.14)
            p = pill(label_str, POINT, 20).next_to(d, dir_vec, buff=buff_val)
            fixed_dots.add(d)
            fixed_pills.add(p)
            self.play(FadeIn(d), FadeIn(p), run_time=0.5)

        # ── Beat 7: (20.48s - 24.30s) Smooth Parabola Curve Glow ─────────
        sync_to(self, 20.48)
        parabola = axes.plot(lambda t: 20*t - 5*t**2, x_range=[0, 4, 0.03], stroke_color=CURVE, stroke_width=5)
        halo = parabola.copy().set_stroke(CURVE, width=14, opacity=0.18)
        self.play(Create(halo), Create(parabola), run_time=1.8)

        # ── Beat 8: (24.60s - 27.77s) Parabola description ──────────────
        sync_to(self, 24.60)
        # Fade out cluttering labels, keep curve & dots
        self.play(FadeOut(fixed_pills), FadeOut(readout), run_time=0.6)

        # ── Beat 9 & 10: (28.07s - 36.38s) Height vs time, NOT ball path ─
        sync_to(self, 28.07)
        not_path_card = card(
            T("Important Distinction:", 24, BAD, bold=True),
            T("Graph is Height vs Time,", 28, CURVE, bold=True),
            T("NOT the ball's path in space!", 28, INK),
            color=BAD, gap=0.2, pad=0.3
        ).move_to(RIGHT * 3.2 + UP * 1.5)
        self.play(FadeIn(not_path_card), run_time=0.8)

        sync_to(self, 34.01)
        self.wait(1.5)
        self.play(FadeOut(not_path_card), run_time=0.4)

        # ── Beat 11 & 12: (36.68s - 44.45s) Same height twice (Symmetry) ─
        sync_to(self, 36.68)
        h15_line = DashedLine(axes.c2p(1, 15), axes.c2p(3, 15), color=MAXC, stroke_width=3, dash_length=0.14)
        sym_pill = pill("h(1) = h(3) = 15 m (Same height twice)", MAXC, 22).move_to(RIGHT * 3.0 + UP * 1.8)
        self.play(Create(h15_line), FadeIn(sym_pill), run_time=0.9)

        sync_to(self, 41.93)
        allow_pill = pill("Two inputs → One output: ALLOWED ✓", GOOD, 24).move_to(RIGHT * 3.0 + UP * 0.9)
        self.play(FadeIn(allow_pill), run_time=0.8)
        self.wait(1.2)
        self.play(FadeOut(VGroup(h15_line, sym_pill, allow_pill)), run_time=0.4)

        # ── Beat 13 & 14: (44.75s - 57.02s) Vertical Line Test ───────────
        sync_to(self, 44.75)
        vlt_title = card(
            T("Vertical Line Test (VLT)", 26, INK, bold=True),
            T("Each vertical line must cross at most ONCE.", 24, MUTED),
            color=CURVE, pad=0.25
        ).move_to(RIGHT * 3.0 + UP * 2.2)
        self.play(FadeIn(vlt_title), run_time=0.8)

        sync_to(self, 50.35)
        # Vertical sweep line across graph
        sweep_x = ValueTracker(0.2)
        v_sweep = always_redraw(
            lambda: Line(
                axes.c2p(sweep_x.get_value(), 0),
                axes.c2p(sweep_x.get_value(), 25),
                color=GOOD, stroke_width=3
            )
        )
        self.add(v_sweep)
        self.play(sweep_x.animate.set_value(3.8), run_time=2.8, rate_func=linear)
        vlt_pass = pill("Passes VLT: Exactly ONE height per instant ✓", GOOD, 24).move_to(RIGHT * 3.0 + DOWN * 2.2)
        self.play(FadeIn(vlt_pass), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(VGroup(vlt_title, v_sweep, vlt_pass)), run_time=0.4)

        # ── Beat 15: (57.32s - 63.29s) Circle Fails VLT (x^2 + y^2 = 9) ──
        sync_to(self, 57.32)
        # Scale and shrink graph to left
        graph_all = VGroup(ruler, axes, lbls, halo, parabola, fixed_dots, ball, dot, conn, traced)
        self.play(graph_all.animate.scale(0.65).move_to(LEFT * 2.5 + DOWN * 0.15), run_time=0.8)

        # Circle axes on right
        c_axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=3.4,
            y_length=3.4,
            axis_config={"color": MUTED, "stroke_width": 1.5, "include_tip": False, "font_size": 18},
            x_axis_config={"numbers_to_include": [-3, 0, 3]},
            y_axis_config={"numbers_to_include": [-3, 3]}
        ).move_to(RIGHT * 3.3 + DOWN * 0.15)

        circle_curve = c_axes.plot_parametric_curve(
            lambda u: np.array([3*np.cos(u), 3*np.sin(u), 0]),
            t_range=[0, TAU, 0.04],
            color=BAD, stroke_width=3.5
        )
        c_title = T("Circle: x² + y² = 9", 24, BAD, bold=True).next_to(c_axes, UP, buff=0.15)

        # Vertical line at x = 0
        vline_bad = Line(c_axes.c2p(0, -3.6), c_axes.c2p(0, 3.6), color=POINT, stroke_width=3)
        dot_top = Dot(c_axes.c2p(0, 3), color=BAD, radius=0.12)
        dot_bot = Dot(c_axes.c2p(0, -3), color=BAD, radius=0.12)
        fail_pill = pill("x = 0 gives y = ±3: FAILS VLT ✗", BAD, 22).move_to(RIGHT * 3.3 + DOWN * 2.3)

        self.play(Create(c_axes), Create(circle_curve), FadeIn(c_title), run_time=0.9)
        self.play(Create(vline_bad), FadeIn(dot_top), FadeIn(dot_bot), FadeIn(fail_pill), run_time=0.9)

        # Hold until total audio length
        sync_to(self, total_audio)
        check_layout(self)
