from manim import *


class ComplexNumberIntroduction(Scene):
    def construct(self):
        title = Text("Liczby Zespolone")
        self.play(Write(title))
        self.wait(2)


        slide1 = Text("Budowa Liczby Zespolonej").to_edge(UP)
        self.play(ReplacementTransform(title, slide1))

        real_part = MathTex("3").scale(2).shift(LEFT*0.5)
        plus = MathTex("+").scale(2).next_to(real_part, RIGHT, buff=0.5)
        imaginary_part = MathTex("2i").scale(2).next_to(plus, RIGHT, buff=0.5)


        real = Text("Część rzeczywista").scale(0.75).to_corner(DOWN + LEFT).set_color(RED)
        imaginary = Text("Część urojona").scale(0.75).to_corner(DOWN + RIGHT).set_color(GREEN)


        arrow_real = Arrow(start=[2,2,0], end=[0,0,0]).next_to(real_part[0][0], DOWN, buff=0.5).shift(LEFT).set_color(RED)
        arrow_imaginary = Arrow(start=[0,6,0], end=[2,4,0]).next_to(imaginary_part[0][0], DOWN, buff=0.5).shift(RIGHT * 2).set_color(GREEN)


        self.play(Write(real_part), Write(plus), Write(imaginary_part))
        self.play( GrowArrow(arrow_real), Write(real), real_part.animate.set_color(RED))
        self.play(GrowArrow(arrow_imaginary), Write(imaginary), imaginary_part.animate.set_color(GREEN))

        self.wait(4)


class ImaginaryNumber(Scene):
    def construct(self):
        title = Text("Czym jest i?").to_edge(UP)
        self.play(Write(title))

        def1 = MathTex(r"i = \sqrt{-1}")
        self.play(Write(def1))

        txt = Text("albo").next_to(def1, DOWN, buff=0.5)
        def2 = MathTex("i^2 = -1").next_to(txt, DOWN, buff=0.5)
        self.play(Write(txt), Write(def2))

        self.wait(4)


class ComplexPlain(Scene):
    def construct(self):
        plane = ComplexPlane(background_line_style={"stroke_opacity": 0}).add_coordinates()
        title = Text("Płaszczyzna Zespolona", font_size=36, color=BLUE).to_corner(UP+LEFT)
        self.play(FadeIn(plane, shift=UP))
        self.play(Write(title))

        real_axis = Line(plane.n2p(-5), plane.n2p(5), color=GREEN)
        imag_axis = Line(plane.n2p(0 - 5j), plane.n2p(0 + 5j), color=YELLOW)
        real_label = Text("Oś rzeczywista", font_size=24, color=GREEN).next_to(real_axis, DOWN).shift(RIGHT*1.5)
        imag_label = Text("Oś urojona", font_size=24, color=YELLOW).next_to(imag_axis, LEFT).shift(UP*1)

        self.play(Create(real_axis), Write(real_label))
        self.play(Create(imag_axis), Write(imag_label))

        z = 3 + 2j
        point = Dot(plane.n2p(z), color=RED)
        label = Text("Liczba Zespolona: 3 + 2i", font_size=15).next_to(point, UR, buff=0.1)
        dashed_line_x = DashedLine(start=plane.n2p(z), end=[plane.n2p(z)[0], 0, 0], color=RED)
        dashed_line_y = DashedLine(start=plane.n2p(z), end=[0, plane.n2p(z)[1], 0], color=RED)
        self.play(FadeIn(point, label, dashed_line_x, dashed_line_y))

        self.wait(4)


class RealOperations(Scene):
    def construct(self):
        plane = ComplexPlane(background_line_style={"stroke_opacity": 0}).add_coordinates()
        title = Text("Operacje rzeczywiste", font_size=36, color=BLUE).to_corner(UP+LEFT)
        self.play(FadeIn(plane, shift=UP))
        self.play(Write(title))

        z = 2 + 1j
        origin = plane.n2p(0)
        point = Dot(plane.n2p(z), color=RED)
        label = Text("Liczba Zespolona: 2 + 1i", font_size=15, color=RED).next_to(point, DR, buff=0.1)
        arrow_to_z = Arrow(origin, point.get_center(), color=RED)
        self.play(FadeIn(point, label), GrowArrow(arrow_to_z))

        opposite = -2 - 1j
        op_point = Dot(plane.n2p(opposite), color=GREEN)
        op_label = Text("Liczba Przeciwna: -2 - 1i", font_size=15, color=GREEN).next_to(op_point, UL, buff=0.1)
        arrow_to_opposite = Arrow(origin, op_point.get_center(), color=GREEN)
        self.play(FadeIn(op_point, op_label), GrowArrow(arrow_to_opposite))

        conjugate = 2 - 1j
        con_point = Dot(plane.n2p(conjugate), color=ORANGE)
        con_label = Text("Liczba Sprzężona: 2 - 1i", font_size=15, color=ORANGE).next_to(con_point, UR, buff=0.1)
        arrow_to_conjugate = Arrow(origin, con_point.get_center(), color=ORANGE)
        self.play(FadeIn(con_point, con_label), GrowArrow(arrow_to_conjugate))

        times2 = 4 + 2j
        times2_point = Dot(plane.n2p(times2), color=YELLOW)
        times2_label = Text("Liczba Podwojona: 4 - 2i", font_size=15, color=YELLOW).next_to(times2_point, UR, buff=0.1)
        arrow_to_times2 = Arrow(origin, times2_point.get_center(), color=YELLOW)
        self.play(FadeIn(times2_point, times2_label), GrowArrow(arrow_to_times2))

        self.wait(4)


class AdditionOperations(Scene):
    def construct(self):
        plane = ComplexPlane(background_line_style={"stroke_opacity": 0}).add_coordinates()
        title = Text("Dodawanie", font_size=36, color=BLUE).to_corner(UP+LEFT)
        self.play(FadeIn(plane, shift=UP))
        self.play(Write(title))


        z1 = 2 + 1j
        z2 = 1 + 2j
        z_sum = z1 + z2


        point_z1 = Dot(plane.n2p(z1), color=RED)
        label_z1 = Text("z1 = 2 + 1i", font_size=15, color=RED).next_to(point_z1, UR, buff=0.1)
        arrow_z1 = Arrow(plane.n2p(0), plane.n2p(z1), color=RED)


        point_z2 = Dot(plane.n2p(z2), color=GREEN)
        label_z2 = Text("z2 = 1 + 2i", font_size=15, color=GREEN).next_to(point_z2, UR, buff=0.1)
        arrow_z2 = Arrow(plane.n2p(0), plane.n2p(z2), color=GREEN)


        point_z_sum = Dot(plane.n2p(z_sum), color=ORANGE)
        label_z_sum = Text("z1 + z2 = 3 + 3i", font_size=15, color=ORANGE).next_to(point_z_sum, UR, buff=0.1)
        arrow_z_sum = Arrow(plane.n2p(0), plane.n2p(z_sum), color=ORANGE, buff=0)

        z2_vector = DashedLine(start=plane.n2p(0), end=plane.n2p(z2), color=YELLOW)
        result_vector = DashedLine(start=plane.n2p(z1), end=plane.n2p(z_sum), color=YELLOW)

        self.play(GrowArrow(arrow_z1), FadeIn(point_z1, label_z1))
        self.wait(1)
        self.play(GrowArrow(arrow_z2), FadeIn(point_z2, label_z2))
        self.wait(1)
        self.play(Create(z2_vector))
        self.wait(1)
        self.play(ReplacementTransform(z2_vector,result_vector))
        self.play(GrowArrow(arrow_z_sum), FadeIn(point_z_sum, label_z_sum))
        self.wait(4)


class TrigonometricForm(Scene):
    def construct(self):
        plane = ComplexPlane(background_line_style={"stroke_opacity": 0}).add_coordinates()
        title = Text("Postać Trygonometryczna", font_size=36, color=BLUE).to_corner(UP+LEFT)
        self.play(FadeIn(plane, shift=UP))
        self.play(Write(title))

        z = -4 - 3j

        point = Dot(plane.n2p(z), color=RED)
        label = Text("z = x + yi", font_size=15, color=RED).next_to(point, UL, buff=0.1)

        origin = plane.n2p(0)
        arrow = Arrow(origin, point.get_center(), color=RED)

        angle_phi = np.angle(z)
        angle_theta = 2 * np.pi + angle_phi

        arc_theta = Arc(
            radius=1,
            start_angle=0,
            angle=angle_theta,
            color=RED,
        )

        theta_label = MathTex(r"\theta", font_size=35, color=RED).move_to(
            arc_theta.point_from_proportion(0.25) + 0.3 * UP + 0.3 * LEFT)

        arrow_label = MathTex(r"|z| = \sqrt{x^2 + y^2}", font_size=27, color=RED).next_to(arrow).shift(LEFT*2)
        arrow_label.shift(DOWN*0.4)

        dashed_line_x = DashedLine(start=plane.n2p(z), end=[plane.n2p(z)[0], 0, 0], color=RED)
        dashed_line_y = DashedLine(start=plane.n2p(z), end=[0, plane.n2p(z)[1], 0], color=RED)

        x_label = Text("X", font_size=15, color=RED).next_to(dashed_line_x.end, UP, buff=0.1)
        y_label = Text("Y", font_size=15, color=RED).next_to(dashed_line_y.end, RIGHT, buff=0.1)


        self.play(GrowArrow(arrow), FadeIn(point, label))
        self.wait(1)
        self.play(Create(arc_theta), FadeIn(theta_label, arrow_label, dashed_line_x, dashed_line_y,x_label,y_label))
        self.wait(1)

        trygo_form = MathTex(r"z = |z|(cos \theta + i sin \theta)", color=RED).to_corner(UP + RIGHT)
        self.play(Write(trygo_form))
        self.wait(4)


class Multiplication(Scene):
    def construct(self):
        plane = ComplexPlane(background_line_style={"stroke_opacity": 0}).add_coordinates()
        title = Text("Mnozenie", font_size=36, color=BLUE).to_corner(UP+LEFT)
        self.play(FadeIn(plane, shift=UP))
        self.play(Write(title))

        z1 = 1 + 2j
        z2 = -2 + 1j
        z_product = z1 * z2

        point_z1 = Dot(plane.n2p(z1), color=RED)
        label_z1 = Text("z1", font_size=15, color=RED).next_to(point_z1, UR, buff=0.1)
        arrow_z1 = Arrow(plane.n2p(0), plane.n2p(z1), color=RED)
        z1_arrow_label = Text("|z1|", font_size=15, color=RED).next_to(arrow_z1).shift(LEFT*0.5)
        z1_angle = np.angle(z1)
        z1_arc = Arc(
            radius=1,
            start_angle=0,
            angle=z1_angle,
            color=RED,
        )
        z1_angle_label = MathTex(r"\theta 1", font_size=35, color=RED).move_to(
            z1_arc.point_from_proportion(0.25) + 0.2 * UP + 0.4 * LEFT)

        point_z2 = Dot(plane.n2p(z2), color=GREEN)
        label_z2 = Text("z2", font_size=15, color=GREEN).next_to(point_z2, UR, buff=0.1)
        arrow_z2 = Arrow(plane.n2p(0), plane.n2p(z2), color=GREEN)
        z2_arrow_label = Text("|z2|", font_size=15, color=GREEN).next_to(arrow_z2).shift(LEFT*1.5)
        z2_arrow_label.shift(UP*0.5)
        z2_angle = np.angle(z2)
        z2_arc = Arc(
            radius=1,
            start_angle=0,
            angle=z2_angle,
            color=GREEN,
        )
        z2_angle_label = MathTex(r"\theta 2", font_size=35, color=GREEN).move_to(
            z2_arc.point_from_proportion(0.25) + 0.6 * UP + 1.1 * LEFT)

        point_z_product = Dot(plane.n2p(z_product), color=ORANGE)
        label_z_product = Text("z3 = z1 * z2", font_size=15, color=ORANGE).next_to(point_z_product, DR, buff=0.1)
        arrow_z_product = Arrow(plane.n2p(0), plane.n2p(z_product), color=ORANGE)
        z_product_arrow_label = Text("|z1|*|z2|", font_size=15, color=ORANGE).next_to(arrow_z_product).shift(LEFT*1.8)
        tmp_angle = np.angle(z_product)
        z_product_angle = 2 * np.pi + tmp_angle
        z_product_arc = Arc(
            radius=1,
            start_angle=0,
            angle=z_product_angle,
            color=ORANGE,
        )
        z_product_angle_label = MathTex(r"\theta 1 + \theta 2", font_size=35, color=ORANGE).move_to(
            z_product_arc.point_from_proportion(0.25) + 1.5 * DOWN + 2.5 * LEFT)

        self.play(GrowArrow(arrow_z1), FadeIn(point_z1, label_z1, z1_arc, z1_angle_label, z1_arrow_label))
        self.wait(1)
        self.play(GrowArrow(arrow_z2), FadeIn(point_z2, label_z2, z2_arc, z2_angle_label, z2_arrow_label))
        self.wait(1)
        self.play(GrowArrow(arrow_z_product), FadeIn(point_z_product, label_z_product, z_product_arc, z_product_angle_label, z_product_arrow_label))

        z1_text = MathTex(r"z1 = |z1|(cos \theta 1 + i sin \theta 1", font_size=25, color=RED).to_corner(UP + RIGHT)
        z2_text = MathTex(r"z2 = |z2|(cos \theta 2 + i sin \theta 2", font_size=25, color=GREEN).next_to(z1_text, DOWN)
        z3_text = MathTex(r"z3 = |z1|*|z2|(cos(\theta 1 + \theta2) + i sin(\theta 1 + \theta 2))", font_size=25, color=ORANGE).next_to(z2_text, DOWN).shift(LEFT*1.2)
        self.play(FadeIn(z1_text, z2_text, z3_text))

        self.wait(4)


class Power(Scene):
    def construct(self):
        plane = ComplexPlane(background_line_style={"stroke_opacity": 0}).add_coordinates()
        title = Text("Potegowanie", font_size=36, color=BLUE).to_corner(UP+LEFT)
        self.play(FadeIn(plane, shift=UP))
        self.play(Write(title))

        z = 1 + 1j

        point_z = Dot(plane.n2p(z), color=RED)
        label_z = MathTex("z", font_size=35, color=RED).next_to(point_z, UR, buff=0.1)
        arrow_z = Arrow(plane.n2p(0), plane.n2p(z), color=RED)
        z_arrow_label = Text("|z|", font_size=15, color=RED).next_to(arrow_z).shift(LEFT * 0.5)
        z_arrow_label.shift(DOWN*0.2)
        z_angle = np.angle(z)
        z_arc = Arc(
            radius=1,
            start_angle=0,
            angle=z_angle,
            color=RED,
        )
        z_angle_label = MathTex(r"\theta", font_size=35, color=RED).move_to(
            z_arc.point_from_proportion(0.25) + 0.2 * UP + 0.5 * RIGHT)

        point_z_copy = point_z.copy()
        arrow_z_copy = arrow_z.copy()
        z_arc_copy = z_arc.copy()

        self.play(GrowArrow(arrow_z), GrowArrow(arrow_z_copy),
                  FadeIn(point_z, label_z, z_arc, z_angle_label, z_arrow_label, point_z_copy, arrow_z_copy))
        self.wait(1)

        z_2 = z ** 2
        point_z_2 = Dot(plane.n2p(z_2), color=GREEN)
        label_z_2 = MathTex("z^2", font_size=35, color=GREEN).next_to(point_z_2, UR, buff=0.1)
        arrow_z_2 = Arrow(plane.n2p(0), plane.n2p(z_2), color=GREEN)
        z_2_arrow_label = MathTex("|z|^2", font_size=30, color=GREEN).next_to(arrow_z_2).shift(UP*0.5 + LEFT*0.2)
        z_2_angle = np.angle(z_2)
        z_2_arc = Arc(
            radius=1,
            start_angle=0,
            angle=z_2_angle,
            color=GREEN,
        )
        z_2_angle_label = MathTex(r"2*\theta", font_size=30, color=GREEN).move_to(
            z_2_arc.point_from_proportion(0.25) + 0.8 * UP + 0.2 * LEFT)

        point_z_2_copy = point_z_2.copy()
        arrow_z_2_copy = arrow_z_2.copy()
        z_2_arc_copy = z_2_arc.copy()

        self.play(Transform(z_arc_copy, z_2_arc), Transform(point_z_copy, point_z_2),
                  Transform(arrow_z_copy, arrow_z_2), FadeIn(label_z_2, z_2_angle_label, z_2_arrow_label))
        self.play(FadeIn(point_z_2_copy, arrow_z_2_copy, z_2_arc_copy))
        self.wait(1)

        z_3 = z ** 3
        point_z_3 = Dot(plane.n2p(z_3), color=YELLOW)
        label_z_3 = MathTex("z^3", font_size=35, color=YELLOW).next_to(point_z_3, UR, buff=0.1)
        arrow_z_3 = Arrow(plane.n2p(0), plane.n2p(z_3), color=YELLOW)
        z_3_arrow_label = MathTex("|z|^3", font_size=35, color=YELLOW).next_to(arrow_z_3).shift(LEFT * 2)
        z_3_angle = np.angle(z_3)
        z_3_arc = Arc(
            radius=1,
            start_angle=0,
            angle=z_3_angle,
            color=YELLOW,
        )
        z_3_angle_label = MathTex(r"3*\theta", font_size=35, color=YELLOW).move_to(
            z_3_arc.point_from_proportion(0.25) + 0.8 * UP + 1.5 * LEFT)

        self.play(Transform(z_2_arc_copy, z_3_arc), Transform(point_z_2_copy, point_z_3),
                  Transform(arrow_z_2_copy, arrow_z_3), FadeIn(label_z_3, z_3_angle_label, z_3_arrow_label))
        self.wait(1)

        z_text = MathTex(r"z = |z|(cos \theta + i sin \theta)", font_size=25, color=RED).to_corner(UP + RIGHT).shift(
            LEFT * 0.5)
        z_2_text = MathTex(r"z^2 = |z|^2(cos(\theta*2) + i sin(\theta*2))", font_size=25, color=GREEN).next_to(z_text,
            DOWN).shift(LEFT * 0.5)
        z_3_text = MathTex(r"z^3 = |z|^3(cos(\theta*3) + i sin(\theta*3))", font_size=25, color=YELLOW).next_to(
            z_2_text, DOWN)
        self.play(FadeIn(z_text, z_2_text, z_3_text))

        self.wait(4)


def fade_out(scene: Scene):
    animations = []
    for mobject in scene.mobjects:
        animations.append(FadeOut(mobject))
    scene.play(*animations)


class CombinedScene(Scene):
    def construct(self):
        scenes = [ComplexNumberIntroduction, ImaginaryNumber, ComplexPlain, RealOperations, AdditionOperations, TrigonometricForm, Multiplication, Power]
        for scene in scenes:
            scene.construct(self)
            fade_out(self)


if __name__ == "__main__":
    from manim import config

    config.background_color = BLACK
    scene = CombinedScene()
    scene.render()
