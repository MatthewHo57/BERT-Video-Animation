from manim import *

class BoxCompression(Scene):
    def construct(self):
        # Define the number of boxes
        num_boxes = 5
        box_width = 2
        spacing = 2.5  # Initial spacing between boxes
        
        # Create boxes and text labels
        boxes = []
        texts = []
        for i in range(num_boxes):
            box = Square(side_length=box_width, color=BLUE).shift(RIGHT * (i * spacing))
            text = Text(f"Box {i+1}", font_size=24).move_to(box.get_center())
            boxes.append(box)
            texts.append(text)
            self.add(box, text)
        
        # Animate compression
        animations = []
        for i in range(1, num_boxes):
            animations.append(
                AnimationGroup(
                    boxes[i].animate.move_to(boxes[0].get_center()),  # Move to first box
                    FadeOut(texts[i]),  # Fade out text
                    lag_ratio=0.5
                )
            )
        
        # Play the animation sequentially
        self.play(*animations, run_time=4)
        
        # Keep the final state
        self.wait(2)
