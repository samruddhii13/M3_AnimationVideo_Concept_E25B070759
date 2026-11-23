from manim import *
from helpers import BG, CURVE, POINT, GOOD, BAD, MAXC, fit, boxed, check_bounds, sync_to, configure_scene, load_timings

class Scene4Features(Scene):
    def construct(self):
        configure_scene(self)
        timings = load_timings("scene4")
        total_audio = timings.get("total_duration", 93.0)
        sentences = {s["beat_index"]: s for s in timings.get("sentences", [])}
        
        # Header
        header = Text("Key Features: Worked Analysis", font_size=40, weight=BOLD, color=WHITE)
        header.to_edge(UP, buff=0.45)
        self.add(header)
        
        # Left Half: Coordinate Axes
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 25, 5],
            x_length=5.2,
            y_length=4.2,
            axis_config={"color": LIGHT_GRAY, "include_numbers": True, "font_size": 20},
            tips=True
        ).move_to(np.array([-3.2, -0.6, 0]))
        
        x_lbl = Text("Time t (s)", font_size=20, color=LIGHT_GRAY).next_to(axes.x_axis.get_end(), DOWN, buff=0.2).shift(LEFT*0.5)
        y_lbl = Text("Height h (m)", font_size=20, color=LIGHT_GRAY).next_to(axes.y_axis.get_end(), UP, buff=0.2).shift(RIGHT*0.3)
        parabola = axes.plot(lambda t: 20*t - 5*t**2, x_range=[0, 4], color=CURVE, stroke_width=3.5)
        axes_group = VGroup(axes, x_lbl, y_lbl, parabola)
        
        # Beat 1: [0.00 - 2.93] "Now let's find the key features step by step."
        sync_to(self, sentences[1]["start"])
        self.play(FadeIn(axes_group), run_time=1.2)
        
        # Right Half Card Container Center
        card_center = np.array([3.4, -0.5, 0])
        
        # ========================================================
        # STEP 1: Intercepts (Beats 2-7)
        # ========================================================
        # Beat 2: [3.23 - 5.27] "First, the intercepts."
        sync_to(self, sentences[2]["start"])
        step1_title = Text("1. Intercepts: h(t) = 0", font_size=28, weight=BOLD, color=GOOD)
        step1_header = boxed(step1_title, color=GOOD, pad=0.2).move_to(card_center + UP*2.0)
        self.play(FadeIn(step1_header), run_time=0.8)
        
        # Beat 3: [5.57 - 10.03] "At tee equals zero, aitch is zero, so the graph starts at the origin."
        sync_to(self, sentences[3]["start"])
        calc1 = MathTex(r"h(0) = 20(0) - 5(0)^2 = 0", font_size=28, color=WHITE)
        calc1_note = Text("Starts at Origin: (0, 0)", font_size=22, color=GOOD)
        c1_group = VGroup(calc1, calc1_note).arrange(DOWN, buff=0.15).next_to(step1_header, DOWN, buff=0.25)
        
        dot_origin = Dot(point=axes.c2p(0, 0), radius=0.12, color=GOOD)
        lbl_origin = Text("(0, 0) Starts", font_size=20, color=GOOD).next_to(dot_origin, UP+RIGHT, buff=0.15)
        self.play(FadeIn(c1_group), FadeIn(dot_origin), FadeIn(lbl_origin), run_time=1.2)
        
        # Beat 4: [10.33 - 16.28] "To find when the ball lands, set aitch equal to zero: twenty tee minus five tee squared equals zero."
        sync_to(self, sentences[4]["start"])
        calc2 = MathTex(r"20t - 5t^2 = 0", font_size=30, color=WHITE).next_to(c1_group, DOWN, buff=0.25)
        self.play(FadeIn(calc2), run_time=1.0)
        
        # Beat 5: [16.58 - 20.90] "Factorising, five tee times, four minus tee, equals zero."
        sync_to(self, sentences[5]["start"])
        calc3 = MathTex(r"5t(4 - t) = 0", font_size=30, color=POINT).next_to(calc2, DOWN, buff=0.2)
        self.play(FadeIn(calc3), run_time=1.0)
        
        # Beat 6: [21.20 - 23.68] "So tee is zero or tee is four."
        sync_to(self, sentences[6]["start"])
        calc4 = MathTex(r"t = 0 \quad\text{or}\quad t = 4", font_size=30, color=GOOD).next_to(calc3, DOWN, buff=0.2)
        self.play(FadeIn(calc4), run_time=0.9)
        
        # Beat 7: [23.98 - 26.38] "The ball lands after four seconds."
        sync_to(self, sentences[7]["start"])
        dot_land = Dot(point=axes.c2p(4, 0), radius=0.12, color=GOOD)
        lbl_land = Text("(4, 0) Lands", font_size=20, color=GOOD).next_to(dot_land, UP+LEFT, buff=0.15)
        land_note = Text("Lands at 4 s: (4, 0)", font_size=22, weight=BOLD, color=GOOD).next_to(calc4, DOWN, buff=0.2)
        self.play(FadeIn(dot_land), FadeIn(lbl_land), FadeIn(land_note), run_time=1.0)
        
        step1_mobs = VGroup(step1_header, c1_group, calc2, calc3, calc4, land_note, dot_origin, lbl_origin, dot_land, lbl_land)
        
        # ========================================================
        # STEP 2: Maximum (Beats 8-12)
        # ========================================================
        # Beat 8: [26.68 - 28.93] "Second, the highest point."
        sync_to(self, sentences[8]["start"])
        self.play(FadeOut(step1_mobs), run_time=0.6)
        
        step2_title = Text("2. Maximum & Vertex", font_size=28, weight=BOLD, color=MAXC)
        step2_header = boxed(step2_title, color=MAXC, pad=0.2).move_to(card_center + UP*2.0)
        self.play(FadeIn(step2_header), run_time=0.8)
        
        # Beat 9: [29.23 - 33.91] "We can rewrite the rule as twenty minus five times, tee minus two, squared."
        sync_to(self, sentences[9]["start"])
        m_form = MathTex(r"h(t) = 20 - 5(t - 2)^2", font_size=32, color=MAXC).next_to(step2_header, DOWN, buff=0.25)
        check_expand = MathTex(r"= 20 - 5(t^2 - 4t + 4) = 20t - 5t^2", font_size=24, color=LIGHT_GRAY).next_to(m_form, DOWN, buff=0.15)
        self.play(FadeIn(m_form), FadeIn(check_expand), run_time=1.2)
        
        # Beat 10: [34.21 - 39.42] "The squared term is never negative, so the height is largest when it is zero, at tee equals two."
        sync_to(self, sentences[10]["start"])
        ineq = MathTex(r"(t - 2)^2 \ge 0 \implies -5(t - 2)^2 \le 0", font_size=28, color=POINT).next_to(check_expand, DOWN, buff=0.25)
        ineq_sub = Text("Largest when (t - 2) = 0 => t = 2 s", font_size=22, color=WHITE).next_to(ineq, DOWN, buff=0.15)
        self.play(FadeIn(ineq), FadeIn(ineq_sub), run_time=1.2)
        
        # Beat 11: [39.72 - 42.00] "There, aitch equals twenty."
        sync_to(self, sentences[11]["start"])
        m_val = MathTex(r"h(2) = 20 - 5(0)^2 = 20\text{ m}", font_size=30, color=GOOD).next_to(ineq_sub, DOWN, buff=0.2)
        self.play(FadeIn(m_val), run_time=0.9)
        
        # Beat 12: [42.30 - 45.68] "The maximum height is twenty metres, after two seconds."
        sync_to(self, sentences[12]["start"])
        dot_max = Dot(point=axes.c2p(2, 20), radius=0.12, color=MAXC)
        lbl_max = Text("Maximum: 20 m at t = 2 s", font_size=20, weight=BOLD, color=MAXC).next_to(dot_max, UP, buff=0.15)
        sym_line = DashedLine(start=axes.c2p(2, 0), end=axes.c2p(2, 22), color=MAXC, stroke_width=2.5)
        lbl_sym = Text("Axis of Symmetry: t = 2", font_size=18, color=MAXC).next_to(axes.c2p(2, 0), DOWN, buff=0.25)
        self.play(FadeIn(dot_max), FadeIn(lbl_max), Create(sym_line), FadeIn(lbl_sym), run_time=1.2)
        
        step2_mobs = VGroup(step2_header, m_form, check_expand, ineq, ineq_sub, m_val, dot_max, lbl_max, sym_line, lbl_sym)
        
        # ========================================================
        # STEP 3: Domain and Range (Beats 13-15)
        # ========================================================
        # Beat 13: [45.98 - 48.19] "Third, the domain and range."
        sync_to(self, sentences[13]["start"])
        self.play(FadeOut(step2_mobs), run_time=0.6)
        
        step3_title = Text("3. Domain & Range", font_size=28, weight=BOLD, color=WHITE)
        step3_header = boxed(step3_title, color=CURVE, pad=0.2).move_to(card_center + UP*2.0)
        self.play(FadeIn(step3_header), run_time=0.8)
        
        # Beat 14: [48.49 - 55.40] "The formula accepts any real number, but the ball only flies from zero to four seconds, so the domain here is zero to four."
        sync_to(self, sentences[14]["start"])
        dom_math = Text("Mathematical Domain: all real t", font_size=22, color=LIGHT_GRAY).next_to(step3_header, DOWN, buff=0.25)
        dom_phys = Text("Physical Domain: [0, 4] s", font_size=28, weight=BOLD, color=POINT).next_to(dom_math, DOWN, buff=0.15)
        dom_note = Text("(Flight period: throw to landing)", font_size=20, color=POINT).next_to(dom_phys, DOWN, buff=0.1)
        
        # Highlight on t-axis
        t_bar = Line(start=axes.c2p(0, 0), end=axes.c2p(4, 0), color=POINT, stroke_width=7)
        self.play(FadeIn(dom_math), FadeIn(dom_phys), FadeIn(dom_note), Create(t_bar), run_time=1.4)
        
        # Beat 15: [55.70 - 59.93] "The height stays between zero and twenty, so the range is zero to twenty."
        sync_to(self, sentences[15]["start"])
        range_phys = Text("Physical Range: [0, 20] m", font_size=28, weight=BOLD, color=GOOD).next_to(dom_note, DOWN, buff=0.3)
        range_note = Text("(Height from hand to peak)", font_size=20, color=GOOD).next_to(range_phys, DOWN, buff=0.1)
        
        # Highlight on h-axis
        h_bar = Line(start=axes.c2p(0, 0), end=axes.c2p(0, 20), color=GOOD, stroke_width=7)
        self.play(FadeIn(range_phys), FadeIn(range_note), Create(h_bar), run_time=1.3)
        
        step3_mobs = VGroup(step3_header, dom_math, dom_phys, dom_note, t_bar, range_phys, range_note, h_bar)
        
        # ========================================================
        # STEP 4: Behaviour & Rates of Change (Beats 16-25)
        # ========================================================
        # Beat 16: [60.23 - 62.34] "Finally, the behaviour."
        sync_to(self, sentences[16]["start"])
        self.play(FadeOut(step3_mobs), run_time=0.6)
        
        step4_title = Text("4. Behaviour & Rates", font_size=28, weight=BOLD, color=WHITE)
        step4_header = boxed(step4_title, color=POINT, pad=0.2).move_to(card_center + UP*2.0)
        self.play(FadeIn(step4_header), run_time=0.8)
        
        # Beat 17: [62.64 - 65.71] "From zero to two seconds the graph is increasing."
        sync_to(self, sentences[17]["start"])
        inc_curve = axes.plot(lambda t: 20*t - 5*t**2, x_range=[0, 2], color=GOOD, stroke_width=5.5)
        inc_lbl = Text("Increasing on [0, 2] s (Climbing)", font_size=24, weight=BOLD, color=GOOD).next_to(step4_header, DOWN, buff=0.35)
        self.play(Create(inc_curve), FadeIn(inc_lbl), run_time=1.1)
        
        # Beat 18: [66.01 - 68.36] "From two to four it is decreasing."
        sync_to(self, sentences[18]["start"])
        dec_curve = axes.plot(lambda t: 20*t - 5*t**2, x_range=[2, 4], color=BAD, stroke_width=5.5)
        dec_lbl = Text("Decreasing on [2, 4] s (Falling)", font_size=24, weight=BOLD, color=BAD).next_to(inc_lbl, DOWN, buff=0.25)
        self.play(Create(dec_curve), FadeIn(dec_lbl), run_time=1.0)
        
        # Beat 19: [68.66 - 72.67] "To measure how fast, look at the average change in height per second."
        sync_to(self, sentences[19]["start"])
        # Transition right side to Rate calculations
        self.play(FadeOut(inc_lbl), FadeOut(dec_lbl), run_time=0.4)
        rate_title = Text("Average Rate: Δh / Δt (m/s)", font_size=24, weight=BOLD, color=WHITE).next_to(step4_header, DOWN, buff=0.3)
        self.play(FadeIn(rate_title), run_time=0.8)
        
        # Beats 20-23: Secant segments and values
        # [0, 1]: 15 m/s
        sync_to(self, sentences[20]["start"])
        sec1 = Line(start=axes.c2p(0, 0), end=axes.c2p(1, 15), color=GOOD, stroke_width=3.5)
        r1_t = MathTex(r"[0, 1]\text{ s: } \frac{15 - 0}{1} = +15\text{ m/s}", font_size=24, color=GOOD).next_to(rate_title, DOWN, buff=0.2)
        self.play(Create(sec1), FadeIn(r1_t), run_time=0.8)
        
        # [1, 2]: 5 m/s
        sync_to(self, sentences[21]["start"])
        sec2 = Line(start=axes.c2p(1, 15), end=axes.c2p(2, 20), color=GOOD, stroke_width=3.5)
        r2_t = MathTex(r"[1, 2]\text{ s: } \frac{20 - 15}{1} = +5\text{ m/s}", font_size=24, color=GOOD).next_to(r1_t, DOWN, buff=0.18)
        self.play(Create(sec2), FadeIn(r2_t), run_time=0.8)
        
        # [2, 3]: -5 m/s
        sync_to(self, sentences[22]["start"])
        sec3 = Line(start=axes.c2p(2, 20), end=axes.c2p(3, 15), color=BAD, stroke_width=3.5)
        r3_t = MathTex(r"[2, 3]\text{ s: } \frac{15 - 20}{1} = -5\text{ m/s}", font_size=24, color=BAD).next_to(r2_t, DOWN, buff=0.18)
        self.play(Create(sec3), FadeIn(r3_t), run_time=0.8)
        
        # [3, 4]: -15 m/s
        sync_to(self, sentences[23]["start"])
        sec4 = Line(start=axes.c2p(3, 15), end=axes.c2p(4, 0), color=BAD, stroke_width=3.5)
        r4_t = MathTex(r"[3, 4]\text{ s: } \frac{0 - 15}{1} = -15\text{ m/s}", font_size=24, color=BAD).next_to(r3_t, DOWN, buff=0.18)
        self.play(Create(sec4), FadeIn(r4_t), run_time=0.8)
        
        # Beat 24: [84.06 - 87.20] "A negative value means the ball is moving downward."
        sync_to(self, sentences[24]["start"])
        neg_note = Text("Negative (< 0) = Falling Down", font_size=22, weight=BOLD, color=BAD).next_to(r4_t, DOWN, buff=0.22)
        self.play(FadeIn(neg_note), run_time=0.9)
        
        # Beat 25: [87.50 - 91.58] "The climb slows down, stops at the peak, and the fall speeds up."
        sync_to(self, sentences[25]["start"])
        summary_dyn = Text("Climb slows -> Stops -> Fall accelerates", font_size=20, color=POINT).next_to(neg_note, DOWN, buff=0.18)
        self.play(FadeIn(summary_dyn), run_time=1.1)
        
        sync_to(self, total_audio + 0.15)
        check_bounds(self)

