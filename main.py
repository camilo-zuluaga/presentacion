from manim import *

from manim_slides import Slide

class RocketIntro(Slide):
    def construct(self):

        # Crear el título
        title = Text("La Dinámica de un Cohete", font_size=70, color="#FF7171").to_edge(UP)
        # Crear el subtítulo
        subtitle = Text("Ecuaciones Diferenciales", font_size=50).next_to(title, DOWN)

        group = VGroup(title, subtitle).arrange(DOWN, buff=0.5).move_to(ORIGIN)

        self.play(Write(title, color="#FF7171"))
        self.play(Write(subtitle))


        Tema1 = Tex("Fundamentos de un Cohete", font_size=70)
        Tema1_1 = Tex("Definición", font_size=70)

        self.next_slide()
        self.play(Unwrite(title))
        self.play(Unwrite(subtitle))
        self.wait(1)
        self.play(Write(Tema1))

        self.next_slide()
        self.play(Transform(Tema1, Tema1_1.to_edge(UP)))


        rectangle = Rectangle(width=6, height=2)
        rectangle.set_fill("#EBEBEB", opacity=0.2)

        # Position the rectangle in the center
        rectangle.move_to(ORIGIN)

        # Create an arrow starting from the right side of the rectangle
        arrow_right = Arrow(
            start=rectangle.get_right(),
            end=rectangle.get_right() + RIGHT * 2,
            color="#FF54CB",
        )

        arrow_left = Arrow(
            start=rectangle.get_left(),
            end=rectangle.get_left() + LEFT * 2,
            color="#2D86FF",
        )

        # Create text labels
        text_acceleration = Tex("Aceleración", color="#FF54CB").scale(0.8)
        text_mass = Tex("Masa", color="#2D86FF").scale(0.8)

        # Position the text labels
        text_acceleration.next_to(arrow_right, DOWN).shift(RIGHT * 0.5)
        text_mass.next_to(arrow_left, UP)

        self.next_slide()
        self.play(FadeIn(rectangle))

        self.next_slide()
        self.play(GrowArrow(arrow_left))
        self.play(FadeIn(text_mass))

        self.next_slide()
        self.play(GrowArrow(arrow_right))
        self.play(FadeIn(text_acceleration))

        circle = Circle(radius=2, color=ORANGE, fill_opacity=1)
        
        # Crear el triángulo
        triangle = Triangle(color=ORANGE, fill_opacity=1)
        triangle.scale(0.5).next_to(circle, DOWN, buff=0)
        
        # Agrupar las formas
        balloon = VGroup(circle, triangle).move_to(ORIGIN)
        balloon.scale(0.8)
        # Mostrar las formas
        arrow = Arrow(start=balloon.get_bottom(), end=balloon.get_bottom() + DOWN, buff=1, color="#FF4A4A")

        self.next_slide()
        self.play(FadeOut(rectangle), FadeOut(arrow_left), FadeOut(arrow_right), FadeOut(text_mass), FadeOut(text_acceleration))
        self.play(FadeOut(Tema1))
        self.wait(0.5)
        self.play(FadeIn(balloon))

        self.next_slide()
        self.play(GrowArrow(arrow))

        self.next_slide()
        self.play(arrow.animate.shift(DOWN * 3), balloon.animate.shift(UP * 7))
        self.play(FadeOut(balloon))
        self.play(FadeOut(arrow))

        Tema2 = Tex("Diseño del Cohete", font_size=70)
        self.next_slide()
        self.play(Write(Tema2))

        rocket = SVGMobject("imagenes/electron_rocket.svg", height=7)
        rectangle2 = Rectangle(width=1, height=4.3, color=YELLOW)
        rectangle2.set_stroke(width=2)

        rectangle3 = Rectangle(width=1, height=1.5, color=YELLOW)
        rectangle3.set_stroke(width=2)

        payload = [-4, 2.9, 0] # x, y, z 
        engine = [-4, -3, 0]

        cuerpo = Tex("Cuerpo", font_size=50).next_to(rectangle2, RIGHT * 2)
        carga = Tex("Carga", font_size=50).next_to(rectangle3, RIGHT * 2)
        motores = Tex("Motores", font_size=50).next_to(rectangle3, RIGHT * 2)

        self.next_slide()
        self.play(Unwrite(Tema2))
        self.play(Write(rocket))
        self.wait(0.8)
        self.play(rocket.animate.shift(LEFT * 4))

        self.next_slide()
        self.play(Write(rectangle2))
        self.play(rectangle2.animate.shift(LEFT * 4))
        self.play(Write(cuerpo))

        self.next_slide()
        self.play(Transform(rectangle2, rectangle3.move_to(payload)))
        self.play(Transform(cuerpo, carga))

        self.next_slide()
        self.play(Transform(rectangle2, rectangle3.move_to(engine)))
        self.play(Transform(cuerpo, motores))

        self.next_slide()
        self.play(FadeOut(rectangle2), FadeOut(cuerpo))
        self.play(rocket.animate.shift(UP * 8))
        self.play(FadeOut(rocket))

        Tema2 = Tex("Leyes de Newton", font_size=70)
        primera = Tex("Primera Ley", font_size=70)
        segunda = Tex("Segunda Ley", font_size=70)
        segundaDef = Tex(r"La aceleración de un objeto es directamente proporcional a\\ la fuerza neta que actúa sobre él e inversamente\\ proporcional a la masa del objeto", font_size=50)
        segundaDef.shift(UP * 1)
        tercera = Tex("Tercera Ley", font_size=70)
        terceraDef = Tex(r"Por cada acción, hay una reacción igual y opuesta", font_size=50)
        terceraDef.shift(UP * 2)

        self.next_slide()
        self.play(Write(Tema2))

        self.next_slide()
        self.play(Transform(Tema2, primera.to_edge(UP)))

        rocket = SVGMobject("imagenes/electron_rocket.svg", height=5)
        line = Line(
            start=rocket.get_bottom() + DOWN * 0 + LEFT * 2,
            end=rocket.get_bottom() + DOWN * 0 + RIGHT * 2,
            color=WHITE
        )

        arrowG = Arrow(start=rocket.get_left() + LEFT*0.5 + UP * 2, end=rocket.get_left() + LEFT * 0.5 + DOWN * 0.4, color=RED_C, buff=0.5)
        arrowE = Arrow(start=rocket.get_left() + LEFT * 0.5 + DOWN * 2, end=rocket.get_left() +LEFT*0.5+ UP * 0.4, color=BLUE_C, buff=0.5)
        arrowI = MathTex(r"\Downarrow", font_size=70)
        inercia = Tex("Inercia", font_size=70)

        arrowI.next_to(inercia, UP).shift(UP * 0.1)

        self.next_slide()
        self.play(Write(rocket), Write(line))
        self.play(GrowArrow(arrowG))

        self.next_slide()
        self.play(GrowArrow(arrowE))

        self.next_slide()
        self.play(FadeOut(rocket), FadeOut(arrowG), FadeOut(arrowE), FadeOut(line))
        self.play(Write(inercia), Write(arrowI))


        Fnet = MathTex("F_{net}", font_size=70)
        Fnet.shift(DOWN * 1 + LEFT * 1)
        a = MathTex("a", font_size=70)
        a.shift(DOWN * 1 + RIGHT * 1)
        m = MathTex("m", font_size=70)
        m.shift(DOWN * 1 + LEFT * 1)

        Fform = MathTex("F_{net} = ma", font_size=70)
        Fform.shift(DOWN * 1)
        framebox1 = SurroundingRectangle(Fform, buff = .1)

        Fnetarrow = Arrow(start=Fnet.get_left() + LEFT * 0.3 + UP * 0.5, end=Fnet.get_left() + LEFT * 0.3 + DOWN * 0.5, color=WHITE)
        Aarrow = Arrow(start=a.get_left() + LEFT * 0.3 + UP * 0.5, end=a.get_left() + LEFT * 0.3 + DOWN * 0.5, color=WHITE)

        Fnetarrow2 = Arrow(start=Fnet.get_left() + LEFT * 0.3 + DOWN * 0.5, end=Fnet.get_left() + LEFT * 0.3 + UP * 0.5, color=WHITE)
        Aarrow2 = Arrow(start=a.get_left() + LEFT * 0.3 + DOWN * 0.5, end=a.get_left() + LEFT * 0.3 + UP * 0.5, color=WHITE)

        marrow = Arrow(start=m.get_left() + LEFT * 0.3 + UP * 0.5, end=m.get_left() + LEFT * 0.3 + DOWN * 0.5, color=WHITE)
        marrow2 = Arrow(start=m.get_left() + LEFT * 0.3 + DOWN * 0.5, end=m.get_left() + LEFT * 0.3 + UP * 0.5, color=WHITE)

        self.next_slide()
        self.play(FadeOut(inercia), FadeOut(arrowI))
        self.play(Transform(Tema2, segunda.shift(UP * 3.2)))
        self.play(Write(segundaDef))

        self.next_slide()
        self.play(Write(Fnet), Write(a))

        self.next_slide()
        self.play(GrowArrow(Fnetarrow2))

        self.next_slide()
        self.play(GrowArrow(Aarrow2))

        self.next_slide()
        self.play(FadeOut(Fnetarrow2))
        self.play(GrowArrow(Fnetarrow))

        self.next_slide()
        self.play(FadeOut(Aarrow2))
        self.play(GrowArrow(Aarrow))

        self.next_slide()
        self.play(FadeOut(Fnetarrow), FadeOut(Aarrow))
        self.play(Transform(Fnet, m))

        self.next_slide()
        self.play(GrowArrow(marrow2))
        self.play(GrowArrow(Aarrow))

        self.next_slide()
        self.play(FadeOut(marrow2), FadeOut(Aarrow))
        self.play(GrowArrow(marrow))
        self.play(GrowArrow(Aarrow2))

        self.next_slide()
        self.play(FadeOut(marrow), FadeOut(Aarrow2), FadeOut(Fnet), FadeOut(a))
        self.play(Write(Fform), Create(framebox1))

        rocket = SVGMobject("imagenes/electron_rocket.svg", height=3)
        arrow = Arrow(start=rocket.get_left() + LEFT * 0.5 + UP * 1, end=rocket.get_left() + LEFT*0.5 + DOWN * 2, color=WHITE, buff = 0.5)
        line = Line(
            start=rocket.get_bottom() + DOWN * 0 + LEFT * 2,
            end=rocket.get_bottom() + DOWN * 0 + RIGHT * 2,
            color=WHITE
        )

        arrow2 = Arrow(start=rocket.get_left() + LEFT * 0.5 + DOWN * 4, end=rocket.get_left() +LEFT*0.5+ DOWN * 1 + UP* 0, color=RED_C, buff=0.5)


        self.next_slide()
        self.play(FadeOut(Fform), FadeOut(framebox1), FadeOut(segundaDef))
        self.play(Transform(Tema2, tercera.shift(UP * 3.2)))
        self.play(Write(terceraDef))
        self.play(Write(rocket), Write(line))

        self.next_slide()
        self.play(GrowArrow(arrow))

        self.next_slide()
        self.play(GrowArrow(arrow2))

        rocket_two = SVGMobject("imagenes/drag.svg", height=4)
        rocket_two.shift(DOWN * 1)
        rocket_two.rotate(PI/-10)
        Tema3 = Tex("Resistencia del Aire", font_size=70)

        Tema3_1 = Tex("Fuerza de Arrastre", font_size=70)
        Temp = MathTex("D", font_size=50, color=YELLOW_C)
        
        Tema3_2 = Tex("Máxima Presión Dinámica", font_size=70)
        Temp2 = MathTex("q", font_size=70, color=YELLOW_C)
        maxqform = MathTex(r"q = \frac{1}{2} \rho v^2", font_size=70)
        maxqform.shift(RIGHT * 2)

        rocketMAXQ = ImageMobject("imagenes/maxq.png", scale_to_resolution=2080)
        rocketMAXQ.set_height(6)
        rocketMAXQ.shift(DOWN * 1)

        DragForce = MathTex(r"D = \frac{1}{2} \rho v^2 A C_d", font_size=70)
        framebox2 = SurroundingRectangle(DragForce, buff = .1)
        framebox3 = SurroundingRectangle(maxqform, buff = .1)

        arrowDrag = Arrow(start=UP, end=DOWN, color=YELLOW_C, buff=0.5)
        arrowDrag.next_to(rocket_two, UP * 1.5 + RIGHT * 1.5,buff=0.1)
        arrowDrag.rotate(PI / -9.3, about_point=arrowDrag.get_start())

        self.next_slide()
        self.play(rocket.animate.shift(UP * 9))
        self.play(FadeOut(rocket), FadeOut(line), FadeOut(arrow), FadeOut(arrow2), FadeOut(Tema2), FadeOut(terceraDef))

        self.next_slide()
        self.play(Write(Tema3))
        self.play(Tema3.animate.shift(UP * 3.2))
        self.wait(0.5)
        self.play(Transform(Tema3, Tema3_1.shift(UP * 3.2)))

        self.next_slide()
        self.play(Write(rocket_two))
        self.play(GrowArrow(arrowDrag))
        self.play(Write(Temp.shift(UP * 2 + RIGHT * 1.3)))

        self.next_slide()
        self.play(FadeOut(rocket_two), FadeOut(arrowDrag))
        self.play(Temp.animate.move_to(ORIGIN))
        self.play(Transform(Temp, DragForce), Create(framebox2))
        self.wait(0.5)

        self.next_slide()
        self.play(FadeOut(Temp), FadeOut(DragForce), FadeOut(framebox2))
        self.play(Transform(Tema3, Tema3_2.shift(UP * 3.2)))
        self.play(FadeIn(rocketMAXQ.shift(UP * 0.7)))
        self.play(Write(Temp2.shift(RIGHT * 3)))

        self.next_slide()
        self.play(rocketMAXQ.animate.shift(LEFT*4), Temp2.animate.shift(LEFT*1))
        self.play(Transform(Temp2, maxqform), Create(framebox3))
        self.wait(0.5)

        Tema4 = Tex("Giro Gravitacional", font_size=70)
        rocket = SVGMobject("imagenes/electron_rocket.svg", height=5)

        self.next_slide()
        self.play(FadeOut(rocketMAXQ), FadeOut(Temp2), FadeOut(framebox3), FadeOut(Tema3))
        self.play(Write(Tema4))
        self.play(Tema4.animate.shift(UP * 3.2))

        arc = ArcBetweenPoints(
            start=[-6, 0, 0], 
            end=[0, 5, 0], 
            stroke_color=BLUE_C, 
            angle=-TAU/4,
            stroke_width=2,
            stroke_opacity=0
        )
        arc.shift(DOWN * 3.5 + RIGHT * 3)

        line = Line( start=arc.get_bottom() + DOWN * 0 + LEFT * 5, end=arc.get_bottom() + DOWN * 0 + RIGHT * 5, color=WHITE, stroke_width=2)
        dot = Dot(arc.get_start(), color=YELLOW_B)
        trajectory = TracedPath(dot.get_center, dissipating_time=0.5, stroke_opacity=[0, 1])

        start = 90
        x_var = Variable(start, "Angulo", var_type=Integer, num_decimal_places=3)

        # Change the color and font size of the variable
        x_var.label.set_color(YELLOW_C)
        x_var.shift(RIGHT*3)
        x_var.label.scale(0.7)
        x_var.label.shift(RIGHT*0.5)  
        x_var.value.scale(0.7)
        
        self.next_slide()
        self.play(Write(line))
        self.add(arc)

        self.next_slide()
        self.play(FadeIn(trajectory))
        self.play(Write(dot))
        self.play(Write(x_var))
        self.wait(0.5)
        
        self.next_slide()
        self.play(MoveAlongPath(dot, arc), x_var.tracker.animate.set_value(0),run_time=3, rate_func=linear)
        self.wait(1)

        self.next_slide()
        self.play(arc.animate.set_stroke(opacity=1.0), run_time=1, rate_func=linear)
        self.wait(1)

        Tema5 = Tex("Las Ecuaciones Diferenciales", font_size=70)

        self.next_slide()
        self.play(FadeOut(arc), FadeOut(line), FadeOut(dot), FadeOut(x_var))
        self.play(Transform(Tema4, Tema5.shift(UP*3.2)))

        gravity_turn = SVGMobject("imagenes/gravityturn.svg", height=10).shift(DOWN*2.5)

        self.next_slide()
        self.play(Write(gravity_turn), run_time=4, rate_func=linear)

        self.next_slide()
        self.play(Unwrite(gravity_turn), FadeOut(Tema4))

        second_law = MathTex("\\overrightarrow{F} = m\\overrightarrow{a}").scale(0.8)
        
        # Descomposición de la Aceleración
        acc_decomposition = VGroup(
            MathTex("\\overrightarrow{a} = a_t \\hat{t} + a_n \\hat{n}"),
            MathTex("a_t = \\frac{dv}{dt} \\qquad a_n = \\frac{v^2}{r} = v \\frac{v}{r} = v \\frac{d\\phi}{dt}")
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.8)
        
        total_force_components = VGroup(
            MathTex("\\overrightarrow{F} = \\overrightarrow{F}_{\\mathrm{grav}} + \\overrightarrow{F}_{\\mathrm{thrust}} + \\overrightarrow{F}_{\\mathrm{drag}}"),
            VGroup(
                MathTex("\\overrightarrow{F}_{\\mathrm{grav}} = -mg \\hat{r}"),
                MathTex("\\overrightarrow{F}_{\\mathrm{thrust}} = T \\hat{t}"),
                MathTex("\\overrightarrow{F}_{\\mathrm{drag}} = -\\frac{1}{2} \\rho AC_d v^2 \\hat{t}")
            ).arrange(RIGHT, aligned_edge=DOWN, buff=1)
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.8)
        
        # Dirección del Vector Unitario Radial
        radial_vector = MathTex(
            "\\hat{r} = \\cos(\\psi) \\hat{t} + \\sin(\\psi) \\hat{n}"
        ).scale(0.8)
        
        # Combinación de Fuerzas y Aceleración
        force_acc_combination = MathTex(
            "m\\left( \\frac{dv}{dt} \\hat{t} + v \\frac{d\\phi}{dt} \\hat{n} \\right) = T \\hat{t} - mg (\\cos(\\psi) \\hat{t} + \\sin(\\psi) \\hat{n}) - \\frac{1}{2} \\rho AC_d v^2 \\hat{t}"
        ).scale(0.6)
        
        # Separación de Componentes Tangenciales y Normales
        tangential_component = MathTex(
            "m \\frac{dv}{dt} = T - mg \\cos(\\psi) - \\frac{1}{2} \\rho AC_d v^2"
        ).scale(0.8)
        
        normal_component = MathTex(
            "m v \\frac{d\\phi}{dt} = -mg \\sin(\\psi)"
        ).scale(0.8)
        
        # Ecuaciones Diferenciales del Movimiento
        diff_eqs = VGroup(
            MathTex("\\frac{dv}{dt} = \\frac{T}{m} - g \\cos(\\psi) - \\frac{1}{2m} \\rho AC_d v^2"),
            MathTex("\\frac{d\\phi}{dt} = -\\frac{g}{v} \\sin(\\psi)")
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.8)
        
        # Ecuaciones adicionales para altura y ángulos
        additional_eqs = VGroup(
            MathTex("\\frac{dh}{dt} = v \\cos(\\psi)"),
            MathTex("\\frac{d\\theta}{dt} = \\frac{v \\sin(\\psi)}{R_e + h}"),
            MathTex("\\frac{d\\psi}{dt} = \\frac{d\\phi}{dt} - \\frac{d\\theta}{dt}")
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.8)
        
        # Posicionar los grupos de ecuaciones
        second_law.shift(UP * 2.5)
        acc_decomposition.next_to(second_law, DOWN, buff=0.4)
        total_force_components.next_to(acc_decomposition, DOWN, buff=0.4)
        radial_vector.shift(UP * 1.7)
        force_acc_combination.next_to(radial_vector, DOWN, buff=0.4)
        tangential_component.next_to(force_acc_combination, DOWN, buff=0.4)
        normal_component.next_to(tangential_component, DOWN, buff=0.4)
        diff_eqs.shift(UP * 1.6)
        additional_eqs.next_to(diff_eqs, DOWN, buff=0.4)

        focus = VGroup(diff_eqs, additional_eqs)
        framebox4 = SurroundingRectangle(focus, buff = .4)

        # Añadir todos los elementos a la escena
        self.next_slide()
        self.play(Write(second_law))
        self.play(Write(acc_decomposition))
        self.play(Write(total_force_components))
        self.wait(1)
        self.play(Unwrite(second_law), Unwrite(acc_decomposition), Unwrite(total_force_components))
        self.play(Write(radial_vector))
        self.play(Write(force_acc_combination))
        self.play(Write(tangential_component))
        self.play(Write(normal_component))
        self.wait(1)
        self.play(Unwrite(radial_vector), Unwrite(force_acc_combination), Unwrite(tangential_component), Unwrite(normal_component))
        self.play(Write(diff_eqs))
        self.play(Write(additional_eqs))
        self.wait(0.5)
        self.play(Create(framebox4))
        self.wait(1)

        Tema6 = Tex("Modelado Atmosférico", font_size=70)
        Tema6_1 = Tex("Densidad del Aire", font_size=70)
        Tema6_2 = Tex("Aceleración Gravitacional", font_size=70)
        tierra = SVGMobject("imagenes/earth.svg", height=6)
        tierra.shift(DOWN * 4.5)

        altitud = Arrow(start=tierra.get_top() + UP * 0.5 + LEFT * 0.5, end=UP * 2 + LEFT * 0.5, color=BLUE_C)
        densidad = Arrow(start=UP * 2 + RIGHT * 0.5, end=tierra.get_top() + UP * 0.5 + RIGHT * 0.5, color=RED_C)

        altitud_text = Tex("Altitud", font_size=50, color=BLUE_C).next_to(altitud, LEFT * 0.5)
        densidad_text = Tex("Densidad", font_size=50, color=RED_C).next_to(densidad, RIGHT * 0.5)

        densidad_formula = MathTex(r"\rho = \rho_0 e^{-\frac{h}{h_0}}", font_size=70)
        densidad_formula.shift(UP * 1.5)
        p = MathTex(r"\rho = 1.225 kg/m^3", font_size=50, color=RED_C)
        p.shift(LEFT * 3)
        h0 = MathTex(r"h_0 = 7.5 km", font_size=50, color=BLUE_C)
        h0.shift(RIGHT * 3)

        self.next_slide()
        self.play(Unwrite(diff_eqs), Unwrite(additional_eqs), Unwrite(framebox4))
        self.play(Write(Tema6))
        
        self.next_slide()
        self.play(Tema6.animate.shift(UP * 3.2))
        self.play(Transform(Tema6, Tema6_1.shift(UP * 3.2)))

        self.next_slide()
        self.play(Write(tierra))

        self.wait(0.5)
        self.play(GrowArrow(altitud), Write(altitud_text))
        self.wait(0.5)
        self.play(GrowArrow(densidad), Write(densidad_text))

        self.next_slide()
        self.play(FadeOut(altitud), FadeOut(altitud_text), FadeOut(densidad), FadeOut(densidad_text))
        self.play(Write(densidad_formula))
        self.play(Write(p), Write(h0))

        self.next_slide()
        self.play(Unwrite(p), Unwrite(h0), Unwrite(densidad_formula), Unwrite(tierra))
        self.play(Transform(Tema6, Tema6_2.shift(UP * 3.2)))

        dot2 = Dot(DOWN * 2 + RIGHT * 4.5, color=PINK)
        grav_formula = MathTex("g = \\frac{g_0}{(1 + \\frac{h}{R_e})^2}", font_size=70)
        grav_formula.shift(UP * 1.5 + RIGHT * 4)

        param = MathTex("(R_e = 6378 \\text{ km},\\ g_0 = 9.81 \\text{ m/s}^2)", font_size=40, color=PINK)
        param.shift(RIGHT * 4)

        ax = Axes(
            x_range=[0, 400, 100],
            y_range=[8.8, 9.9, 0.2],
            tips=False,
            x_axis_config={"numbers_to_include": np.arange(0, 401, 100)},
            y_axis_config={"numbers_to_include": np.arange(8.8, 9.9, 0.2)},
        )
        ax.scale(0.7).shift(LEFT * 2)

        altitud_label = Text("Altitud (km)").scale(0.5)
        altitud_label.next_to(ax.get_x_axis(), DOWN, buff=0.5)

        # x_min must be > 0 because log is undefined at 0.e)
        line = ax.plot_line_graph(
            x_values=[0, 400],
            y_values=[9.8, 8.8],
            line_color=PINK,
        )

        start_point = ax.c2p(8.8, 9.8)  # Convertir coordenadas a coordenadas del eje
        end_point = ax.c2p(400, 8.8)  # Convertir coordenadas a coordenadas del eje
        line = Line(start_point, end_point, color=PINK)

        self.next_slide()
        self.play(Create(ax), Write(altitud_label), run_time=2 , rate_func=linear)
        self.wait(1)

        self.next_slide()
        self.play(Write(dot2))
        self.wait(1)
        self.play(Create(line), dot2.animate.shift(UP * 3.7), run_time=3)
        self.wait(0.5)

        self.next_slide()
        self.play(Unwrite(dot2))
        self.play(Write(grav_formula))
        self.play(Write(param))

        Tema7 = Tex("Simulación", font_size=70)
        Tema7_1 = Tex("Modelado del Cohete", font_size=70)
        Tema7_2 = Tex("Código", font_size=70)
        Tema7_3 = Tex("Resultados", font_size=70)

        table = Table(
            [["900", "300"],
            ["10000","2000"],
            ["9", "1"], ["24.33167", "28.192"]],
            row_labels=[Text("Masa Estructural"), Text("Masa Propelante"), Text("N. Motores"), Text("Empuje del Motor")],
            col_labels=[Text("Primera Etapa"), Text("Segunda Etapa")],
            top_left_entry=Text("Parámetro"),
            include_outer_lines=True)
        table.scale(0.5)

        self.next_slide()
        self.play(Unwrite(grav_formula), Unwrite(param), Unwrite(ax), Unwrite(altitud_label), Unwrite(Tema6), Unwrite(line))
        self.play(Write(Tema7))

        tierra = SVGMobject("imagenes/earth.svg", height=2)
        circle = Circle(radius=2, color=BLUE_C, fill_opacity=0)
        dot3 = Dot(circle.get_start(), color=WHITE)

        label_info = Tex("Órbita: 184 Km", font_size=50, color=BLUE_C).shift(UP * 1.5)
        label_info2 = Tex("Diámetro: 1.2 m", font_size=50, color=YELLOW_C).shift(UP * 0.5)
        label_info3 = Tex("Payload: 300 Kg", font_size=50, color=RED_C).shift(DOWN * 0.3 )
        label_info4 = Tex("Altura: 1.4 Km, Ángulo: 10.489").shift(DOWN * 2)

        self.next_slide()
        self.play(Transform(Tema7, Tema7_1.shift(UP * 3.2)))
        self.play(table.create())

        self.next_slide()
        self.play(FadeOut(table))
        self.play(Write(tierra), Write(circle), Write(dot3))
        self.play(MoveAlongPath(dot3, circle), run_time=4, rate_func=linear)
        self.wait(0.5)

        self.next_slide()
        self.play(Unwrite(tierra), Unwrite(circle), Unwrite(dot3))
        self.play(Write(label_info))
        self.play(Write(label_info2))
        self.play(Write(label_info3))
        self.play(Write(label_info4))

        codigo1 = ImageMobject("imagenes/code1.png", scale_to_resolution=2080)
        codigo1.set_height(8)
        codigo1.shift(RIGHT*3.5)
        
        codigo2 = ImageMobject("imagenes/code2.png", scale_to_resolution=2080)
        codigo2.set_height(3)
        codigo2.shift(LEFT*3)

        codigo3 = ImageMobject("imagenes/code4.png", scale_to_resolution=2080)
        codigo3.set_height(8)
        codigo3.shift(RIGHT*3.5)
        
        codigo4 = ImageMobject("imagenes/code3.png", scale_to_resolution=2080)
        codigo4.set_height(3)
        codigo4.shift(LEFT*3)

        codigo5 = ImageMobject("imagenes/code5.png", scale_to_resolution=2080)
        codigo5.set_height(6.5)

        resultados = ImageMobject("imagenes/all_in_one.png", scale_to_resolution=4080)
        resultados.set_height(8.7)

        tierrat = ImageMobject("imagenes/trajectory.png", scale_to_resolution=2080)
        tierrat.set_height(8.5)

        self.next_slide()
        self.play(Unwrite(label_info), Unwrite(label_info2), Unwrite(label_info3), Unwrite(label_info4))
        self.play(Transform(Tema7, Tema7_2.shift(UP * 3.5).scale(0.5)))

        self.next_slide()
        self.play(FadeIn(codigo1), FadeIn(codigo2))

        self.next_slide()
        self.play(FadeOut(codigo1), FadeOut(codigo2))
        self.play(FadeIn(codigo3), FadeIn(codigo4))

        self.next_slide()
        self.play(FadeOut(codigo3), FadeOut(codigo4))
        self.play(FadeIn(codigo5))

        self.next_slide()
        self.play(FadeOut(codigo5), Transform(Tema7, Tema7_3.shift(UP * 3.2)))
        self.play(FadeIn(resultados))

        self.next_slide()
        self.play(FadeOut(resultados))
        self.play(Unwrite(Tema7))
        self.play(FadeIn(tierrat))