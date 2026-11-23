"""
scene0_title.py – Opening card (6 s, silent).
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from design import *

class Scene0Title(Base):
    def construct(self):
        # ── Title group ──────────────────────────────────────────────────
        title = T("From Input to Output:", 54, INK, bold=True)
        sub   = T("Reading the Graph of a Function", 30, MUTED)
        title_grp = VGroup(title, sub).arrange(DOWN, buff=0.25).move_to(UP * 2.1)

        # ── Parabola arc under title with glow ────────────────────────────
        # Frame coordinates: x in [-3.5, 3.5], y = 0.6 - 0.22 * x^2
        parabola = ParametricFunction(
            lambda s: np.array([s, 0.6 - 0.20 * s**2, 0]),
            t_range=[-3.5, 3.5, 0.05],
            color=CURVE, stroke_width=4
        )
        parabola_glow = parabola.copy().set_stroke(CURVE, width=14, opacity=0.18)

        # ── Cricket ball riding the curve ─────────────────────────────────
        s_val = ValueTracker(-3.5)
        ball = always_redraw(
            lambda: make_ball(0.25).move_to(
                np.array([s_val.get_value(), 0.6 - 0.20 * (s_val.get_value()**2), 0])
            )
        )

        # ── Author credentials ────────────────────────────────────────────
        id_pill = pill("Samruddhi Meshram | E25B070759", POINT, 26).move_to(DOWN * 2.0)
        course  = T("Linear Algebra and Calculus (M3)", 22, MUTED).move_to(DOWN * 2.55)

        # ── Choreography (exactly 6.0 seconds) ────────────────────────────
        self.play(FadeIn(title_grp, shift=UP*0.2), run_time=1.0)
        self.play(Create(parabola_glow), Create(parabola), run_time=0.8)
        self.add(ball)
        self.play(s_val.animate.set_value(3.5), run_time=2.4, rate_func=linear)
        self.play(FadeIn(id_pill, shift=UP*0.2), FadeIn(course, shift=UP*0.2), run_time=0.8)
        
        # Sync to exactly 6.0s
        sync_to(self, 6.0)
        check_layout(self)
