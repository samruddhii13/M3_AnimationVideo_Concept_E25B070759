from manim import *
from helpers import BG, CURVE, POINT, GOOD, BAD, MAXC, fit, boxed, check_bounds, sync_to, configure_scene, load_timings

class Scene1Hook(Scene):
    def construct(self):
        configure_scene(self)
        timings = load_timings("scene1")
        total_audio = timings.get("total_duration", 31.056)
        sentences = {s["beat_index"]: s for s in timings.get("sentences", [])}
        
        # Title
        header = Text("The Real-Life Problem", font_size=42, weight=BOLD, color=WHITE)
        header.to_edge(UP, buff=0.5)
        self.add(header)
        
        # Ruler and Ball setup on the left
        # Ruler height from 0 to 20m. Frame height is 8. Safe area y from -3 to 2.8.
        # Let ruler span y = -2.8 (0m) to y = 2.2 (20m), height = 5.0 units.
        # Scale: 5.0 units / 20m = 0.25 units per metre.
        y_bottom = -2.8
        y_top = 2.2
        ruler_scale = (y_top - y_bottom) / 20.0
        ruler_x = -4.8
        
        ruler_line = Line(start=np.array([ruler_x, y_bottom, 0]), end=np.array([ruler_x, y_top, 0]), color=LIGHT_GRAY, stroke_width=4)
        
        ticks = VGroup()
        tick_labels = VGroup()
        for m in [0, 5, 10, 15, 20]:
            y_pos = y_bottom + m * ruler_scale
            t_line = Line(start=np.array([ruler_x - 0.15, y_pos, 0]), end=np.array([ruler_x + 0.15, y_pos, 0]), color=LIGHT_GRAY, stroke_width=2)
            lbl = Text(f"{m} m", font_size=22, color=LIGHT_GRAY).next_to(t_line, LEFT, buff=0.15)
            ticks.add(t_line)
            tick_labels.add(lbl)
            
        ruler_group = VGroup(ruler_line, ticks, tick_labels)
        
        # Cricket ball (reddish with seam)
        ball = Dot(point=np.array([ruler_x + 0.8, y_bottom, 0]), radius=0.24, color="#E11D48")
        seam = Arc(radius=0.24, start_angle=-PI/2, angle=PI, color=WHITE, stroke_width=2).move_to(ball.get_center())
        ball_mobject = VGroup(ball, seam)
        ball_label = Text("Cricket Ball", font_size=24, color=WHITE).next_to(ball_mobject, RIGHT, buff=0.2)
        
        # Beat 1: [0.00 - 3.34] "Imagine you throw a cricket ball straight up into the air."
        sync_to(self, sentences[1]["start"])
        self.play(FadeIn(ruler_group), FadeIn(ball_mobject), FadeIn(ball_label), run_time=0.8)
        
        # Animate ball throw up to 20m and down to 0m (duration 2.2s), fade out redundant label
        self.play(
            ball_mobject.animate.move_to(np.array([ruler_x + 0.8, y_top, 0])),
            FadeOut(ball_label),
            rate_func=rush_from, run_time=1.1
        )
        self.play(
            ball_mobject.animate.move_to(np.array([ruler_x + 0.8, y_bottom, 0])),
            rate_func=rush_into, run_time=1.1
        )
        
        # Right-side Question panel
        # Beat 2: [3.64 - 5.94] "How high is it after one second?"
        sync_to(self, sentences[2]["start"])
        q1 = Text("1. How high after 1 s?", font_size=32, color=CURVE)
        q1_box = boxed(q1, color=CURVE, pad=0.25).move_to(np.array([1.8, 1.5, 0]))
        
        # Move ball to 15m (t=1s -> h=15m)
        y_15 = y_bottom + 15 * ruler_scale
        h_line_15 = DashedLine(start=np.array([ruler_x, y_15, 0]), end=np.array([ruler_x + 0.8, y_15, 0]), color=CURVE, stroke_width=2)
        h_lbl_15 = Text("h = 15 m", font_size=26, color=CURVE).next_to(np.array([ruler_x + 0.8, y_15, 0]), RIGHT, buff=0.25)
        
        self.play(
            FadeIn(q1_box, shift=LEFT*0.3),
            ball_mobject.animate.move_to(np.array([ruler_x + 0.8, y_15, 0])),
            Create(h_line_15),
            FadeIn(h_lbl_15),
            run_time=1.4
        )
        
        # Beat 3: [6.24 - 8.11] "After two seconds?"
        sync_to(self, sentences[3]["start"])
        q2 = Text("2. After 2 s?", font_size=32, color=MAXC)
        q2_box = boxed(q2, color=MAXC, pad=0.25).next_to(q1_box, DOWN, buff=0.35).align_to(q1_box, LEFT)
        
        y_20 = y_bottom + 20 * ruler_scale
        h_line_20 = DashedLine(start=np.array([ruler_x, y_20, 0]), end=np.array([ruler_x + 0.8, y_20, 0]), color=MAXC, stroke_width=2)
        h_lbl_20 = Text("h = 20 m (Peak)", font_size=26, color=MAXC).next_to(np.array([ruler_x + 0.8, y_20, 0]), RIGHT, buff=0.25)
        
        self.play(
            FadeIn(q2_box, shift=LEFT*0.3),
            ball_mobject.animate.move_to(np.array([ruler_x + 0.8, y_20, 0])),
            Create(h_line_20),
            FadeIn(h_lbl_20),
            run_time=1.3
        )
        
        # Beat 4: [8.41 - 10.52] "And when does it come back down?"
        sync_to(self, sentences[4]["start"])
        q3 = Text("3. When does it land?", font_size=32, color=GOOD)
        q3_box = boxed(q3, color=GOOD, pad=0.25).next_to(q2_box, DOWN, buff=0.35).align_to(q1_box, LEFT)
        
        h_line_0 = DashedLine(start=np.array([ruler_x, y_bottom, 0]), end=np.array([ruler_x + 0.8, y_bottom, 0]), color=GOOD, stroke_width=2)
        h_lbl_0 = Text("h = 0 m (Lands)", font_size=26, color=GOOD).next_to(np.array([ruler_x + 0.8, y_bottom, 0]), RIGHT, buff=0.25)
        
        self.play(
            FadeIn(q3_box, shift=LEFT*0.3),
            ball_mobject.animate.move_to(np.array([ruler_x + 0.8, y_bottom, 0])),
            Create(h_line_0),
            FadeIn(h_lbl_0),
            run_time=1.3
        )
        
        # Beat 5: [10.82 - 15.50] "These questions have exact answers, and the tool that gives them is called a function."
        sync_to(self, sentences[5]["start"])
        # Fade out questions and height lines
        self.play(
            FadeOut(q1_box), FadeOut(q2_box), FadeOut(q3_box),
            FadeOut(h_line_15), FadeOut(h_lbl_15),
            FadeOut(h_line_20), FadeOut(h_lbl_20),
            FadeOut(h_line_0), FadeOut(h_lbl_0),
            FadeOut(ruler_group), FadeOut(ball_mobject), FadeOut(ball_label),
            FadeOut(header),
            run_time=0.8
        )
        
        # Show Concept Title
        header2 = Text("What is a Function?", font_size=42, weight=BOLD, color=WHITE).to_edge(UP, buff=0.5)
        def_line1 = Text("A function gives exact mathematical answers:", font_size=32, color=LIGHT_GRAY)
        def_line2 = Text("It connects each moment in time to its exact height.", font_size=32, color=CURVE)
        def_group = VGroup(def_line1, def_line2).arrange(DOWN, buff=0.3)
        def_card = boxed(def_group, color=CURVE, pad=0.35).move_to(UP*0.8)
        
        self.play(FadeIn(header2), FadeIn(def_card), run_time=1.2)
        
        # Beat 6: [15.80 - 21.95] "A function is a rule that takes an input, here the time, and gives back exactly one output, here the height."
        sync_to(self, sentences[6]["start"])
        self.play(FadeOut(def_card), run_time=0.5)
        
        # Function Machine
        # Input on left, Machine in center, Output on right
        m_box_rect = RoundedRectangle(corner_radius=0.2, width=3.4, height=2.0, color=CURVE, fill_color="#1E293B", fill_opacity=0.9)
        m_title = Text("Function Rule", font_size=28, weight=BOLD, color=WHITE).move_to(m_box_rect.get_center() + UP*0.4)
        m_formula = MathTex(r"h(t) = 20t - 5t^2", font_size=36, color=CURVE).move_to(m_box_rect.get_center() + DOWN*0.35)
        machine = VGroup(m_box_rect, m_title, m_formula).move_to(ORIGIN)
        
        in_label = Text("Input", font_size=28, weight=BOLD, color=POINT)
        in_val = MathTex(r"t = 1\text{ s}", font_size=34, color=WHITE)
        in_group = VGroup(in_label, in_val).arrange(DOWN, buff=0.2)
        in_box = boxed(in_group, color=POINT, pad=0.25).move_to(LEFT*4.2)
        in_arrow = Arrow(start=in_box.get_right(), end=machine.get_left(), color=POINT, buff=0.15)
        
        out_label = Text("Output", font_size=28, weight=BOLD, color=GOOD)
        out_val = MathTex(r"h(1) = 15\text{ m}", font_size=34, color=WHITE)
        out_group = VGroup(out_label, out_val).arrange(DOWN, buff=0.2)
        out_box = boxed(out_group, color=GOOD, pad=0.25).move_to(RIGHT*4.2)
        out_arrow = Arrow(start=machine.get_right(), end=out_box.get_left(), color=GOOD, buff=0.15)
        
        machine_group = fit(VGroup(in_box, in_arrow, machine, out_arrow, out_box)).move_to(DOWN*0.2)
        
        note_one = Text("Exactly ONE output for each input", font_size=28, color=POINT).next_to(machine_group, DOWN, buff=0.45)
        
        self.play(FadeIn(machine), run_time=0.8)
        self.play(FadeIn(in_box), GrowArrow(in_arrow), run_time=0.9)
        self.play(FadeIn(out_box), GrowArrow(out_arrow), run_time=0.9)
        self.play(FadeIn(note_one), run_time=0.8)
        
        # Beat 7: [22.25 - 30.72] "In this video, we will use this ball to understand three things: how inputs map to outputs, how to read a graph, and which key features tell the whole story."
        sync_to(self, sentences[7]["start"])
        self.play(
            FadeOut(machine_group), FadeOut(note_one), FadeOut(header2),
            run_time=0.7
        )
        
        roadmap_title = Text("Three Video Goals", font_size=42, weight=BOLD, color=WHITE).to_edge(UP, buff=0.5)
        g1 = Text("1. Input-Output Mapping: The Definition & Rule", font_size=30, color=POINT)
        g2 = Text("2. Reading the Graph: Height vs. Time Curve", font_size=30, color=CURVE)
        g3 = Text("3. Key Features: Intercepts, Peak, Domain & Rates", font_size=30, color=GOOD)
        
        goals_vgroup = VGroup(g1, g2, g3).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        roadmap_card = fit(boxed(goals_vgroup, color=CURVE, pad=0.4)).move_to(DOWN*0.2)
        
        self.play(FadeIn(roadmap_title), run_time=0.6)
        self.play(FadeIn(roadmap_card), run_time=1.2)
        
        sync_to(self, total_audio + 0.15)
        check_bounds(self)
