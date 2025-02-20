from manim import *

class CompressingBERT(Scene):
    def construct(self):
        # Start position of the first square
        start_x = -6  
        y_pos = 0  
        square_size = 1  # Size of the square
        num_squares = 12  # Total squares to generate
        shift_right = 2  # Distance between squares
        camera_shift = 2  # Camera movement per step

        # Create a list to hold squares
        squares = []
        
        # Create squares one by one
        for i in range(num_squares):
            new_square = Square(side_length=square_size, color=BLUE).move_to([start_x + i * shift_right, y_pos, 0])
            squares.append(new_square)
            
            # Add animation for square appearance
            self.play(FadeIn(new_square), run_time=0.5)

            # Start shifting camera after the 10th square
            if i >= 10:
                self.play(self.camera.frame.animate.shift(RIGHT * camera_shift), run_time=0.5)

        # Hold the final frame
        self.wait(2)
