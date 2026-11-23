"""Scene 0 – Title card (silent, 5 s)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from design import *

class Scene0Title(Base):
    def construct(self):
        logo = T("M3 · Linear Algebra and Calculus", 28, MUTED)
        title = T("From Input to Output:", 48, INK, bold=True)
        sub   = T("Reading the Graph of a Function", 40, CURVE, bold=True)
        rule_line = Line(LEFT*4, RIGHT*4, stroke_width=1.5, color=MUTED).set_opacity(0.5)
        example = T("Example: a cricket ball thrown straight up", 30, INK)
        meta = VGroup(
            T("Samruddhi Meshram  ·  E25B070759", 26, MUTED),
            T("Course: Linear Algebra and Calculus (M3)", 26, MUTED),
        ).arrange(DOWN, buff=0.18)

        content = VGroup(logo, title, sub, rule_line, example, meta).arrange(DOWN, buff=0.38)
        place(content)

        bx = SurroundingRectangle(content, buff=0.5, corner_radius=0.22,
                                  color=CURVE, stroke_width=2.5,
                                  fill_color=CURVE, fill_opacity=0.06)
        self.add(bx, content)

        # progress track (empty at scene 0)
        w = config.frame_width
        track = Line(LEFT*w/2, RIGHT*w/2, stroke_width=4, color=WHITE).set_opacity(0.12)
        track.to_edge(UP, buff=0.05)
        self.add(track)

        self.wait(5)
        check_layout(self)
