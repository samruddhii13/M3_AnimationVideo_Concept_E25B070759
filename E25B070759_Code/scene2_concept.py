"""Scene 2 – Concept & Mapping.
Template A: centred stage throughout.
Beat 8 narration: "Here is the mapping for five sample times."
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

class Scene2Concept(Base):
    def construct(self):
        sents, total_dur = _load_scene_timings("scene2")

        hdr = header(2, "Concept & Mapping")
        self.add(hdr)

        # ── Beats 0-1: definition ────────────────────────────────────────────
        sync_to(self, sents[0]["start"])
        defn = VGroup(
            T("A function assigns to each allowed input", 32, INK),
            T("exactly one output.", 32, CURVE, bold=True),
        ).arrange(DOWN, buff=0.22)
        defn_box = card(defn, color=CURVE, pad=0.42)
        place(defn_box, center=CONTENT_CENTER + UP * 0.7)
        self.play(FadeIn(defn_box), run_time=0.8)

        # ── Beats 2-3: input & output ────────────────────────────────────────
        sync_to(self, sents[2]["start"])
        io = VGroup(
            VGroup(T("Input:", 30, MUTED),
                   T("time  t  (seconds)", 32, CURVE, bold=True)).arrange(RIGHT, buff=0.3),
            VGroup(T("Output:", 30, MUTED),
                   T("h(t) = height  (metres)", 32, GOOD, bold=True)).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        io_box = card(io, color=GOOD, pad=0.38)
        place(io_box, center=CONTENT_CENTER + DOWN * 1.1)
        self.play(FadeIn(io_box), run_time=0.8)

        # ── Beats 4-5: rule + gravity note ───────────────────────────────────
        sync_to(self, sents[4]["start"])
        self.play(FadeOut(defn_box), FadeOut(io_box), run_time=0.4)

        rule = MathTex(r"h(t)=20t-5t^2", font_size=52, color=POINT)
        note = T("(gravity taken as 10 m/s² for simplicity)", 26, MUTED)
        rule_box = card(rule, note, color=POINT, gap=0.25, pad=0.42)
        place(rule_box, center=CONTENT_CENTER + UP * 0.5)
        self.play(FadeIn(rule_box), run_time=0.8)

        # ── Beats 6-7: worked calculation ────────────────────────────────────
        sync_to(self, sents[6]["start"])
        calc = VGroup(
            T("Test: h(1) = 20(1) − 5(1)² = 20 − 5 = 15 m", 32, INK),
        )
        calc_box = card(calc, color=GOOD, pad=0.38)
        place(calc_box, center=CONTENT_CENTER + DOWN * 1.1)
        self.play(FadeIn(calc_box), run_time=0.8)

        # ── Beat 8: mapping diagram ───────────────────────────────────────────
        # narration: "Here is the mapping for five sample times."
        sync_to(self, sents[8]["start"])
        self.play(FadeOut(rule_box), FadeOut(calc_box), run_time=0.4)

        hd_in  = T("Sample inputs t (s)", 28, CURVE, bold=True)
        hd_out = T("Outputs h(t) (m)",    28, GOOD,  bold=True)

        pairs = [(0,0),(1,15),(2,20),(3,15),(4,0)]
        in_pills  = VGroup(*[pill(str(t), CURVE, 28) for t,_ in pairs]).arrange(DOWN, buff=0.22)
        out_pills = VGroup(*[pill(str(hv), GOOD,  28) for _,hv in pairs]).arrange(DOWN, buff=0.22)

        col_in  = VGroup(hd_in,  in_pills ).arrange(DOWN, buff=0.28)
        col_out = VGroup(hd_out, out_pills).arrange(DOWN, buff=0.28)
        mapping = VGroup(col_in, col_out).arrange(RIGHT, buff=2.6)

        mapping_box = card(mapping, color=CURVE, pad=0.42)
        place(mapping_box, region_h=4.2, center=CONTENT_CENTER + UP * 0.3)
        self.play(FadeIn(mapping_box), run_time=0.8)

        # ── Beats 9-13: arrows animate one by one ────────────────────────────
        arrows = []
        for i, (ip, op) in enumerate(zip(in_pills, out_pills)):
            sync_to(self, sents[9+i]["start"])
            arr = Arrow(ip.get_right(), op.get_left(), buff=0.12,
                        stroke_width=2.5, tip_length=0.16, color=MUTED)
            self.play(GrowArrow(arr), run_time=0.4)
            arrows.append(arr)

        # ── Beat 14: "every input, exactly one arrow" ─────────────────────────
        sync_to(self, sents[14]["start"])
        highlight = T("Every input → exactly one output", 32, POINT, bold=True)
        highlight.next_to(mapping_box, DOWN, buff=0.42)
        if highlight.get_bottom()[1] < -config.frame_height/2 + 1.2:
            highlight.shift(UP * 0.4)
        if highlight.width > CONTENT_W: highlight.scale_to_fit_width(CONTENT_W)
        self.play(FadeIn(highlight), run_time=0.8)

        # ── Beat 16: Domain & Range (text, no intervals here) ────────────────
        sync_to(self, sents[16]["start"])
        self.play(FadeOut(VGroup(*arrows)), FadeOut(highlight), FadeOut(mapping_box), run_time=0.4)

        dr = VGroup(
            T("Domain = the set of allowed inputs", 32, CURVE),
            T("Range  = the outputs actually produced", 32, GOOD),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        dr_box = card(dr, color=CURVE, pad=0.42)
        place(dr_box)
        self.play(FadeIn(dr_box), run_time=0.8)

        sync_to(self, total_dur + 0.15)
        check_layout(self)
