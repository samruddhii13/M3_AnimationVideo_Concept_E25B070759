"""Scene 1 – The Real-Life Problem (hook).
Template A: centred stage throughout.
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

class Scene1Hook(Base):
    def construct(self):
        sents, total_dur = _load_scene_timings("scene1")

        hdr = header(1, "The Real-Life Problem")
        self.add(hdr)

        # ── Beat 0: hook question ────────────────────────────────────────────
        sync_to(self, sents[0]["start"])
        q = T("Can you predict where a cricket ball will be at any moment?", 34, INK)
        if q.width > CONTENT_W: q.scale_to_fit_width(CONTENT_W)
        q.move_to(CONTENT_CENTER + UP * 1.5)
        self.play(FadeIn(q), run_time=0.8)

        # ── Beat 1: setup ────────────────────────────────────────────────────
        sync_to(self, sents[1]["start"])
        setup_rows = VGroup(
            T("Ball thrown straight up at 20 m/s", 32, INK),
            T("Gravity: 10 m/s²  (simplified from 9.8)", 28, MUTED),
        ).arrange(DOWN, buff=0.22)
        setup_box = card(setup_rows, color=CURVE, pad=0.35)
        setup_box.move_to(CONTENT_CENTER + DOWN * 0.5)
        if setup_box.height > 2.2: setup_box.scale_to_fit_height(2.2)
        if setup_box.width > CONTENT_W: setup_box.scale_to_fit_width(CONTENT_W)
        self.play(FadeIn(setup_box), run_time=0.8)

        # ── Beat 2: input / output ───────────────────────────────────────────
        sync_to(self, sents[2]["start"])
        io_row = VGroup(
            pill("Input: t = time (s)", CURVE, 30),
            T("→", 36, MUTED),
            pill("Output: h(t) = height (m)", GOOD, 30),
        ).arrange(RIGHT, buff=0.5)
        io_row.move_to(CONTENT_CENTER + DOWN * 2.0)
        if io_row.width > CONTENT_W: io_row.scale_to_fit_width(CONTENT_W)
        self.play(FadeIn(io_row), run_time=0.8)

        # ── Beat 3: function machine ─────────────────────────────────────────
        sync_to(self, sents[3]["start"])
        self.play(FadeOut(q), FadeOut(setup_box), FadeOut(io_row), run_time=0.4)

        in_pill  = pill("t  (seconds)", CURVE, 30)
        rule_box = card(T("h(t) = 20t − 5t²", 36, POINT, bold=True), color=POINT, pad=0.3)
        out_pill = pill("h(t)  (metres)", GOOD, 30)
        machine  = VGroup(in_pill, rule_box, out_pill).arrange(RIGHT, buff=0.6)
        place(machine, center=CONTENT_CENTER)

        # arrows LAST
        arr1 = Arrow(in_pill.get_right(),  rule_box.get_left(),  buff=0.12,
                     stroke_width=3, tip_length=0.18, color=MUTED)
        arr2 = Arrow(rule_box.get_right(), out_pill.get_left(), buff=0.12,
                     stroke_width=3, tip_length=0.18, color=MUTED)
        lbl1 = T("INPUT",  22, MUTED).next_to(arr1, UP, buff=0.1)
        lbl2 = T("OUTPUT", 22, MUTED).next_to(arr2, UP, buff=0.1)
        func_title = T("Function Machine", 30, INK).move_to(machine).shift(UP * 1.65)

        self.play(FadeIn(func_title), FadeIn(machine),
                  FadeIn(arr1), FadeIn(arr2), FadeIn(lbl1), FadeIn(lbl2), run_time=0.8)

        # ── Beat 4-6: three learning goals ──────────────────────────────────
        sync_to(self, sents[4]["start"])
        self.play(FadeOut(func_title), FadeOut(machine),
                  FadeOut(arr1), FadeOut(arr2), FadeOut(lbl1), FadeOut(lbl2), run_time=0.4)

        goals = VGroup(
            pill("① What is a function?",           CURVE, 30),
            pill("② How do we plot its graph?",     GOOD,  30),
            pill("③ What do key features tell us?", MAXC,  30),
        ).arrange(DOWN, buff=0.38)
        goals_box = card(
            T("By the end of this video you will:", 32, INK, bold=True),
            goals, color=CURVE, pad=0.42
        )
        place(goals_box)
        self.play(FadeIn(goals_box), run_time=0.8)

        sync_to(self, total_dur + 0.15)
        check_layout(self)
