from manim import *

class ZoomOutToBackground(MovingCameraScene):
    def construct(self):
        # Your pre-existing animation content
        dot = Dot().scale(2)
        label = Text("This is the main animation", font_size=24).next_to(dot, DOWN)

        self.add(dot, label)
        self.wait(1)

        # Simulate some animation to focus on the center
        self.play(dot.animate.shift(LEFT * 2), run_time=1)
        self.wait(0.5)

        # Load the background image
        background = ImageMobject("speedAI240_lowres_bkg_light (1).jpg")  # Replace with your actual image path
        background.scale_to_fit_height(8)
        background.set_z_index(-10)  # Send to the back
        background.scale(5)
        background.set_opacity(0)  # Initially invisible
        self.add(background)

        # Zoom out effect with camera frame scaling
        self.play(FadeOut(dot), FadeOut(label),  # Fade out the main elements
            self.camera.frame.animate.scale(4.5),  # Adjust scale to zoom out
            background.animate.set_opacity(1),  # Fade in the background
            run_time=3

        )

        self.wait(2)
