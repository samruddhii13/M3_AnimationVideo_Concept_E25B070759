"""
scene2_concept.py – Precise definition, physics rule test, and mapping diagram.
Total audio duration: 60.264 s.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from design import *

class Scene2Concept(Base):
    def construct(self):
        timings = load_scene_timings("scene2")
        total_audio = timings.get("total_duration", 60.264)

        hdr = header(2, "Function Definition and Rule", total=6)
        self.add(hdr)

        # ── Beat 0 & 1: (0.00s - 6.08s) Definition Card ─────────────────
        sync_to(self, 0.0)
        def_card = card(
            T("Mathematical Definition", 24, CURVE),
            T("A function gives each allowed input exactly ONE output.", 30, INK, bold=True),
            color=CURVE, gap=0.25, pad=0.35
        ).move_to(UP * 1.5)

        p_in  = pill("Input: time t (s)", CURVE, 26)
        p_arr = Arrow(LEFT*0.5, RIGHT*0.5, color=POINT, buff=0.1, stroke_width=3)
        p_out = pill("Output: height h(t) (m)", GOOD, 26)
        p_grp = VGroup(p_in, p_arr, p_out).arrange(RIGHT, buff=0.3).move_to(DOWN * 0.2)

        self.play(FadeIn(def_card), run_time=1.0)
        sync_to(self, 2.24)
        self.play(FadeIn(p_grp), run_time=1.0)

        # ── Beat 2 & 3: (6.38s - 12.90s) Inputs & Outputs explanation ──
        sync_to(self, 6.38)
        self.play(p_in.animate.scale(1.08).set_color(CURVE), run_time=0.6)
        self.play(p_in.animate.scale(1/1.08), run_time=0.4)
        sync_to(self, 9.59)
        self.play(p_out.animate.scale(1.08).set_color(GOOD), run_time=0.6)
        self.play(p_out.animate.scale(1/1.08), run_time=0.4)

        # ── Beat 4 & 5: (13.20s - 26.75s) Physics Rule & g assumption ───
        sync_to(self, 13.20)
        self.play(FadeOut(def_card), FadeOut(p_grp), run_time=0.6)

        rule_card = card(
            T("Physics Model (Vertical Projectile)", 24, CURVE),
            T("h(t) = 20t − 5t²", 36, INK, bold=True),
            T("= 5t(4 − t) = 20 − 5(t − 2)²", 26, MUTED),
            color=CURVE, gap=0.25, pad=0.35
        ).move_to(UP * 1.6)

        note_g = card(
            T("Assumption: g = 10 m/s², no air resistance (simplified from 9.8)", 22, MUTED),
            color=MUTED, pad=0.2
        ).move_to(DOWN * 0.1)

        self.play(FadeIn(rule_card), run_time=1.0)
        sync_to(self, 22.02)
        self.play(FadeIn(note_g), run_time=0.8)

        # ── Beat 6 & 7: (27.05s - 33.66s) Test rule with mini ruler ball ──
        sync_to(self, 27.05)
        self.play(FadeOut(note_g), run_time=0.4)
        self.play(rule_card.animate.scale(0.80).move_to(UP * 1.8), run_time=0.6)

        # Mini ruler on left
        ruler_mini = NumberLine(
            x_range=[0, 20, 5],
            length=3.5,
            rotation=PI/2,
            include_numbers=True,
            font_size=20,
            label_direction=LEFT,
            line_to_number_buff=0.25,
            color=MUTED
        ).move_to(LEFT * 4.2 + DOWN * 0.8)
        ruler_mini_lbl = T("Height (m)", 18, MUTED).next_to(ruler_mini, UP, buff=0.15)

        t_scrub = ValueTracker(0.0)
        ball_mini = always_redraw(
            lambda: make_ball(0.20).move_to(ruler_mini.n2p(h_of(t_scrub.get_value())))
        )

        test_calc = card(
            T("Test at t = 1 s:", 26, POINT, bold=True),
            T("h(1) = 20(1) − 5(1)²", 28, INK),
            T("     = 20 − 5 = 15 m", 30, GOOD, bold=True),
            color=POINT, gap=0.2, pad=0.3
        ).move_to(RIGHT * 1.4 + DOWN * 0.8)

        self.play(Create(ruler_mini), FadeIn(ruler_mini_lbl), FadeIn(ball_mini), run_time=0.8)
        sync_to(self, 29.22)
        self.play(
            FadeIn(test_calc),
            t_scrub.animate.set_value(1.0),
            run_time=2.2,
            rate_func=linear
        )

        # ── Beat 8: (33.96s) "Here is the mapping for five sample times." ──
        sync_to(self, 33.96)
        self.play(
            FadeOut(VGroup(rule_card, ruler_mini, ruler_mini_lbl, ball_mini, test_calc)),
            run_time=0.6
        )

        # Mapping Diagram Step 3
        # Headings: "Sample inputs t (s)" and "Outputs h(t) (m)"
        h_left  = T("Sample inputs t (s)", 26, CURVE, bold=True).move_to(LEFT * 2.8 + UP * 2.1)
        h_right = T("Outputs h(t) (m)", 26, GOOD, bold=True).move_to(RIGHT * 2.8 + UP * 2.1)

        # Two rounded column cards
        col_in_box  = RoundedRectangle(corner_radius=0.2, width=2.4, height=3.8, color=CURVE, stroke_width=2, fill_opacity=0.06).move_to(LEFT * 2.8 + DOWN * 0.1)
        col_out_box = RoundedRectangle(corner_radius=0.2, width=2.4, height=3.8, color=GOOD,  stroke_width=2, fill_opacity=0.06).move_to(RIGHT * 2.8 + DOWN * 0.1)

        # Inputs: 0, 1, 2, 3, 4 (y from 1.2 to -1.4, step 0.65)
        in_pts = {}
        in_mobs = []
        for i, val in enumerate([0, 1, 2, 3, 4]):
            y_pos = 1.2 - i * 0.65
            dot = Dot(LEFT * 1.8 + UP * y_pos, color=CURVE, radius=0.08)
            num = T(str(val), 26, INK).move_to(LEFT * 2.8 + UP * y_pos)
            in_pts[val] = dot
            in_mobs.extend([dot, num])

        # Outputs: 20, 15, 0 (y at 1.0, 0.0, -1.0)
        out_pts = {}
        out_mobs = []
        out_vals = [(20, 1.0), (15, 0.0), (0, -1.0)]
        for val, y_pos in out_vals:
            dot = Dot(RIGHT * 1.8 + UP * y_pos, color=GOOD, radius=0.08)
            num = T(str(val), 26, INK).move_to(RIGHT * 2.8 + UP * y_pos)
            out_pts[val] = dot
            out_mobs.extend([dot, num])

        diag_grp = VGroup(h_left, h_right, col_in_box, col_out_box, *in_mobs, *out_mobs)
        self.play(FadeIn(diag_grp), run_time=1.0)

        # ── Beats 9 to 13: (37.14s - 47.77s) Draw arrows one by one ─────
        # Arrow function: Arrow ending next to dot
        def make_mapping_arrow(p1, p2, col=POINT):
            return Arrow(p1.get_center(), p2.get_center(), buff=0.12, stroke_width=2.5, tip_length=0.18, color=col)

        # Beat 9: 0 -> 0
        sync_to(self, 37.14)
        arr_0 = make_mapping_arrow(in_pts[0], out_pts[0])
        self.play(Create(arr_0), run_time=0.6)

        # Beat 10: 1 -> 15
        sync_to(self, 39.34)
        arr_1 = make_mapping_arrow(in_pts[1], out_pts[15])
        self.play(Create(arr_1), run_time=0.6)

        # Beat 11: 2 -> 20
        sync_to(self, 41.53)
        arr_2 = make_mapping_arrow(in_pts[2], out_pts[20])
        self.play(Create(arr_2), run_time=0.6)

        # Beat 12: 3 -> 15 (converges on 15!)
        sync_to(self, 43.70)
        arr_3 = make_mapping_arrow(in_pts[3], out_pts[15], col=POINT)
        self.play(Create(arr_3), run_time=0.6)

        # Beat 13: 4 -> 0 (converges on 0!)
        sync_to(self, 45.88)
        arr_4 = make_mapping_arrow(in_pts[4], out_pts[0], col=POINT)
        self.play(Create(arr_4), run_time=0.6)

        # ── Beat 14 & 15: (48.07s - 54.32s) Two inputs -> one output allowed ──
        sync_to(self, 48.07)
        allowed_pill = pill("Two inputs, one output: ALLOWED ✓", GOOD, 24).move_to(DOWN * 2.3)
        self.play(FadeIn(allowed_pill), run_time=0.8)

        # ── Beat 16: (54.62s - 60.26s) Domain & Range definitions ────────
        sync_to(self, 54.62)
        self.play(FadeOut(allowed_pill), run_time=0.3)
        dom_lbl = T("Domain = allowed inputs", 24, CURVE).move_to(LEFT * 2.8 + DOWN * 2.3)
        rng_lbl = T("Range = outputs actually produced", 24, GOOD).move_to(RIGHT * 2.8 + DOWN * 2.3)
        self.play(FadeIn(dom_lbl), FadeIn(rng_lbl), run_time=1.0)

        # Hold until audio completes
        sync_to(self, total_audio)
        check_layout(self)
