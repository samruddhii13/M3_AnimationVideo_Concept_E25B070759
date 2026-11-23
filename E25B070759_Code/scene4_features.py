"""
scene4_features.py – Four key features: intercepts, max, domain/range, behaviour.
Total audio duration: 93.0 s.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from design import *

class Scene4Features(Base):
    def construct(self):
        timings = load_scene_timings("scene4")
        total_audio = timings.get("total_duration", 93.0)

        hdr = header(4, "Key Features of the Function", total=6)
        self.add(hdr)

        # ── Beat 0: (0.00s) Permanent Graph on the Left ──────────────────
        sync_to(self, 0.0)
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 25, 5],
            x_length=5.2,
            y_length=4.2,
            axis_config={"color": MUTED, "stroke_width": 2, "include_tip": False, "font_size": 22},
            x_axis_config={"numbers_to_include": [0, 1, 2, 3, 4, 5]},
            y_axis_config={"numbers_to_include": [0, 5, 10, 15, 20, 25]}
        ).move_to(LEFT * 3.0 + DOWN * 0.1)

        xl = T("Time t (s)", 22, MUTED).next_to(axes.x_axis, DOWN, buff=0.18)
        yl = T("Height h (m)", 22, MUTED).next_to(axes.y_axis, UP, buff=0.15)

        curve = axes.plot(lambda t: 20*t - 5*t**2, x_range=[0, 4, 0.03], stroke_color=CURVE, stroke_width=4.5)
        halo  = curve.copy().set_stroke(CURVE, width=12, opacity=0.18)

        t_mark = ValueTracker(0.0)
        ball = always_redraw(
            lambda: make_ball(0.20).move_to(axes.c2p(t_mark.get_value(), h_of(t_mark.get_value())))
        )

        self.play(Create(axes), FadeIn(xl), FadeIn(yl), Create(halo), Create(curve), FadeIn(ball), run_time=1.8)

        # =====================================================================
        # FEATURE 1: INTERCEPTS (Beats 1 to 6: 3.23s - 26.38s)
        # =====================================================================
        sync_to(self, 3.23)
        card1_chip = T("1", 24, BG, True)
        card1_hdr  = VGroup(
            RoundedRectangle(corner_radius=0.14, width=0.6, height=0.5, fill_color=GOOD, fill_opacity=1, stroke_width=0),
            card1_chip
        )
        card1_chip.move_to(card1_hdr[0])
        card1_title = VGroup(card1_hdr, T("Intercepts", 28, GOOD, bold=True)).arrange(RIGHT, buff=0.25)

        c1_step1 = T("t = 0 → h(0) = 0 m (origin)", 24, INK)
        c1_step2 = T("Set h(t) = 0:  20t − 5t² = 0", 24, INK)
        c1_step3 = T("Factor: 5t(4 − t) = 0", 24, INK)
        c1_step4 = T("Roots: t = 0  or  t = 4 s", 26, GOOD, bold=True)

        card1 = card(card1_title, c1_step1, c1_step2, c1_step3, c1_step4, color=GOOD, gap=0.2, pad=0.3).move_to(RIGHT * 3.1 + UP * 0.4)

        d_t0 = Dot(axes.c2p(0, 0), color=GOOD, radius=0.13)
        p_t0 = pill("starts at 0", GOOD, 18).next_to(d_t0, UP + LEFT*0.2, buff=0.12)
        d_t4 = Dot(axes.c2p(4, 0), color=GOOD, radius=0.13)
        p_t4 = pill("lands at 4 s", GOOD, 18).next_to(d_t4, UP + RIGHT*0.2, buff=0.12)

        self.play(FadeIn(card1_title), run_time=0.6)
        sync_to(self, 5.57)
        self.play(FadeIn(c1_step1), FadeIn(d_t0), FadeIn(p_t0), run_time=0.8)

        sync_to(self, 10.33)
        self.play(FadeIn(c1_step2), run_time=0.8)

        sync_to(self, 16.58)
        self.play(FadeIn(c1_step3), run_time=0.8)

        sync_to(self, 21.20)
        self.play(FadeIn(c1_step4), run_time=0.6)

        sync_to(self, 23.98)
        self.play(
            t_mark.animate.set_value(4.0),
            FadeIn(d_t4), FadeIn(p_t4),
            run_time=2.0, rate_func=linear
        )
        self.wait(0.5)

        # =====================================================================
        # FEATURE 2: MAXIMUM (Beats 7 to 11: 26.68s - 45.68s)
        # =====================================================================
        sync_to(self, 26.68)
        self.play(FadeOut(VGroup(card1, p_t0, p_t4)), run_time=0.5)

        card2_chip = T("2", 24, BG, True)
        card2_hdr  = VGroup(
            RoundedRectangle(corner_radius=0.14, width=0.6, height=0.5, fill_color=MAXC, fill_opacity=1, stroke_width=0),
            card2_chip
        )
        card2_chip.move_to(card2_hdr[0])
        card2_title = VGroup(card2_hdr, T("Highest Point (Maximum)", 26, MAXC, bold=True)).arrange(RIGHT, buff=0.25)

        c2_step1 = T("Vertex Form:", 22, MUTED)
        c2_step2 = T("h(t) = 20 − 5(t − 2)²", 28, INK, bold=True)
        c2_step3 = T("Since (t − 2)² ≥ 0, h ≤ 20", 24, INK)
        c2_step4 = T("Max height = 20 m at t = 2 s", 26, MAXC, bold=True)

        card2 = card(card2_title, c2_step1, c2_step2, c2_step3, c2_step4, color=MAXC, gap=0.2, pad=0.3).move_to(RIGHT * 3.1 + UP * 0.4)

        d_max = Dot(axes.c2p(2, 20), color=MAXC, radius=0.15)
        p_max = pill("maximum: 20 m at t = 2 s", MAXC, 20).next_to(d_max, UP, buff=0.18)
        sym_axis = DashedLine(axes.c2p(2, 0), axes.c2p(2, 21), color=MAXC, stroke_width=2.5, dash_length=0.14)

        self.play(FadeIn(card2_title), run_time=0.6)
        sync_to(self, 29.23)
        self.play(FadeIn(c2_step1), FadeIn(c2_step2), run_time=0.8)

        sync_to(self, 34.21)
        self.play(FadeIn(c2_step3), run_time=0.8)

        sync_to(self, 39.72)
        self.play(FadeIn(c2_step4), run_time=0.6)

        sync_to(self, 42.30)
        self.play(
            t_mark.animate.set_value(2.0),
            FadeIn(d_max), Create(sym_axis), FadeIn(p_max),
            run_time=2.0
        )
        self.wait(1.0)

        # =====================================================================
        # FEATURE 3: DOMAIN & RANGE (Beats 12 to 14: 45.98s - 59.93s)
        # =====================================================================
        sync_to(self, 45.98)
        self.play(FadeOut(VGroup(card2, d_max, p_max, sym_axis)), run_time=0.5)

        card3_chip = T("3", 24, BG, True)
        card3_hdr  = VGroup(
            RoundedRectangle(corner_radius=0.14, width=0.6, height=0.5, fill_color=CURVE, fill_opacity=1, stroke_width=0),
            card3_chip
        )
        card3_chip.move_to(card3_hdr[0])
        card3_title = VGroup(card3_hdr, T("Domain and Range", 26, CURVE, bold=True)).arrange(RIGHT, buff=0.25)

        c3_note = T("Formula accepts any real t;", 22, MUTED)
        c3_note2 = T("Ball only flies from 0 to 4 s:", 22, MUTED)
        c3_dom = pill("Domain:  [0, 4] seconds", CURVE, 24)
        c3_rng = pill("Range:  [0, 20] metres", GOOD, 24)

        card3 = card(card3_title, c3_note, c3_note2, c3_dom, c3_rng, color=CURVE, gap=0.2, pad=0.3).move_to(RIGHT * 3.1 + UP * 0.4)

        # Highlighted bars on axes
        dom_bar = Line(axes.c2p(0, 0), axes.c2p(4, 0), color=CURVE, stroke_width=8, stroke_opacity=0.85)
        rng_bar = Line(axes.c2p(0, 0), axes.c2p(0, 20), color=GOOD,  stroke_width=8, stroke_opacity=0.85)

        self.play(FadeIn(card3_title), run_time=0.6)
        sync_to(self, 48.49)
        self.play(FadeIn(c3_note), FadeIn(c3_note2), FadeIn(c3_dom), Create(dom_bar), run_time=1.2)

        sync_to(self, 55.70)
        self.play(FadeIn(c3_rng), Create(rng_bar), run_time=1.0)
        self.wait(1.5)

        # =====================================================================
        # FEATURE 4: BEHAVIOUR & AVERAGE RATES (Beats 15 to 24: 60.23s - 93.0s)
        # =====================================================================
        sync_to(self, 60.23)
        self.play(FadeOut(VGroup(card3, dom_bar, rng_bar)), run_time=0.5)

        card4_chip = T("4", 24, BG, True)
        card4_hdr  = VGroup(
            RoundedRectangle(corner_radius=0.14, width=0.6, height=0.5, fill_color=POINT, fill_opacity=1, stroke_width=0),
            card4_chip
        )
        card4_chip.move_to(card4_hdr[0])
        card4_title = VGroup(card4_hdr, T("Behaviour & Rates", 26, POINT, bold=True)).arrange(RIGHT, buff=0.25)

        # Colored curve segments
        inc_seg = axes.plot(lambda t: 20*t - 5*t**2, x_range=[0, 2, 0.03], stroke_color=GOOD, stroke_width=6)
        dec_seg = axes.plot(lambda t: 20*t - 5*t**2, x_range=[2, 4, 0.03], stroke_color=BAD,  stroke_width=6)

        p_inc = pill("↑ Increasing: [0, 2] s", GOOD, 22)
        p_dec = pill("↓ Decreasing: [2, 4] s", BAD,  22)
        bh_row = VGroup(p_inc, p_dec).arrange(RIGHT, buff=0.2)

        chip1 = pill("[0, 1] s:  +15 m/s", GOOD, 20)
        chip2 = pill("[1, 2] s:  +5 m/s",  GOOD, 20)
        chip3 = pill("[2, 3] s:  −5 m/s",  BAD,  20)
        chip4 = pill("[3, 4] s:  −15 m/s", BAD,  20)
        chips_grid = VGroup(
            VGroup(chip1, chip2).arrange(RIGHT, buff=0.25),
            VGroup(chip3, chip4).arrange(RIGHT, buff=0.25)
        ).arrange(DOWN, buff=0.18)

        note_neg = T("negative = moving downward", 20, MUTED)

        card4 = card(card4_title, bh_row, chips_grid, note_neg, color=POINT, gap=0.2, pad=0.25).move_to(RIGHT * 3.1 + UP * 0.4)

        self.play(FadeIn(card4_title), run_time=0.5)
        sync_to(self, 62.64)
        self.play(Create(inc_seg), FadeIn(p_inc), run_time=1.0)

        sync_to(self, 66.01)
        self.play(Create(dec_seg), FadeIn(p_dec), run_time=1.0)

        sync_to(self, 72.97)
        self.play(FadeIn(chip1), run_time=0.5)

        sync_to(self, 75.74)
        self.play(FadeIn(chip2), run_time=0.5)

        sync_to(self, 78.18)
        self.play(FadeIn(chip3), run_time=0.5)

        sync_to(self, 81.02)
        self.play(FadeIn(chip4), run_time=0.5)

        sync_to(self, 84.06)
        self.play(FadeIn(note_neg), run_time=0.8)

        sync_to(self, 87.50)
        # Scrub ball along whole trajectory
        t_mark.set_value(0.0)
        self.play(t_mark.animate.set_value(4.0), run_time=3.5, rate_func=linear)

        # Hold until total audio length
        sync_to(self, total_audio)
        check_layout(self)
