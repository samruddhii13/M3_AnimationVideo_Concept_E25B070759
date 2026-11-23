from manim import *
from helpers import BG, CURVE, POINT, GOOD, BAD, MAXC, fit, boxed, check_bounds, sync_to, configure_scene, load_timings

class Scene0Title(Scene):
    def construct(self):
        configure_scene(self)
        
        title = Text("From Input to Output:\nReading the Graph of a Function", font_size=46, weight=BOLD, line_spacing=1.2, color=WHITE)
        subtitle = Text("Single-variable functions and graphs (M3 Calculus)", font_size=32, color=CURVE)
        example = Text("Example: A cricket ball thrown straight up", font_size=28, color=POINT)
        student = Text("Samruddhi Meshram | ID: E25B070759", font_size=28, color=LIGHT_GRAY)
        
        content = VGroup(title, subtitle, example, student).arrange(DOWN, buff=0.45)
        box = SurroundingRectangle(content, color=CURVE, buff=0.45, corner_radius=0.15)
        card = fit(VGroup(box, content)).move_to(ORIGIN)
        
        self.play(FadeIn(card, shift=UP*0.2), run_time=1.5)
        self.wait(3.5)
        self.play(FadeOut(card, shift=DOWN*0.2), run_time=1.0)
        
        check_bounds(self)

