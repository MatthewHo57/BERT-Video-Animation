from manim import *

class TestScene(Scene):
    def construct(self):

        CPU_Square = Square()
        CPU_Square.rotate(PI/4)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Playing animation
   
        self.play(Create(CPU_Square))
        self.play(Rotate(CPU_Square, PI/4))