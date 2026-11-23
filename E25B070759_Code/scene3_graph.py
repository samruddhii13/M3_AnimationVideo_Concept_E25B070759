from manim import *
from helpers import BG, CURVE, POINT, GOOD, BAD, MAXC, fit, boxed, check_bounds, sync_to, configure_scene, load_timings

class Scene3Graph(Scene):
    def construct(self):
        configure_scene(self)
        timings = load_timings("scene3")
        total_audio = timings.get("total_duration", 63.288)
        sentences = {s["beat_index"]: s for s in timings.get("sentences", [])}
        
        # Header
        header = Text("Plotting the Graph & Vertical Line Test", font_size=40, weight=BOLD, color=WHITE)
        header.to_edge(UP, buff=0.45)
        self.add(header)
        
        # Right Half: Axes
        # Horizontal t: 0 to 5, Vertical h: 0 to 25
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 25, 5],
            x_length=5.6,
            y_length=4.2,
            axis_config={"color": LIGHT_GRAY, "include_numbers": True, "font_size": 22},
            tips=True
        ).move_to(np.array([3.0, -0.6, 0]))
        
        x_label = Text("Time t (s)", font_size=22, color=LIGHT_GRAY).next_to(axes.x_axis.get_end(), DOWN, buff=0.25).shift(LEFT*0.6)
        y_label = Text("Height h (m)", font_size=22, color=LIGHT_GRAY).next_to(axes.y_axis.get_end(), UP, buff=0.2).shift(RIGHT*0.4)
        axes_group = VGroup(axes, x_label, y_label)
        
        # Left Half: Table of values
        table_title = Text("Input-Output Pairs", font_size=26, weight=BOLD, color=WHITE).move_to(np.array([-4.2, 1.6, 0]))
        th_t = MathTex(r"t\text{ (s)}", font_size=28, color=POINT)
        th_h = MathTex(r"h(t)\text{ (m)}", font_size=28, color=GOOD)
        th_group = VGroup(th_t, th_h).arrange(RIGHT, buff=0.6).next_to(table_title, DOWN, buff=0.25)
        sep_h = Line(start=np.array([-5.6, th_group.get_bottom()[1] - 0.1, 0]), end=np.array([-2.8, th_group.get_bottom()[1] - 0.1, 0]), color=GRAY)
        
        # Beat 1: [0.00 - 2.62] "Now let's turn this mapping into a graph."
        sync_to(self, sentences[1]["start"])
        self.play(FadeIn(table_title), FadeIn(th_group), Create(sep_h), run_time=1.0)
        
        # Beat 2: [2.92 - 9.32] "Each input-output pair becomes a point: time goes on the horizontal axis, and height goes on the vertical axis."
        sync_to(self, sentences[2]["start"])
        self.play(FadeIn(axes_group), run_time=1.4)
        
        # Table rows & points
        data = [
            (0, 0, sentences[3]["start"]),    # Beat 3: "Zero comma zero."
            (1, 15, sentences[4]["start"]),   # Beat 4: "One comma fifteen."
            (2, 20, sentences[5]["start"]),   # Beat 5: "Two comma twenty."
            (3, 15, sentences[6]["start"]),   # Beat 6: "Three comma fifteen."
            (4, 0, sentences[7]["start"])     # Beat 7: "Four comma zero."
        ]
        
        row_mobs = []
        plot_dots = VGroup()
        for i, (t_val, h_val, b_time) in enumerate(data):
            sync_to(self, b_time)
            y_r = sep_h.get_bottom()[1] - 0.35 - i * 0.48
            r_t = MathTex(str(t_val), font_size=28, color=WHITE).move_to(np.array([th_t.get_center()[0], y_r, 0]))
            r_h = MathTex(str(h_val), font_size=28, color=WHITE).move_to(np.array([th_h.get_center()[0], y_r, 0]))
            row_grp = VGroup(r_t, r_h)
            row_mobs.append(row_grp)
            
            dot = Dot(point=axes.c2p(t_val, h_val), radius=0.1, color=POINT)
            plot_dots.add(dot)
            self.play(FadeIn(row_grp), FadeIn(dot, scale=1.5), run_time=0.7)
            
        # Beat 8: [20.48 - 24.30] "Join the points smoothly, and we get a curve called a parabola."
        sync_to(self, sentences[8]["start"])
        parabola = axes.plot(lambda t: 20*t - 5*t**2, x_range=[0, 4], color=CURVE, stroke_width=4)
        curve_label = MathTex(r"h(t) = 20t - 5t^2", font_size=26, color=CURVE).next_to(axes.c2p(2, 20), UP, buff=0.2)
        
        self.play(Create(parabola), run_time=1.8)
        self.play(FadeIn(curve_label), run_time=0.6)
        
        # Beat 9: [24.60 - 27.77] "It rises, peaks, and falls symmetrically."
        sync_to(self, sentences[9]["start"])
        peak_note = Text("Symmetric Parabola: Rises, Peaks, Falls", font_size=22, color=MAXC).move_to(np.array([-4.2, -1.8, 0]))
        peak_box = boxed(peak_note, color=MAXC, pad=0.2).move_to(np.array([-4.2, -1.8, 0]))
        self.play(FadeIn(peak_box), run_time=0.9)
        
        # Beat 10: [28.07 - 33.71] "Be careful: this is not the path of the ball in space, because the ball moves straight up and down."
        sync_to(self, sentences[10]["start"])
        self.play(FadeOut(peak_box), run_time=0.4)
        warning_t1 = Text("NOT the Spatial Path!", font_size=24, weight=BOLD, color=BAD)
        warning_t2 = Text("Ball moves straight UP and DOWN.", font_size=22, color=WHITE)
        warning_grp = VGroup(warning_t1, warning_t2).arrange(DOWN, buff=0.2)
        warning_box = boxed(warning_grp, color=BAD, pad=0.2).move_to(np.array([-4.2, -1.8, 0]))
        self.play(FadeIn(warning_box), run_time=1.0)
        
        # Beat 11: [34.01 - 36.38] "The graph shows height against time."
        sync_to(self, sentences[11]["start"])
        h_vs_t = Text("Graph = Height vs. Time", font_size=24, weight=BOLD, color=POINT)
        h_vs_t_box = boxed(h_vs_t, color=POINT, pad=0.2).move_to(np.array([-4.2, -1.8, 0]))
        self.play(Transform(warning_box, h_vs_t_box), run_time=0.8)
        
        # Beat 12: [36.68 - 41.63] "Notice also that at one second and at three seconds the height is the same, fifteen metres."
        sync_to(self, sentences[12]["start"])
        self.play(FadeOut(warning_box), run_time=0.4)
        
        h_line_15 = DashedLine(start=axes.c2p(1, 15), end=axes.c2p(3, 15), color=POINT, stroke_width=3)
        lbl_two_in = MathTex(r"h(1) = h(3) = 15\text{ m}", font_size=26, color=POINT).next_to(h_line_15, DOWN, buff=0.2)
        self.play(Create(h_line_15), FadeIn(lbl_two_in), run_time=1.2)
        
        # Beat 13: [41.93 - 44.45] "Two different inputs may share an output."
        sync_to(self, sentences[13]["start"])
        obs_1 = Text("2 Inputs -> 1 Output (Allowed!)", font_size=22, weight=BOLD, color=GOOD)
        obs_1_box = boxed(obs_1, color=GOOD, pad=0.2).move_to(np.array([-4.2, -1.8, 0]))
        self.play(FadeIn(obs_1_box), run_time=0.8)
        
        # Beat 14: [44.75 - 50.05] "But one input can never have two outputs, because at any moment the ball has only one height."
        sync_to(self, sentences[14]["start"])
        obs_2 = Text("1 Input -> 2 Outputs (Forbidden!)", font_size=22, weight=BOLD, color=BAD)
        obs_2_box = boxed(obs_2, color=BAD, pad=0.2).next_to(obs_1_box, DOWN, buff=0.2)
        self.play(FadeIn(obs_2_box), run_time=1.0)
        
        # Beat 15: [50.35 - 57.02] "That gives us the vertical line test: if every vertical line crosses a graph at most once, the graph shows a function."
        sync_to(self, sentences[15]["start"])
        self.play(FadeOut(h_line_15), FadeOut(lbl_two_in), FadeOut(obs_1_box), FadeOut(obs_2_box), run_time=0.5)
        
        vlt_badge = Text("Vertical Line Test: At most 1 intersection", font_size=22, weight=BOLD, color=GOOD)
        vlt_box = boxed(vlt_badge, color=GOOD, pad=0.2).move_to(np.array([-4.2, -1.8, 0]))
        self.play(FadeIn(vlt_box), run_time=0.6)
        
        # Sweep vertical line across axes from t=0.5 to t=3.5
        v_line = Line(start=axes.c2p(1.0, 0), end=axes.c2p(1.0, 24), color=GOOD, stroke_width=3)
        v_dot = Dot(point=axes.c2p(1.0, 15), radius=0.1, color=GOOD)
        self.play(Create(v_line), FadeIn(v_dot), run_time=0.6)
        
        self.play(
            v_line.animate.move_to(axes.c2p(2.0, 12)),
            v_dot.animate.move_to(axes.c2p(2.0, 20)),
            run_time=1.2
        )
        self.play(
            v_line.animate.move_to(axes.c2p(3.0, 12)),
            v_dot.animate.move_to(axes.c2p(3.0, 15)),
            run_time=1.2
        )
        self.play(FadeOut(v_line), FadeOut(v_dot), run_time=0.4)
        
        # Beat 16: [57.32 - 62.41] "A circle fails this test, because the line at ex equals zero crosses it twice."
        sync_to(self, sentences[16]["start"])
        self.play(FadeOut(vlt_box), run_time=0.3)
        
        # Replace table area with circle test
        circle_title = MathTex(r"\text{Contrast: } x^2 + y^2 = 9", font_size=32, color=BAD).move_to(np.array([-4.2, 1.4, 0]))
        circle_shape = Circle(radius=1.0, color=BAD, stroke_width=3.5).next_to(circle_title, DOWN, buff=0.35)
        c_axis_v = Line(start=circle_shape.get_top() + UP*0.35, end=circle_shape.get_bottom() + DOWN*0.35, color=BAD, stroke_width=2.5)
        dot_top = Dot(point=circle_shape.get_top(), radius=0.1, color=BAD)
        lbl_top = MathTex(r"(0, 3)", font_size=26, color=WHITE).next_to(dot_top, RIGHT, buff=0.15)
        dot_bot = Dot(point=circle_shape.get_bottom(), radius=0.1, color=BAD)
        lbl_bot = MathTex(r"(0, -3)", font_size=26, color=WHITE).next_to(dot_bot, RIGHT, buff=0.15)
        fail_badge = Text("Line x = 0 crosses TWICE\n=> NOT a function!", font_size=24, weight=BOLD, line_spacing=1.2, color=BAD)
        fail_box = boxed(fail_badge, color=BAD, pad=0.25).next_to(circle_shape, DOWN, buff=0.35)
        
        self.play(
            FadeOut(table_title), FadeOut(th_group), FadeOut(sep_h), *[FadeOut(m) for m in row_mobs],
            FadeIn(circle_title), Create(circle_shape), Create(c_axis_v),
            FadeIn(dot_top), FadeIn(lbl_top), FadeIn(dot_bot), FadeIn(lbl_bot),
            FadeIn(fail_box),
            run_time=2.0
        )
        
        sync_to(self, total_audio + 0.15)
        check_bounds(self)
