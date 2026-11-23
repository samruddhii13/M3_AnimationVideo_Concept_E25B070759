from manim import *
from helpers import BG, CURVE, POINT, GOOD, BAD, MAXC, fit, boxed, check_bounds, sync_to, configure_scene, load_timings

class Scene2Concept(Scene):
    def construct(self):
        configure_scene(self)
        timings = load_timings("scene2")
        total_audio = timings.get("total_duration", 60.312)
        sentences = {s["beat_index"]: s for s in timings.get("sentences", [])}
        
        # Header
        header = Text("Function Concept & Mapping", font_size=42, weight=BOLD, color=WHITE)
        header.to_edge(UP, buff=0.5)
        self.add(header)
        
        # Beat 1: [0.00 - 1.94] "Let's make this precise."
        sync_to(self, sentences[1]["start"])
        
        # Beat 2: [2.24 - 6.08] "A function assigns to each allowed input exactly one output."
        sync_to(self, sentences[2]["start"])
        def_t1 = Text("Core Definition of a Function:", font_size=32, weight=BOLD, color=WHITE)
        def_t2 = Text("Each allowed input has exactly ONE output.", font_size=34, weight=BOLD, color=POINT)
        def_group = VGroup(def_t1, def_t2).arrange(DOWN, buff=0.3)
        def_box = fit(boxed(def_group, color=POINT, pad=0.35)).move_to(UP*1.2)
        self.play(FadeIn(def_box, shift=DOWN*0.2), run_time=1.0)
        
        # Beat 3: [6.38 - 9.29] "Our input is the time, tee, in seconds."
        sync_to(self, sentences[3]["start"])
        in_t = Text("Input: Time t (s)", font_size=30, weight=BOLD, color=POINT)
        in_badge = boxed(in_t, color=POINT, pad=0.25).move_to(LEFT*3.0 + DOWN*0.6)
        self.play(FadeIn(in_badge, shift=RIGHT*0.2), run_time=0.9)
        
        # Beat 4: [9.59 - 12.90] "Our output is the height, aitch of tee, in metres."
        sync_to(self, sentences[4]["start"])
        out_t = Text("Output: Height h(t) (m)", font_size=30, weight=BOLD, color=GOOD)
        out_badge = boxed(out_t, color=GOOD, pad=0.25).move_to(RIGHT*3.0 + DOWN*0.6)
        self.play(FadeIn(out_badge, shift=LEFT*0.2), run_time=0.9)
        
        # Beat 5: [13.20 - 21.72] "If the ball is thrown upward at twenty metres per second, and we ignore air resistance, physics gives the rule: aitch of tee equals twenty tee minus five tee squared."
        sync_to(self, sentences[5]["start"])
        self.play(FadeOut(def_box), FadeOut(in_badge), FadeOut(out_badge), run_time=0.6)
        
        rule_title = Text("The Mathematical Rule", font_size=32, weight=BOLD, color=WHITE)
        formula = MathTex(r"h(t) = 20t - 5t^2", font_size=44, color=CURVE)
        rule_group = VGroup(rule_title, formula).arrange(DOWN, buff=0.3)
        rule_box = boxed(rule_group, color=CURVE, pad=0.35).move_to(UP*1.2)
        self.play(FadeIn(rule_box, shift=DOWN*0.2), run_time=1.0)
        
        # Beat 6: [22.02 - 26.75] "Here we take gravity as ten metres per second squared, to keep the numbers clean."
        sync_to(self, sentences[6]["start"])
        note = Text("Physical Assumption: g taken as 10 m/s², air resistance ignored", font_size=24, color=LIGHT_GRAY)
        note_box = boxed(note, color=GRAY, pad=0.2).next_to(rule_box, DOWN, buff=0.3)
        self.play(FadeIn(note_box), run_time=0.9)
        
        # Beat 7: [27.05 - 28.92] "Let's test the rule."
        sync_to(self, sentences[7]["start"])
        test_title = Text("Testing at t = 1 s:", font_size=28, weight=BOLD, color=POINT).move_to(DOWN*1.2)
        self.play(FadeIn(test_title), run_time=0.7)
        
        # Beat 8: [29.22 - 33.66] "At tee equals one, we get twenty minus five, which is fifteen metres."
        sync_to(self, sentences[8]["start"])
        calc = MathTex(r"h(1) = 20(1) - 5(1)^2 = 20 - 5 = 15\text{ m}", font_size=38, color=WHITE)
        calc.next_to(test_title, DOWN, buff=0.25)
        calc_box = boxed(VGroup(test_title, calc), color=GOOD, pad=0.25).move_to(DOWN*1.5)
        self.play(FadeOut(test_title), FadeIn(calc_box), run_time=1.0)
        
        # Beat 9: [33.96 - 35.95] "Here is the full mapping."
        sync_to(self, sentences[9]["start"])
        self.play(
            FadeOut(rule_box), FadeOut(note_box), FadeOut(calc_box),
            run_time=0.7
        )
        
        # Mapping Diagram Setup
        # Left column: Domain (Inputs: 0, 1, 2, 3, 4)
        # Right column: Range (Outputs: 0, 15, 20)
        domain_label = Text("Domain (Inputs t)", font_size=28, weight=BOLD, color=POINT).move_to(np.array([-3.2, 1.8, 0]))
        range_label = Text("Range (Outputs h)", font_size=28, weight=BOLD, color=GOOD).move_to(np.array([3.2, 1.8, 0]))
        
        # Oval backgrounds
        in_oval = RoundedRectangle(corner_radius=0.4, width=2.4, height=3.8, color=POINT, fill_color="#1E293B", fill_opacity=0.6).move_to(np.array([-3.2, -0.4, 0]))
        out_oval = RoundedRectangle(corner_radius=0.4, width=2.4, height=3.8, color=GOOD, fill_color="#1E293B", fill_opacity=0.6).move_to(np.array([3.2, -0.4, 0]))
        
        inputs = [0, 1, 2, 3, 4]
        in_mobs = {}
        for i, val in enumerate(inputs):
            y_pos = 0.9 - i * 0.65
            dot = Dot(point=np.array([-2.4, y_pos, 0]), radius=0.08, color=POINT)
            lbl = MathTex(str(val), font_size=34, color=WHITE).next_to(dot, LEFT, buff=0.2)
            in_mobs[val] = (dot, lbl, np.array([-2.3, y_pos, 0]))
            
        outputs = [0, 15, 20]
        out_mobs = {}
        out_y = {0: -1.05, 15: -0.05, 20: 0.95}
        for val in outputs:
            y_pos = out_y[val]
            dot = Dot(point=np.array([2.4, y_pos, 0]), radius=0.08, color=GOOD)
            lbl = MathTex(str(val), font_size=34, color=WHITE).next_to(dot, RIGHT, buff=0.2)
            out_mobs[val] = (dot, lbl, np.array([2.3, y_pos, 0]))
            
        diagram_base = VGroup(
            domain_label, range_label, in_oval, out_oval,
            *[m[0] for m in in_mobs.values()], *[m[1] for m in in_mobs.values()],
            *[m[0] for m in out_mobs.values()], *[m[1] for m in out_mobs.values()]
        )
        self.play(FadeIn(diagram_base), run_time=1.0)
        
        def make_arrow(in_val, out_val, col=WHITE):
            p1 = in_mobs[in_val][2]
            p2 = out_mobs[out_val][2]
            return Arrow(start=p1, end=p2, color=col, buff=0.1, stroke_width=3, max_tip_length_to_length_ratio=0.15)
            
        # Beat 10: [36.25 - 38.15] "Zero goes to zero."
        sync_to(self, sentences[10]["start"])
        arr0 = make_arrow(0, 0, col=GOOD)
        self.play(GrowArrow(arr0), run_time=0.9)
        
        # Beat 11: [38.45 - 40.34] "One goes to fifteen."
        sync_to(self, sentences[11]["start"])
        arr1 = make_arrow(1, 15, col=CURVE)
        self.play(GrowArrow(arr1), run_time=0.9)
        
        # Beat 12: [40.64 - 42.52] "Two goes to twenty."
        sync_to(self, sentences[12]["start"])
        arr2 = make_arrow(2, 20, col=MAXC)
        self.play(GrowArrow(arr2), run_time=0.9)
        
        # Beat 13: [42.82 - 44.69] "Three goes to fifteen."
        sync_to(self, sentences[13]["start"])
        arr3 = make_arrow(3, 15, col=CURVE)
        self.play(GrowArrow(arr3), run_time=0.9)
        
        # Beat 14: [44.99 - 46.88] "And four goes to zero."
        sync_to(self, sentences[14]["start"])
        arr4 = make_arrow(4, 0, col=GOOD)
        self.play(GrowArrow(arr4), run_time=0.9)
        
        # Beat 15: [47.18 - 50.83] "Notice that every input has exactly one arrow leaving it."
        sync_to(self, sentences[15]["start"])
        key_obs = Text("Every input has exactly ONE outgoing arrow!", font_size=28, weight=BOLD, color=POINT)
        key_box = boxed(key_obs, color=POINT, pad=0.25).move_to(DOWN*2.6)
        self.play(FadeIn(key_box, shift=UP*0.2), run_time=1.0)
        
        # Beat 16: [51.13 - 53.44] "That is what makes it a function."
        sync_to(self, sentences[16]["start"])
        two_to_one = Text("Two inputs can share one output: h(1) = h(3) = 15", font_size=26, weight=BOLD, color=CURVE)
        two_box = boxed(two_to_one, color=CURVE, pad=0.25).move_to(DOWN*2.6)
        self.play(Transform(key_box, two_box), run_time=1.0)
        
        # Beat 17: [53.74 - 59.38] "The set of allowed inputs is the domain, and the set of outputs the function actually produces is the range."
        sync_to(self, sentences[17]["start"])
        self.play(FadeOut(key_box), run_time=0.4)
        
        d_summary = Text("Domain: {0, 1, 2, 3, 4} s", font_size=26, weight=BOLD, color=POINT)
        r_summary = Text("Range: {0, 15, 20} m", font_size=26, weight=BOLD, color=GOOD)
        dr_group = VGroup(d_summary, r_summary).arrange(RIGHT, buff=0.8)
        dr_box = fit(boxed(dr_group, color=WHITE, pad=0.25)).move_to(DOWN*2.6)
        
        self.play(
            Indicate(domain_label, color=POINT),
            Indicate(range_label, color=GOOD),
            FadeIn(dr_box),
            run_time=1.5
        )
        
        sync_to(self, total_audio + 0.15)
        check_bounds(self)
