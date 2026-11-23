from manim import *
from helpers import BG, CURVE, POINT, GOOD, BAD, MAXC, fit, boxed, check_bounds, sync_to, configure_scene, load_timings

class Scene5Interpretation(Scene):
    def construct(self):
        configure_scene(self)
        timings = load_timings("scene5")
        total_audio = timings.get("total_duration", 35.832)
        sentences = {s["beat_index"]: s for s in timings.get("sentences", [])}
        
        # Header
        header = Text("Physical Interpretation: Reading the Story", font_size=40, weight=BOLD, color=WHITE)
        header.to_edge(UP, buff=0.45)
        self.add(header)
        
        # Ruler on the far left
        ruler_x = -5.5
        y_bot = -2.5
        y_top = 1.7
        ruler_scale = (y_top - y_bot) / 20.0
        ruler = Line(start=np.array([ruler_x, y_bot, 0]), end=np.array([ruler_x, y_top, 0]), color=LIGHT_GRAY, stroke_width=3)
        ticks = VGroup()
        for m in [0, 5, 10, 15, 20]:
            y_p = y_bot + m * ruler_scale
            t_l = Line(start=np.array([ruler_x - 0.1, y_p, 0]), end=np.array([ruler_x + 0.1, y_p, 0]), color=LIGHT_GRAY)
            t_lbl = Text(f"{m}m", font_size=18, color=LIGHT_GRAY).next_to(t_l, LEFT, buff=0.1)
            ticks.add(t_l, t_lbl)
            
        ruler_grp = VGroup(ruler, ticks)
        
        # Axes in Center/Right
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 25, 5],
            x_length=5.6,
            y_length=4.2,
            axis_config={"color": LIGHT_GRAY, "include_numbers": True, "font_size": 20},
            tips=True
        ).move_to(np.array([0.5, -0.6, 0]))
        
        x_lbl = Text("Time t (s)", font_size=20, color=LIGHT_GRAY).next_to(axes.x_axis.get_end(), DOWN, buff=0.2).shift(LEFT*0.5)
        y_lbl = Text("Height h (m)", font_size=20, color=LIGHT_GRAY).next_to(axes.y_axis.get_end(), UP, buff=0.2).shift(RIGHT*0.3)
        parabola = axes.plot(lambda t: 20*t - 5*t**2, x_range=[0, 4], color=CURVE, stroke_width=3.5)
        
        # ValueTracker for time t
        t_tracker = ValueTracker(0.0)
        
        # Ball on ruler
        ball = always_redraw(lambda: Dot(
            point=np.array([ruler_x, y_bot + (20*t_tracker.get_value() - 5*t_tracker.get_value()**2)*ruler_scale, 0]),
            radius=0.18, color="#E11D48"
        ))
        
        # Dot on parabola
        graph_dot = always_redraw(lambda: Dot(
            point=axes.c2p(t_tracker.get_value(), 20*t_tracker.get_value() - 5*t_tracker.get_value()**2),
            radius=0.12, color=POINT
        ))
        
        # Connecting line from ball to graph dot
        connect_line = always_redraw(lambda: DashedLine(
            start=ball.get_center(),
            end=graph_dot.get_center(),
            color=GRAY, stroke_width=1.5
        ))
        
        # Beat 1: [0.00 - 2.57] "Now let's read the graph as a story."
        sync_to(self, sentences[1]["start"])
        self.play(FadeIn(ruler_grp), FadeIn(axes), FadeIn(x_lbl), FadeIn(y_lbl), FadeIn(parabola), FadeIn(ball), FadeIn(graph_dot), FadeIn(connect_line), run_time=1.2)
        
        # Ball moves t: 0 -> 1 during intro
        self.play(t_tracker.animate.set_value(1.0), rate_func=linear, run_time=1.2)
        
        # Beat 2: [2.87 - 6.61] "The starting point says: the ball leaves your hand at height zero."
        sync_to(self, sentences[2]["start"])
        self.play(t_tracker.animate.set_value(0.0), run_time=0.6)
        c1_dot = Dot(point=axes.c2p(0, 0), radius=0.14, color=GOOD)
        c1_lbl = Text("Starts at height 0 m", font_size=20, weight=BOLD, color=GOOD)
        c1_box = boxed(c1_lbl, color=GOOD, pad=0.15).move_to(axes.c2p(0.8, 4))
        c1_arr = Arrow(start=c1_box.get_bottom(), end=axes.c2p(0, 0), color=GOOD, buff=0.1, stroke_width=2.5)
        self.play(FadeIn(c1_dot), FadeIn(c1_box), GrowArrow(c1_arr), run_time=1.0)
        
        # Ball moves to peak t: 2
        # Beat 3: [6.91 - 12.50] "The peak says: for an instant, at two seconds, the ball is twenty metres up and stops rising."
        sync_to(self, sentences[3]["start"])
        self.play(t_tracker.animate.set_value(2.0), rate_func=rush_from, run_time=1.6)
        c2_dot = Dot(point=axes.c2p(2, 20), radius=0.14, color=MAXC)
        c2_t1 = Text("Peak: 20 m at t = 2 s", font_size=20, weight=BOLD, color=MAXC)
        c2_t2 = Text("Stops rising for an instant", font_size=18, color=WHITE)
        c2_box = boxed(VGroup(c2_t1, c2_t2).arrange(DOWN, buff=0.1), color=MAXC, pad=0.15).move_to(axes.c2p(3.5, 21.0))
        c2_arr = Arrow(start=c2_box.get_left(), end=axes.c2p(2, 20), color=MAXC, buff=0.15, stroke_width=2.5)
        self.play(FadeIn(c2_dot), FadeIn(c2_box), GrowArrow(c2_arr), run_time=1.2)
        
        # Ball moves to land t: 4
        # Beat 4: [12.80 - 16.28] "The second intercept says: it lands after four seconds."
        sync_to(self, sentences[4]["start"])
        self.play(t_tracker.animate.set_value(4.0), rate_func=rush_into, run_time=1.6)
        c3_dot = Dot(point=axes.c2p(4, 0), radius=0.14, color=GOOD)
        c3_lbl = Text("Lands after 4 s", font_size=20, weight=BOLD, color=GOOD)
        c3_box = boxed(c3_lbl, color=GOOD, pad=0.15).move_to(axes.c2p(3.2, 4))
        c3_arr = Arrow(start=c3_box.get_bottom(), end=axes.c2p(4, 0), color=GOOD, buff=0.1, stroke_width=2.5)
        self.play(FadeIn(c3_dot), FadeIn(c3_box), GrowArrow(c3_arr), run_time=1.0)
        
        # Beat 5: [16.58 - 20.98] "The symmetry says: it takes exactly as long to fall as to rise."
        sync_to(self, sentences[5]["start"])
        self.play(
            FadeOut(c1_box), FadeOut(c1_arr),
            FadeOut(c2_box), FadeOut(c2_arr),
            FadeOut(c3_box), FadeOut(c3_arr),
            run_time=0.5
        )
        sym_line = DashedLine(start=axes.c2p(2, 0), end=axes.c2p(2, 21), color=POINT, stroke_width=2.5)
        sym_lbl = Text("Symmetry: Rise Time (2 s) = Fall Time (2 s)", font_size=22, weight=BOLD, color=POINT)
        sym_box = boxed(sym_lbl, color=POINT, pad=0.2).move_to(np.array([2.5, 2.2, 0]))
        self.play(Create(sym_line), FadeIn(sym_box), run_time=1.2)
        
        # Beat 6: [21.28 - 26.68] "And the domain reminds us that this formula describes the ball only between zero and four seconds."
        sync_to(self, sentences[6]["start"])
        self.play(FadeOut(sym_box), FadeOut(sym_line), run_time=0.4)
        
        dom_bracket = Line(start=axes.c2p(0, -2.5), end=axes.c2p(4, -2.5), color=GOOD, stroke_width=6)
        dom_txt = Text("Physical Domain: 0 <= t <= 4 s (flight only)", font_size=22, weight=BOLD, color=GOOD)
        dom_box = boxed(dom_txt, color=GOOD, pad=0.2).next_to(axes.c2p(2, 0), DOWN, buff=0.7)
        self.play(Create(dom_bracket), FadeIn(dom_box), run_time=1.2)
        
        # Beat 7: [26.98 - 30.86] "Before the throw, or after the landing, it says nothing useful."
        sync_to(self, sentences[7]["start"])
        t_neg = Text("t < 0: not yet thrown", font_size=18, color=BAD).move_to(axes.c2p(-0.5, 5))
        t_pos = Text("t > 4: on the ground", font_size=18, color=BAD).move_to(axes.c2p(4.5, 5))
        self.play(FadeIn(t_neg), FadeIn(t_pos), run_time=1.0)
        
        # Beat 8: [31.16 - 35.44] "That is the power of a graph: it shows a whole relationship at a glance."
        sync_to(self, sentences[8]["start"])
        self.play(
            FadeOut(dom_bracket), FadeOut(dom_box), FadeOut(t_neg), FadeOut(t_pos),
            FadeOut(c1_dot), FadeOut(c2_dot), FadeOut(c3_dot),
            FadeOut(ruler_grp), FadeOut(axes), FadeOut(x_lbl), FadeOut(y_lbl),
            FadeOut(parabola), FadeOut(ball), FadeOut(graph_dot), FadeOut(connect_line),
            FadeOut(header),
            run_time=0.8
        )
        
        takeaway_title = Text("The Power of a Graph", font_size=40, weight=BOLD, color=WHITE)
        takeaway_t = Text("A graph shows the whole physical relationship at a single glance!", font_size=30, weight=BOLD, color=CURVE)
        takeaway_sub = Text("Every point is an event; every feature tells the story.", font_size=26, color=POINT)
        takeaway_group = VGroup(takeaway_title, takeaway_t, takeaway_sub).arrange(DOWN, buff=0.4)
        takeaway_card = fit(boxed(takeaway_group, color=CURVE, pad=0.45)).move_to(ORIGIN)
        self.play(FadeIn(takeaway_card, shift=UP*0.2), run_time=1.2)
        
        sync_to(self, total_audio + 0.15)
        check_bounds(self)

