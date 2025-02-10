from manim import *

class VerticalBERT(Scene):
    def construct(self):
        output = Text("Output", font="Arial").scale(0.5)
        arrow_1 = Arrow(buff=0.5, start=2 * DOWN, end=0 * UP)
        
        
        softmax_text = Text("Softmax", font = "Arial", color=GREEN).scale(0.5).shift(2 * DOWN)
        softmax_box = Rectangle(color=WHITE)
        softmax_box.surround(softmax_text)
        softmax = VGroup(softmax_box, softmax_text)


        
    


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Playing animation
   
        self.add(output)
        self.add(arrow_1)
        self.add(softmax)
        #self.add(arrow_2)
