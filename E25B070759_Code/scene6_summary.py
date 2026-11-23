from manim import *
from helpers import BG, CURVE, POINT, GOOD, BAD, MAXC, fit, boxed, check_bounds, sync_to, configure_scene, load_timings

class Scene6Summary(Scene):
    def __init__(self, textbook="Thomas' Calculus (14th Edition), Hass, Heil, Weir", music="No background music", **kwargs):
        super().__init__(**kwargs)
        self.textbook = textbook
        self.music = music

    def construct(self):
        configure_scene(self)
        timings = load_timings("scene6")
        total_audio = timings.get("total_duration", 27.456)
        sentences = {s["beat_index"]: s for s in timings.get("sentences", [])}
        
        # Header
        header = Text("Key Takeaways & Summary", font_size=40, weight=BOLD, color=WHITE)
        header.to_edge(UP, buff=0.45)
        self.add(header)
        
        # Beat 1: [0.00 - 2.18] "Let's recap three ideas."
        sync_to(self, sentences[1]["start"])
        recap_intro = Text("Three Core Principles to Remember:", font_size=30, color=LIGHT_GRAY).move_to(UP*1.5)
        self.play(FadeIn(recap_intro), run_time=0.8)
        
        # Beat 2: [2.48 - 8.48] "One: a function gives each input exactly one output, and the vertical line test checks this on a graph."
        sync_to(self, sentences[2]["start"])
        self.play(FadeOut(recap_intro), run_time=0.3)
        
        c1_title = Text("1. Exactly ONE Output per Input", font_size=32, weight=BOLD, color=POINT)
        c1_b1 = Text("• A function assigns to each allowed input exactly one output.", font_size=26, color=WHITE)
        c1_b2 = Text("• Geometrically verified by the Vertical Line Test (crosses at most once).", font_size=26, color=GOOD)
        c1_b3 = Text("• Multiple inputs sharing an output is valid; multiple outputs for one input is not.", font_size=24, color=LIGHT_GRAY)
        c1_grp = VGroup(c1_title, c1_b1, c1_b2, c1_b3).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        c1_card = fit(boxed(c1_grp, color=POINT, pad=0.35)).move_to(DOWN*0.2)
        self.play(FadeIn(c1_card, shift=UP*0.2), run_time=1.2)
        
        # Beat 3: [8.78 - 14.54] "Two: on a graph, each point is an input-output pair, with the input on the horizontal axis."
        sync_to(self, sentences[3]["start"])
        self.play(FadeOut(c1_card), run_time=0.4)
        
        c2_title = Text("2. Every Point is an (Input, Output) Pair", font_size=32, weight=BOLD, color=CURVE)
        c2_b1 = Text("• Horizontal axis represents the input (time t in seconds).", font_size=26, color=WHITE)
        c2_b2 = Text("• Vertical axis represents the output (height h(t) in metres).", font_size=26, color=WHITE)
        c2_b3 = Text("• The curve shows height vs. time, NOT the physical path through space.", font_size=24, color=BAD)
        c2_grp = VGroup(c2_title, c2_b1, c2_b2, c2_b3).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        c2_card = fit(boxed(c2_grp, color=CURVE, pad=0.35)).move_to(DOWN*0.2)
        self.play(FadeIn(c2_card, shift=UP*0.2), run_time=1.2)
        
        # Beat 4: [14.84 - 21.56] "Three: the intercepts, the maximum, the domain and range, and where the graph rises or falls, tell the real-life story."
        sync_to(self, sentences[4]["start"])
        self.play(FadeOut(c2_card), run_time=0.4)
        
        c3_title = Text("3. Features Tell the Real-Life Story", font_size=32, weight=BOLD, color=GOOD)
        c3_b1 = Text("• Intercepts: Launch at (0, 0) and landing at (4, 0).", font_size=24, color=GOOD)
        c3_b2 = Text("• Maximum: Peak height 20 m reached at t = 2 s.", font_size=24, color=MAXC)
        c3_b3 = Text("• Domain & Range: Valid flight domain [0, 4] s; range [0, 20] m.", font_size=24, color=POINT)
        c3_b4 = Text("• Behaviour: Climbing on [0, 2] s, falling on [2, 4] s.", font_size=24, color=WHITE)
        c3_grp = VGroup(c3_title, c3_b1, c3_b2, c3_b3, c3_b4).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        c3_card = fit(boxed(c3_grp, color=GOOD, pad=0.35)).move_to(DOWN*0.2)
        self.play(FadeIn(c3_card, shift=UP*0.2), run_time=1.2)
        
        # Beat 5: [21.86 - 23.74] "Thanks for watching."
        # Beat 6: [24.04 - 27.18] "Credits and the AI disclosure are on screen."
        sync_to(self, sentences[5]["start"])
        self.play(FadeOut(c3_card), FadeOut(header), run_time=0.6)
        
        # Closing Frame
        takeaway = Text("What goes in? What comes out? What does each feature mean?", font_size=28, weight=BOLD, color=POINT)
        takeaway_box = boxed(takeaway, color=POINT, pad=0.2)
        
        student_info = Text("Samruddhi Meshram | ID: E25B070759", font_size=26, weight=BOLD, color=WHITE)
        course_info = Text("Linear Algebra and Calculus (M3)", font_size=24, color=CURVE)
        
        ref_text = Text(f"Reference: {self.textbook}", font_size=20, color=LIGHT_GRAY)
        music_text = Text(f"Music Credit: {self.music}", font_size=20, color=LIGHT_GRAY)
        
        ai_disc = Text(
            "AI disclosure: code, script and narration voice created with AI tools;\nmaths verified by the student. Full details in README.md.",
            font_size=18, color=GRAY, line_spacing=1.2
        )
        
        closing_content = VGroup(
            takeaway_box,
            student_info,
            course_info,
            ref_text,
            music_text,
            ai_disc
        ).arrange(DOWN, buff=0.28)
        
        closing_frame = fit(boxed(closing_content, color=CURVE, pad=0.35)).move_to(ORIGIN)
        self.play(FadeIn(closing_frame, shift=UP*0.2), run_time=1.2)
        
        # Hold frame through end of narration + safety buffer
        sync_to(self, total_audio + 0.15)
        check_bounds(self)

