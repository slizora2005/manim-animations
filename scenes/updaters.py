from manim import *


class Updaters(Scene):
    def construct(self):
        num = MathTex("ln(2)")
        box = always_redraw(lambda : SurroundingRectangle(num, color=BLUE, buff=0.5))
        name = always_redraw(lambda : Tex("ln(2)'s captor").next_to(box,DOWN, buff=0.25))
        self.play(Create(VGroup(num, box, name)))
        self.play(num.animate.shift(RIGHT*2), run_time=1.5)
        self.play(num.animate.shift(LEFT*4), run_time=1.5)
        self.play(num.animate.shift(RIGHT*2), run_time=1)

        self.wait()
