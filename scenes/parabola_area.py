from manim import *


class Graphing(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-8, 8, 2], x_length=10, y_range=[-6,14, 2], y_length=10).add_coordinates()
        labels = plane.get_axis_labels(x_label='x', y_label='f(x)')
        parab = plane.plot(lambda x: x**2 - 4 , x_range=[-4,4,0.01], color=BLUE)
        semi = plane.plot(lambda x: np.sqrt(max(0, 16 - x**2)) , x_range=[-4,4,0.01], color=BLUE)
        parab_label = MathTex("f(x) = x^2 - 4").scale(0.8).to_corner(UL)
        semi_label = MathTex(r"f(x) = \sqrt{16 - x^2}").scale(0.8).next_to(parab_label, DOWN, buff=0.2)
        area = plane.get_riemann_rectangles(
            parab,
            x_range=[-4, 4],
            dx=0.05,
            stroke_color=TEAL,
        )
        area2 = plane.get_riemann_rectangles(
            semi,
            x_range=[-4, 4],
            dx=0.05,
            stroke_color=PURPLE,
        )
        area.set_fill(TEAL, opacity=0.5)
        self.play(DrawBorderThenFill(plane))
        self.play(Create(labels))
        self.wait(1)
        self.play(Create(VGroup(parab, parab_label), run_time=2))
        self.wait(0.5)
        self.play(Create(VGroup(semi, semi_label), run_time=2))
        self.wait(2)
        self.play(Create(area))
        self.wait(1)
        self.play(Transform(area, area.copy().set_color(PURPLE)))
        self.wait(1)
        self.play(Transform(area, area2))
        self.play(Create(area2))

        self.wait()
