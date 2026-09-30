from manim import *

class HelloWorld(ThreeDScene):
    def construct(self):
        circle = Sphere()
        square = Cube()
        self.add(circle)
        self.add(square)
        self.add(ThreeDAxes())
        circle.set_fill(color="#FF0000", opacity=0.5)
        square.set_fill(color="#00FF00", opacity=0.5)
        circle.set_stroke(color="#FF0000", width=4)
        square.set_stroke(color="#00FF00", width=4)
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
        self.play(circle.animate.move_to([2, 0, 0]), square.animate.move_to([-2, 0, 0]))
        self.wait(1)
        self.play(circle.animate.move_to([1, 1, 0]), square.animate.move_to([-1, -1, 0]))
        self.wait(1)
        self.play(circle.animate.move_to([1, 1, 1]), square.animate.move_to([-1, -1, -1]))
        self.wait(1)
