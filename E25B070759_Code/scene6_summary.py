"""Scene 6 – Summary & Closing.
Template A: sequential takeaway cards, then closing frame.
"""
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from design import *

AUDIO_DIR = os.path.join(os.path.dirname(__file__), "..", "Audio")

def _load_scene_timings(scene_key):
    p = os.path.join(AUDIO_DIR, "timings.json")
    if not os.path.exists(p):
        return [], 0.0
    with open(p) as f:
        d = json.load(f)
    sc = d.get(scene_key, {})
    return sc.get("sentences", []), sc.get("total_duration", 0.0)

class Scene6Summary(Base):
    def construct(self):
        sents, total_dur = _load_scene_timings("scene6")

        hdr = header(6, "Summary", total=6)
        self.add(hdr)

        # ── Takeaway 1 ────────────────────────────────────────────────────────
        sync_to(self, sents[1]["start"])
        c1 = card(
            T("A function maps each input to exactly one output.", 32, INK),
            color=CURVE, pad=0.42
        )
        place(c1, region_h=1.4, center=CONTENT_CENTER + UP * 1.4)
        self.play(FadeIn(c1), run_time=0.8)

        # ── Takeaway 2 ────────────────────────────────────────────────────────
        sync_to(self, sents[2]["start"])
        c2 = card(
            VGroup(
                T("Read the graph:", 32, INK, bold=True),
                T("intercepts, maximum, domain, range,", 30, INK),
                T("increasing [0,2]  ·  decreasing [2,4]", 30, MUTED),
            ).arrange(DOWN, buff=0.2),
            color=GOOD, pad=0.42
        )
        place(c2, region_h=2.2, center=CONTENT_CENTER + DOWN * 0.1)
        self.play(FadeIn(c2), run_time=0.8)

        # ── Takeaway 3 ────────────────────────────────────────────────────────
        sync_to(self, sents[3]["start"])
        c3 = card(
            T("Vertical Line Test confirms a graph is a function.", 32, INK),
            color=MAXC, pad=0.42
        )
        place(c3, region_h=1.4, center=CONTENT_CENTER + DOWN * 1.5)
        if c3.get_bottom()[1] < -config.frame_height/2 + 1.2:
            c3.shift(UP * (-config.frame_height/2 + 1.2 - c3.get_bottom()[1]))
        self.play(FadeIn(c3), run_time=0.8)

        # ── Closing frame ─────────────────────────────────────────────────────
        sync_to(self, sents[4]["start"])
        self.play(FadeOut(c1), FadeOut(c2), FadeOut(c3), run_time=0.4)

        closing_rows = VGroup(
            T("From Input to Output", 36, INK, bold=True),
            T("Reading the Graph of a Function", 30, CURVE),
            Line(LEFT*5, RIGHT*5, stroke_width=1.2, color=MUTED).set_opacity(0.5),
            VGroup(
                T("Samruddhi Meshram  ·  E25B070759", 28, MUTED),
                T("Linear Algebra and Calculus (M3)", 28, MUTED),
            ).arrange(DOWN, buff=0.14),
            Line(LEFT*4, RIGHT*4, stroke_width=1.0, color=MUTED).set_opacity(0.4),
            T("References: course textbook and class notes", 24, MUTED),
            T("Audio: edge-tts · en-IN-NeerjaNeural, +32% rate", 22, MUTED),
            T("Animations: Manim Community Edition", 22, MUTED),
            T("Produced with AI assistance. All maths verified by student.", 20, MUTED),
        ).arrange(DOWN, buff=0.24)
        closing_box = card(closing_rows, color=CURVE, pad=0.5)
        place(closing_box)
        self.play(FadeIn(closing_box), run_time=0.8)

        sync_to(self, total_dur + 0.15)
        check_layout(self)
