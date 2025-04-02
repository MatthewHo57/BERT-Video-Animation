from manim import *

class BoxCompression(MovingCameraScene):
    def construct(self):
        shift_count = 0
        horizontal_boxes = []  # Store box references
        texts = []  # Store text references

        # Creating boxes and texts
        for _ in range(5):  # Example with 5 boxes
            box = Square(side_length=1.5, color=BLUE).shift(shift_count * RIGHT)
            text = Text(f"{shift_count // 6 + 1}", font_size=24).move_to(box.get_center())

            self.add(box, text)  # Add to scene
            horizontal_boxes.append(box)
            texts.append(text)

            shift_count += 6  # Increment position

        self.wait(1)  # Pause before compression

        # Animation: Move all boxes left to overlap and fade out text
        animations = []
        for i in range(1, len(horizontal_boxes)):  
            animations.append(
                AnimationGroup(
                    horizontal_boxes[i].animate.move_to(horizontal_boxes[0].get_center()),  # Move box to first box
                    FadeOut(texts[i]),  # Fade out text
                    lag_ratio=0.5
                )
            )

        # Execute animation
        self.play(*animations, run_time=4)
        self.wait(2)  # Pause to see final compressed state
