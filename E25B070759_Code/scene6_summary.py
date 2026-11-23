"""
scene6_summary.py – Three takeaway cards and final credits frame.
Total audio duration: 27.456 s.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from design import *

class Scene6Summary(Base):
    def construct(self):
        timings = load_scene_timings("scene6")
        total_audio = timings.get("total_duration", 27.456)

        hdr = header(6, "Summary and Takeaways", total=6)
        self.add(hdr)

        # ── Three Takeaway Cards ──────────────────────────────────────────
        def make_takeaway_card(num_str, title_str, line1_str, line2_str, col):
            num_chip = T(num_str, 24, BG, True)
            chip_bg  = RoundedRectangle(corner_radius=0.14, width=0.6, height=0.5, fill_color=col, fill_opacity=1, stroke_width=0)
            num_chip.move_to(chip_bg)
            chip = VGroup(chip_bg, num_chip)

            ball_icon = make_ball(0.18)
            hdr_row   = VGroup(chip, ball_icon).arrange(RIGHT, buff=0.25)
            t_head    = T(title_str, 24, col, bold=True)
            t_body    = VGroup(T(line1_str, 22, INK), T(line2_str, 22, INK)).arrange(DOWN, buff=0.12)
            c = card(hdr_row, t_head, t_body, color=col, gap=0.22, pad=0.3)
            return c

        c1 = make_takeaway_card("1", "Function Rule", "Each input has", "exactly one output", CURVE)
        c2 = make_takeaway_card("2", "The Graph", "Each graph point is", "an input-output pair", GOOD)
        c3 = make_takeaway_card("3", "Key Features", "Features tell the", "real-life story", MAXC)

        cards = VGroup(c1, c2, c3).arrange(RIGHT, buff=0.32).move_to(CONTENT_CENTER + UP * 0.2)

        # ── Beat 0 & 1: (0.00s - 8.48s) Card 1 ───────────────────────────
        sync_to(self, 0.0)
        sync_to(self, 2.48)
        self.play(FadeIn(c1, shift=UP*0.3), run_time=1.2)

        # ── Beat 2: (8.78s - 14.54s) Card 2 ──────────────────────────────
        sync_to(self, 8.78)
        self.play(FadeIn(c2, shift=UP*0.3), run_time=1.2)

        # ── Beat 3: (14.84s - 21.56s) Card 3 ──────────────────────────────
        sync_to(self, 14.84)
        self.play(FadeIn(c3, shift=UP*0.3), run_time=1.2)
        self.wait(1.5)

        # ── Beat 4 & 5: (21.86s - 27.46s) Closing Frame ──────────────────
        sync_to(self, 21.86)
        self.play(FadeOut(cards), FadeOut(hdr), run_time=0.6)

        headline = T("What goes in? What comes out? What does each feature mean?", 28, POINT, bold=True)
        name_id  = T("Samruddhi Meshram | E25B070759", 26, INK, bold=True)
        course   = T("Linear Algebra and Calculus (M3)", 22, CURVE)
        div_line = Line(LEFT * 4.8, RIGHT * 4.8, color=CURVE, stroke_width=1.5).set_opacity(0.7)

        c_ref    = T("References: course textbook and class notes", 20, INK)
        c_mus    = T("Music: No background music", 20, INK)
        c_ai     = T("AI disclosure: code, script and narration voice created with AI tools.", 18, MUTED)
        c_ai2    = T("Maths verified by the student. Details in README.md.", 18, MUTED)

        credits_grp = VGroup(c_ref, c_mus, c_ai, c_ai2).arrange(DOWN, buff=0.14, aligned_edge=LEFT)

        closing_vgroup = VGroup(
            headline,
            name_id,
            course,
            div_line,
            credits_grp
        ).arrange(DOWN, buff=0.22).move_to(CONTENT_CENTER)

        # Entry order: headline, name/course, line, credits one by one (0.4s each)
        self.play(FadeIn(headline, shift=UP*0.2), run_time=0.6)
        self.play(FadeIn(name_id), FadeIn(course), run_time=0.6)
        self.play(Create(div_line), run_time=0.4)
        self.play(FadeIn(c_ref), run_time=0.4)
        self.play(FadeIn(c_mus), run_time=0.4)
        self.play(FadeIn(c_ai), FadeIn(c_ai2), run_time=0.5)

        # Hold until audio completes + 0.5s margin
        sync_to(self, total_audio + 0.5)
        check_layout(self)
