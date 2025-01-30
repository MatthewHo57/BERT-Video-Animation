from manim import *

class TestScene(Scene):
    def construct(self):
        # Create text object
        text = Text("Hello, Manim!")
        
        # Animate text appearance
        self.play(Write(text))
        
        # Wait for 2 seconds
        self.wait(2)
        
        # Fade out
        self.play(FadeOut(text))