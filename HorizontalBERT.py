from manim import *

class HorizontalBERT(Scene):
    def construct(self):
        # Create 10 squares, each shifted 1 unit to the right
        squares = VGroup(*[Square().shift(i * RIGHT) for i in range(10)])
        
        # Animate the creation of the squares with a staggered effect.
        self.play(AnimationGroup(*[Create(square) for square in squares], lag_ratio=0.2))
        
        # Animate a camera shift to the right so the right-most square is visible.
        # This moves the viewport such that squares on the left will be off-screen.
        self.play(self.camera.frame.animate.shift(5 * RIGHT), run_time=2)
        
        self.wait(1)