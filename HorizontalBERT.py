from manim import *

class HorizontalBERT(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        # --- Creating HorizontalBERT Traditional --- #
        horizontal_boxes = [1, 2, 3, 4, 5]
        
        weight_1 = [MathTex(w).scale(0.5) for w in [r"\text{Input} \times " + "5", r"\text{Input} \times " + "4", r"\text{Input} \times " + "3", r"\text{Input} \times " + "2", r"\text{Input} \times " + "1"]]
        weight_2 = [MathTex(w).scale(0.5) for w in [r"\text{Calc 1 + }" + "9", r"\text{Calc 1 + }" + "6", r"\text{Calc 1 + }" + "4", r"\text{Calc 1 + }" + "9", r"\text{Calc 1 + }" + "8"]]
        weight_3 = [MathTex(w).scale(0.5) for w in [r"\dfrac{\text{Calc 2}}{7}", r"\dfrac{\text{Calc 2}}{2}", r"\dfrac{\text{Calc 2}}{1}", r"\dfrac{\text{Calc 2}}{2}", r"\dfrac{\text{Calc 2}}{12}"]]
        inputs_outputs = [MathTex(w).scale(0.5) for w in ["78", r"\frac{39}{2}", r"\frac{31}{6}", r"\frac{2}{3}", "0"]]

        set_1_colour = [MathTex(w).scale(0.5).set_color(MAROON) for w in [r"\dfrac{\text{Calc 2}}{12}", r"\text{Calc 1 + }" + "8", r"\text{Input} \times " + "1"]]
        set_2_colour = [MathTex(w).scale(0.5).set_color(GREEN) for w in [r"\dfrac{\text{Calc 2}}{2}", r"\text{Calc 1 + }" + "9", r"\text{Input} \times " + "2"]]
        set_3_colour = [MathTex(w).scale(0.5).set_color(YELLOW) for w in [r"\dfrac{\text{Calc 2}}{1}", r"\text{Calc 1 + }" + "4", r"\text{Input} \times " + "3"]]
        set_4_colour = [MathTex(w).scale(0.5).set_color(BLUE) for w in [r"\dfrac{\text{Calc 2}}{2}", r"\text{Calc 1 + }" + "6", r"\text{Input} \times " + "4"]]
        set_5_colour = [MathTex(w).scale(0.5).set_color(ORANGE) for w in [r"\dfrac{\text{Calc 2}}{7}", r"\text{Calc 1 + }" + "9", r"\text{Input} \times " + "5"]]

        point_t = Dot(1 * UP + 2 * RIGHT)
        point_u = Dot(1 * DOWN + 2 * LEFT)
        horizontal_vgroup = VGroup()
        box_dic = {}
        text_dic = {}
        colour_dic = {}


        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        # --- HorizontalBERT Traditional Animations --- #
     
        shift_count = -3.25
        camera_shift = -5.75
        
        for i, _ in enumerate(horizontal_boxes, start=1):
            
            input_horizontal = Text("Input: ", color= WHITE).scale(0.4).shift(0.8 * UP + 3.1 * LEFT)
            input_horizontal.shift(shift_count * RIGHT)
            
            calc_1_horizontal = Text("Calc 1: ", color= WHITE).scale(0.4).shift(0.8 * UP + 1.6 * LEFT)
            calc_1_horizontal.shift(shift_count * RIGHT)
            
            calc_2_horizontal = Text("Calc 2: ", color= WHITE).scale(0.4).shift(0.8 * DOWN + 1.6 * LEFT)
            calc_2_horizontal.shift(shift_count * RIGHT)

            calc_3_horizontal = Text("Calc 3: ", color= WHITE).scale(0.4).shift(0.8 * UP + 0.7 * RIGHT)
            calc_3_horizontal.shift(shift_count * RIGHT)

            arrow_1_horizontal = Arrow(buff= 0.05, start= 0.35 * UP + 3.65 * LEFT, end= 0.35 * UP + 2.3 * LEFT, stroke_width= 2, max_tip_length_to_length_ratio= 0.12)
            arrow_1_horizontal.shift(shift_count * RIGHT)
            arrow_2_horizontal = Arrow(buff= 0.05, start= 0.6 * UP + 1.25 * LEFT, end= 0.6 * DOWN + 1.25 * LEFT, stroke_width= 2, max_tip_length_to_length_ratio= 0.13)
            arrow_2_horizontal.shift(shift_count * RIGHT)
            arrow_3_horizontal = Arrow(buff= 0.05, start= 0.85 * DOWN + 0.2 * RIGHT, end= 0.6 * UP + 1.05 * RIGHT, stroke_width= 2, max_tip_length_to_length_ratio= 0.085)
            arrow_3_horizontal.shift(shift_count * RIGHT)


            weight_1_value = weight_1.pop().shift(0.6 * LEFT + 0.77 * UP)
            weight_1_value.shift(shift_count * RIGHT)

            weight_2_value = weight_2.pop().shift(0.54 * LEFT + 0.81 * DOWN)
            weight_2_value.shift(shift_count * RIGHT)

            weight_3_value = weight_3.pop().shift(1.6 * RIGHT + 0.8 * UP)
            weight_3_value.shift(shift_count * RIGHT)

            input_value = inputs_outputs.pop().shift(2.5 * LEFT + 0.8 * UP)
            input_value.shift(shift_count * RIGHT)

            box = SurroundingRectangle(point_t, point_u, color= WHITE, stroke_width= 2).shift(shift_count * RIGHT)
            
            
            horizontal_vgroup.add(box, arrow_1_horizontal, arrow_2_horizontal, arrow_3_horizontal, calc_1_horizontal, calc_2_horizontal, calc_3_horizontal, input_horizontal, weight_1_value, weight_2_value, weight_3_value, input_value)
            shift_count += 6
            camera_shift += 6
            box_dic[f"box_{i}"] = VGroup(box)
            text_dic[f"text_{i}"] = VGroup(arrow_1_horizontal, arrow_2_horizontal, arrow_3_horizontal, calc_1_horizontal, calc_2_horizontal, calc_3_horizontal, input_horizontal, input_value, weight_1_value, weight_2_value, weight_3_value)

            self.play(AnimationGroup(Create(arrow_1_horizontal), Create(input_horizontal), FadeIn(input_value), Create(calc_1_horizontal), FadeIn(weight_1_value), Create(arrow_2_horizontal), Create(calc_2_horizontal), FadeIn(weight_2_value), Create(arrow_3_horizontal), Create(calc_3_horizontal), FadeIn(weight_3_value), Create(box),
            lag_ratio= 0.5, run_time= 5)
            )
            self.play(self.camera.frame.animate.move_to(camera_shift * RIGHT))



        last_output = Text("Output: 57", color= WHITE).scale(0.4).shift(0.8 * UP + 23.8 * RIGHT)
        arrow_4_horizontal = Arrow(buff= 0.05, start= 0.35 * UP + 23.1 * RIGHT, end= 0.35 * UP + 24.45 * RIGHT, stroke_width= 2, max_tip_length_to_length_ratio= 0.12)
        self.play(Create(last_output), FadeIn(arrow_4_horizontal))
        horizontal_vgroup.add(arrow_4_horizontal, last_output)


        self.wait(1)
        self.play(self.camera.frame.animate.move_to(ORIGIN), run_time= 10)
        self.wait(1)

        
        # --- WAITING WAITING WAITING --- #

        # self.wait(20)


        # --- Changing Colour of Weight Values --- #
        
        shift_count = -3.25
        camera_shift = -5.75

        colour_list = [set_1_colour, set_2_colour, set_3_colour, set_4_colour, set_5_colour]
        for i, colour in enumerate(colour_list, start=1):

            weight_1_value_colour = colour.pop().shift(0.6 * LEFT + 0.77 * UP)
            weight_1_value_colour.shift(shift_count * RIGHT)

            weight_2_value_colour = colour.pop().shift(0.54 * LEFT + 0.81 * DOWN)
            weight_2_value_colour.shift(shift_count * RIGHT)

            weight_3_value_colour = colour.pop().shift(1.6 * RIGHT + 0.8 * UP)
            weight_3_value_colour.shift(shift_count * RIGHT)


            shift_count += 6
            camera_shift += 6
            colour_dic[f"colour_{i}"] = VGroup(weight_1_value_colour, weight_2_value_colour, weight_3_value_colour)
            text_dic[f"text_{i}"].add(weight_1_value_colour, weight_2_value_colour, weight_3_value_colour)
            horizontal_vgroup.add(weight_1_value_colour, weight_2_value_colour, weight_3_value_colour)

            self.play(AnimationGroup(FadeIn(weight_1_value_colour, weight_2_value_colour, weight_3_value_colour),
            lag_ratio= 0.75, run_time= 1.5))

            self.play(self.camera.frame.animate.move_to(camera_shift * RIGHT))



        # --- WAITING WAITING WAITING --- #

        # self.wait(20)


        # --- Compressing HorizontalBERT Traditional --- #

        self.wait(1)
        
        self.play(AnimationGroup(self.camera.frame.animate.move_to(box_dic["box_3"]).set(width= horizontal_vgroup.width + 2), rate_func= linear, run_time= 7))

        self.wait(1)

        self.play(FadeOut(arrow_4_horizontal), FadeOut(last_output))

        for i in range (5, 0, -1):
            next_box = box_dic[f"box_{i}"]
            next_text = text_dic[f"text_{i}"]
            next_colour = colour_dic[f"colour_{i}"]
            temp = VGroup(next_box, next_text, next_colour)

            if i > 1:
                self.play(temp.animate.move_to(box_dic[f"box_{i-1}"].get_center() + 0.7 * LEFT), rate_func= smoothstep, run_time= 1.75)

            if i == 1:
                break

            self.remove(next_box, next_text, next_colour)

        self.play(Restore(self.camera.frame), run_time= 5)


        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        # --- Creating CompressedBERT --- #

        lpddr_text = Text("LPDDR", color= WHITE).scale(1.5).shift(2 * UP + 3 * LEFT)