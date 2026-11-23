"""
scene1_hook.py – Hook: cricket ball throw & function machine.
Total audio duration: 31.056 s.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from design import *

class Scene1Hook(Base):
    def construct(self):
        timings = load_scene_timings("scene1")
        total_audio = timings.get("total_duration", 31.056)

        hdr = header(1, "The Cricket Ball Problem", total=6)
        self.add(hdr)

        # ── Setup Ruler on Left ──────────────────────────────────────────
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
        ruler.move_to([-4.6, -0.35, 0])
        ruler_lbl = T("Ruler (m)", 22, MUTED).next_to(ruler, UP, buff=0.2)
        note_g = T("v₀ = 20 m/s, g = 10 m/s²", 18, MUTED).next_to(ruler, DOWN, buff=0.25)

        # Intro Card on Right
        intro_card = card(
            T("Real-Life Example", 24, CURVE),
            T("Cricket Ball Thrown Upward", 32, INK, bold=True),
            T("Can we predict its height at any time?", 26, MUTED),
            color=CURVE, gap=0.25, pad=0.35
        ).move_to(RIGHT * 1.8 + UP * 0.3)

        t_val = ValueTracker(0.0)
        ball = always_redraw(
            lambda: make_ball(0.25).move_to(ruler.n2p(h_of(t_val.get_value())))
        )

        # ── Beat 1: (0.00s) "Imagine you throw a cricket ball straight up into the air." ──
        sync_to(self, 0.0)
        self.play(Create(ruler), FadeIn(ruler_lbl), FadeIn(note_g), FadeIn(intro_card), run_time=1.2)
        self.play(FadeIn(ball), run_time=0.6)

        # Dotted trail & readout card
        def readout_card():
            tv = t_val.get_value()
            hv = h_of(tv)
            t_txt = T(f"t = {tv:.1f} s", 26, POINT)
            h_txt = T(f"h = {hv:.1f} m", 26, GOOD)
            c = card(t_txt, h_txt, direction=RIGHT, gap=0.3, pad=0.22, color=POINT)
            return c.move_to(RIGHT * 1.8 + UP * 2.3)

        readout = always_redraw(readout_card)
        trail = TracedPath(lambda: ruler.n2p(h_of(t_val.get_value())), stroke_color=POINT, stroke_width=2.5, stroke_opacity=0.6)

        # ── Beat 2: (3.64s) "How high is it after one second?" ───────────
        sync_to(self, 3.64)
        self.play(FadeOut(intro_card), run_time=0.4)
        self.add(trail, readout)
        q1 = pill("1 s:  How high? (15 m)", POINT, 24).move_to(RIGHT * 1.8 + UP * 1.0)
        self.play(t_val.animate.set_value(1.0), FadeIn(q1), run_time=1.8, rate_func=linear)

        # ── Beat 3: (6.24s) "After two seconds?" ─────────────────────────
        sync_to(self, 6.24)
        q2 = pill("2 s:  Maximum height? (20 m)", MAXC, 24).move_to(RIGHT * 1.8 + UP * 0.2)
        self.play(t_val.animate.set_value(2.0), FadeIn(q2), run_time=1.6, rate_func=linear)

        # ── Beat 4: (8.41s) "And when does it come back down?" ───────────
        sync_to(self, 8.41)
        q3 = pill("4 s:  When does it land? (0 m)", BAD, 24).move_to(RIGHT * 1.8 + DOWN * 0.6)
        self.play(t_val.animate.set_value(4.0), FadeIn(q3), run_time=1.8, rate_func=linear)
        dust = Circle(radius=0.35, color=MUTED, stroke_width=2).move_to(ruler.n2p(0))
        self.play(dust.animate.scale(1.8).set_opacity(0), run_time=0.4)

        # ── Beat 5: (10.82s) "These questions have exact answers... a function." ──
        sync_to(self, 10.82)
        self.play(
            FadeOut(VGroup(ruler, ruler_lbl, note_g, ball, trail, readout, q1, q2, q3)),
            run_time=0.8
        )

        in_pill  = pill("t = 1 s", CURVE, 26)
        rule_box = card(T("Function Rule", 22, MUTED),
                        T("h(t) = 20t − 5t²", 34, INK, bold=True),
                        color=CURVE, pad=0.3)
        out_pill = pill("15 m", GOOD, 26)
        arr1     = Arrow(LEFT*0.6, RIGHT*0.6, color=POINT, buff=0.1, stroke_width=3)
        arr2     = Arrow(LEFT*0.6, RIGHT*0.6, color=POINT, buff=0.1, stroke_width=3)

        machine = VGroup(in_pill, arr1, rule_box, arr2, out_pill).arrange(RIGHT, buff=0.25).move_to(UP * 0.5)
        sub_text = T("Input: time  →  Output: height", 28, POINT).move_to(DOWN * 1.1)

        self.play(FadeIn(rule_box), run_time=0.8)
        self.play(FadeIn(in_pill), Create(arr1), run_time=0.8)
        self.play(Create(arr2), FadeIn(out_pill), FadeIn(sub_text), run_time=0.9)

        # ── Beat 6: (15.80s) "A function is a rule that takes an input... one output..." ──
        sync_to(self, 15.80)
        defn_pill = pill("Rule: Each input gives EXACTLY ONE output", GOOD, 24).move_to(DOWN * 2.1)
        self.play(FadeIn(defn_pill), run_time=1.0)
        self.wait(1.5)

        # ── Beat 7: (22.25s) "In this video, we will use this ball to understand three things..." ──
        sync_to(self, 22.25)
        self.play(FadeOut(VGroup(machine, sub_text, defn_pill)), run_time=0.6)

        g1 = card(T("1", 24, BG, True), T("Input to Output: Rule and Mapping Table", 26, INK),
                  direction=RIGHT, gap=0.3, pad=0.22, color=CURVE)
        g2 = card(T("2", 24, BG, True), T("Plotting and Reading the Parabola Graph", 26, INK),
                  direction=RIGHT, gap=0.3, pad=0.22, color=GOOD)
        g3 = card(T("3", 24, BG, True), T("Key Features: Intercepts, Max, Behaviour", 26, INK),
                  direction=RIGHT, gap=0.3, pad=0.22, color=MAXC)
        goals = VGroup(g1, g2, g3).arrange(DOWN, buff=0.32).move_to(CONTENT_CENTER)

        self.play(LaggedStart(*[FadeIn(g, shift=RIGHT*0.3) for g in goals], lag_ratio=0.4), run_time=2.2)

        # Hold until total audio length
        sync_to(self, total_audio)
        check_layout(self)
