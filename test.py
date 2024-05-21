from manim import *

class Test(Scene):
    def construct(self):
        codigo1 = ImageMobject("imagenes/code4.png", scale_to_resolution=2080)
        codigo1.set_height(8)
        codigo1.shift(RIGHT*3.5)
        
        codigo2 = ImageMobject("imagenes/code3.png", scale_to_resolution=2080)
        codigo2.set_height(3)
        codigo2.shift(LEFT*3)
        self.wait(1)

        self.play(FadeIn(codigo1), FadeIn(codigo2))