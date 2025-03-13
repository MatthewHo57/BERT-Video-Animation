from manim import *

class HorizontalBERT(MovingCameraScene):
    def construct(self):

        # --- Creating HorizontalBERT Traditional --- #
        horizontal_boxes = [1, 2, 3, 4, 5]
        
        weight_1 = [MathTex(w).scale(0.5) for w in [r"\text{Input} \times " + "5", r"\text{Input} \times " + "4", r"\text{Input} \times " + "3", r"\text{Input} \times " + "2", r"\text{Input} \times " + "1"]]
        weight_2 = [MathTex(w).scale(0.5) for w in [r"\text{Calc 1 + }" + "9", r"\text{Calc 1 + }" + "6", r"\text{Calc 1 + }" + "4", r"\text{Calc 1 + }" + "9", r"\text{Calc 1 + }" + "8"]]
        weight_3 = [MathTex(w).scale(0.5) for w in [r"\dfrac{\text{Calc 2}}{7}", r"\dfrac{\text{Calc 2}}{2}", r"\dfrac{\text{Calc 2}}{1}", r"\dfrac{\text{Calc 2}}{2}", r"\dfrac{\text{Calc 2}}{12}"]]
        inputs_outputs = [MathTex(w).scale(0.5) for w in ["78", r"\frac{39}{2}", r"\frac{31}{6}", r"\frac{2}{3}", "0"]]

        weight_1_colour = [MathTex(w).scale(0.5).set_color(RED) for w in [r"\dfrac{\text{Calc 2}}{12}", r"\text{Calc 1 + }" + "8", r"\text{Input} \times " + "1"]]
        weight_2_colour = [MathTex(w).scale(0.5).set_color(GREEN) for w in [r"\dfrac{\text{Calc 2}}{2}", r"\text{Calc 1 + }" + "9", r"\text{Input} \times " + "2"]]
        weight_3_colour = [MathTex(w).scale(0.5).set_color(YELLOW) for w in [r"\dfrac{\text{Calc 2}}{1}", r"\text{Calc 1 + }" + "4", r"\text{Input} \times " + "3"]]
        weight_4_colour = [MathTex(w).scale(0.5).set_color(BLUE) for w in [r"\dfrac{\text{Calc 2}}{2}", r"\text{Calc 1 + }" + "6", r"\text{Input} \times " + "4"]]
        weight_5_colour = [MathTex(w).scale(0.5).set_color(ORANGE) for w in [r"\dfrac{\text{Calc 2}}{7}", r"\text{Calc 1 + }" + "9", r"\text{Input} \times " + "5"]]

        point_r = Dot(1 * UP + 2 * RIGHT)
        point_s = Dot(1 * DOWN + 2 * LEFT)
        horizontal_vgroup = VGroup()
        box_dic = {}



        # --- Playing Animations --- #
     
        shift_count = -3.25
        
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
            arrow_2_horizontal = Arrow(buff= 0.05, start= 0.6 * UP + 1.25 * LEFT, end= 0.6 * DOWN + 1.25 * LEFT, stroke_width= 2, max_tip_length_to_length_ratio= 0.12)
            arrow_2_horizontal.shift(shift_count * RIGHT)
            arrow_3_horizontal = Arrow(buff= 0.05, start= 0.85 * DOWN + 0.2 * RIGHT, end= 0.6 * UP + 1.05 * RIGHT, stroke_width= 2, max_tip_length_to_length_ratio= 0.08)
            arrow_3_horizontal.shift(shift_count * RIGHT)


            weight_1_value = weight_1.pop().shift(0.6 * LEFT + 0.77 * UP)
            weight_1_value.shift(shift_count * RIGHT)

            weight_2_value = weight_2.pop().shift(0.54 * LEFT + 0.81 * DOWN)
            weight_2_value.shift(shift_count * RIGHT)

            weight_3_value = weight_3.pop().shift(1.6 * RIGHT + 0.8 * UP)
            weight_3_value.shift(shift_count * RIGHT)

            input_value = inputs_outputs.pop().shift(2.5 * LEFT + 0.8 * UP)
            input_value.shift(shift_count * RIGHT)

            box = SurroundingRectangle(point_r, point_s, color= WHITE, stroke_width= 2).shift(shift_count * RIGHT)
            
            
            horizontal_vgroup.add(box, arrow_1_horizontal, arrow_2_horizontal, arrow_3_horizontal, calc_1_horizontal, calc_2_horizontal, calc_3_horizontal, input_horizontal, weight_1_value, weight_2_value, weight_3_value, input_value)
            shift_count += 6
            box_dic[f"box_{i}"] = VGroup(box, arrow_1_horizontal, arrow_2_horizontal, arrow_3_horizontal, calc_1_horizontal, calc_2_horizontal, calc_3_horizontal, input_horizontal, weight_1_value, weight_2_value, weight_3_value, input_value)


            self.play(AnimationGroup(Create(arrow_1_horizontal), Create(input_horizontal), FadeIn(input_value), Create(calc_1_horizontal), FadeIn(weight_1_value), Create(arrow_2_horizontal), Create(calc_2_horizontal), FadeIn(weight_2_value), Create(arrow_3_horizontal), Create(calc_3_horizontal), FadeIn(weight_3_value), Create(box),
            lag_ratio= 0.5, run_time= 5)
            )
            self.play(self.camera.frame.animate.move_to(shift_count * RIGHT))



        last_output = Text("Output: 57", color= WHITE).scale(0.4).shift(0.8 * UP + 23.8 * RIGHT)
        arrow_4_horizontal = Arrow(buff= 0.05, start= 0.35 * UP + 23.1 * RIGHT, end= 0.35 * UP + 24.45 * RIGHT, stroke_width= 2, max_tip_length_to_length_ratio= 0.12)
        self.play(Create(last_output), Create(arrow_4_horizontal))
        horizontal_vgroup.add(arrow_4_horizontal, last_output)


        self.wait(1)
        self.play(self.camera.frame.animate.move_to(ORIGIN), run_time= 10)
        self.wait(1)

        
        # --- WAITING WAITING WAITING --- #

        # self.wait(20)


        # --- Changing Colour of Weight Values --- #
        
        shift_count = -3.25

        colour_list = [weight_1_colour, weight_2_colour, weight_3_colour, weight_4_colour, weight_5_colour]
        for colour_list in colour_list:

            weight_1_value = colour_list.pop().shift(0.6 * LEFT + 0.77 * UP)
            weight_1_value.shift(shift_count * RIGHT)

            weight_2_value = colour_list.pop().shift(0.54 * LEFT + 0.81 * DOWN)
            weight_2_value.shift(shift_count * RIGHT)

            weight_3_value = colour_list.pop().shift(1.6 * RIGHT + 0.8 * UP)
            weight_3_value.shift(shift_count * RIGHT)


            shift_count += 6
            horizontal_vgroup.add(weight_1_value, weight_2_value, weight_3_value)

            self.play(AnimationGroup(FadeIn(weight_1_value, weight_2_value, weight_3_value),
            lag_ratio= 0.75, run_time= 1.5))

            self.play(self.camera.frame.animate.move_to(shift_count * RIGHT))




        # --- WAITING WAITING WAITING --- #

        # self.wait(20)




        self.wait(1)
        self.play(box_dic["box_5"].animate.shift(24 * LEFT), self.camera.frame.animate.move_to(ORIGIN), rate_func= linear, run_time= 15)
        self.wait(1)

        
        