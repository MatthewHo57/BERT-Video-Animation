from manim import *

class HorizontalBERT(Scene):
    def construct(self):

        # --- Creating HorizontalBERT Traditional --- #
        horizontal_boxes = [1, 2, 3, 4, 5]
        
        weight_1 = [MathTex(w).scale(0.5) for w in [r"\text{Input}" r"\times" "5", r"\text{Input}" r"\times" "4", r"\text{Input}" r"\times" "3", r"\text{Input}" r"\times" "2", r"\text{Input}" r"\times" "1"]]
        weight_2 = [MathTex(w).scale(0.5) for w in [r"\text{Calc 1 + }" "9", r"\text{Calc 1 + }" "6", r"\text{Calc 1 + }" "4", r"\text{Calc 1 + }" "9", r"\text{Calc 1 + }" "8"]]
        weight_3 = [MathTex(w).scale(0.5) for w in [r"\dfrac{\text{Calc 2}}{7}", r"\dfrac{\text{Calc 2}}{2}", r"\dfrac{\text{Calc 2}}{1}", r"\dfrac{\text{Calc 2}}{2}", r"\dfrac{\text{Calc 2}}{12}"]]
        inputs_outputs = [MathTex(w).scale(0.5) for w in ["57", "78", r"\frac{39}{2}", r"\frac{31}{6}", r"\frac{2}{3}", "0"]]

        

        # --- Creating HorizontalBERT Prototyping --- #
        # shift_count = -3.5
        # point_r = Dot(1 * UP + 1.5 * RIGHT)
        # point_s = Dot(1 * DOWN + 1.5 * LEFT)


        # for box in horizontal_boxes:
            
        #     input_horizontal = Text("Input: ", font= "Arial", color= WHITE).scale(0.4).shift(0.9 * UP + 2.8 * LEFT)
        #     self.add(input_horizontal)
        #     input_horizontal.shift(shift_count * RIGHT)

        #     calc_1_horizontal = Text("Calc 1: ", font= "Arial", color= WHITE).scale(0.4).shift(0.85 * UP + 1.2 * LEFT)
        #     self.add(calc_1_horizontal)
        #     calc_1_horizontal.shift(shift_count * RIGHT)
        #     calc_2_horizontal = Text("Calc 2: ", font= "Arial", color= WHITE).scale(0.4).shift(0.85 * DOWN + 1.2 * LEFT)
        #     self.add(calc_2_horizontal)
        #     calc_2_horizontal.shift(shift_count * RIGHT)
        #     calc_3_horizontal = Text("Calc 3: ", font= "Arial", color= WHITE).scale(0.4).shift(0.85 * UP + 0.5 * RIGHT)
        #     self.add(calc_3_horizontal)
        #     calc_3_horizontal.shift(shift_count * RIGHT)

        #     arrow_1_horizontal = Arrow(buff= 0.05, start= 0.5 * UP + 3 * LEFT, end= 0.5 * UP + 1.8 * LEFT, stroke_width= 2, max_tip_length_to_length_ratio=0.12)
        #     arrow_1_horizontal.shift(shift_count * RIGHT)
        #     self.add(arrow_1_horizontal)
        #     arrow_2_horizontal = Arrow(buff= 0.05, start= 0.65 * UP + 1 * LEFT, end= 0.65 * DOWN + 1 * LEFT, stroke_width= 2, max_tip_length_to_length_ratio=0.12)
        #     arrow_2_horizontal.shift(shift_count * RIGHT)
        #     self.add(arrow_2_horizontal)
        #     arrow_3_horizontal = Arrow(buff= 0.05, start= 0.65 * DOWN + 0.7 * LEFT, end= 0.65 * UP + 0.7 * RIGHT, stroke_width= 2, max_tip_length_to_length_ratio=0.08)
        #     arrow_3_horizontal.shift(shift_count * RIGHT)
        #     self.add(arrow_3_horizontal)


            

        #     weight_1_value = weight_1.pop().shift(0.5 * LEFT + 0.84 * UP)
        #     weight_1_value.shift(shift_count * RIGHT)
        #     self.add(weight_1_value)

        #     weight_2_value = weight_2.pop().shift(0.45 * LEFT + 0.85 * DOWN)
        #     weight_2_value.shift(shift_count * RIGHT)
        #     self.add(weight_2_value)

        #     weight_3_value = weight_3.pop().shift(1.1 * RIGHT + 0.85 * UP)
        #     weight_3_value.shift(shift_count * RIGHT)
        #     self.add(weight_3_value)

        #     input_value = inputs_outputs.pop().shift(2.3 * LEFT + 0.85 * UP)
        #     input_value.shift(shift_count * RIGHT)
        #     self.add(input_value)

        #     box = SurroundingRectangle(point_r, point_s, color= WHITE, stroke_width= 2).shift(shift_count * RIGHT)
        #     self.add(box)

        #     shift_count += 7
    


        # --- Playing Animations --- #
     
        shift_count = -3
        point_r = Dot(1 * UP + 2 * RIGHT)
        point_s = Dot(1 * DOWN + 2 * LEFT)
        horizontal_vgroup = VGroup()

        for box in horizontal_boxes:
            

            input_horizontal = Text("Input: ", font= "Arial", color= WHITE).scale(0.4).shift(0.8 * UP + 2.8 * LEFT)
            self.add(input_horizontal)
            input_horizontal.shift(shift_count * RIGHT)

            calc_1_horizontal = Text("Calc 1: ", font= "Arial", color= WHITE).scale(0.4).shift(0.8 * UP + 1.6 * LEFT)
            self.add(calc_1_horizontal)
            calc_1_horizontal.shift(shift_count * RIGHT)
            calc_2_horizontal = Text("Calc 2: ", font= "Arial", color= WHITE).scale(0.4).shift(0.8 * DOWN + 1.6 * LEFT)
            self.add(calc_2_horizontal)
            calc_2_horizontal.shift(shift_count * RIGHT)
            calc_3_horizontal = Text("Calc 3: ", font= "Arial", color= WHITE).scale(0.4).shift(0.8 * UP + 0.7 * RIGHT)
            self.add(calc_3_horizontal)
            calc_3_horizontal.shift(shift_count * RIGHT)

            arrow_1_horizontal = Arrow(buff= 0.05, start= 0.5 * UP + 3.1 * LEFT, end= 0.5 * UP + 1.9 * LEFT, stroke_width= 2, max_tip_length_to_length_ratio=0.12)
            arrow_1_horizontal.shift(shift_count * RIGHT)
            self.add(arrow_1_horizontal)
            arrow_2_horizontal = Arrow(buff= 0.05, start= 0.65 * UP + 1 * LEFT, end= 0.65 * DOWN + 1 * LEFT, stroke_width= 2, max_tip_length_to_length_ratio=0.12)
            arrow_2_horizontal.shift(shift_count * RIGHT)
            self.add(arrow_2_horizontal)
            arrow_3_horizontal = Arrow(buff= 0.05, start= 0.65 * DOWN + 0.7 * LEFT, end= 0.65 * UP + 0.7 * RIGHT, stroke_width= 2, max_tip_length_to_length_ratio=0.08)
            arrow_3_horizontal.shift(shift_count * RIGHT)
            self.add(arrow_3_horizontal)


            weight_1_value = weight_1.pop().shift(0.6 * LEFT + 0.77 * UP)
            weight_1_value.shift(shift_count * RIGHT)
            self.add(weight_1_value)

            weight_2_value = weight_2.pop().shift(0.5 * LEFT + 0.78 * DOWN)
            weight_2_value.shift(shift_count * RIGHT)
            self.add(weight_2_value)

            weight_3_value = weight_3.pop().shift(1.6 * RIGHT + 0.8 * UP)
            weight_3_value.shift(shift_count * RIGHT)
            self.add(weight_3_value)

            input_value = inputs_outputs.pop().shift(2.3 * LEFT + 0.8 * UP)
            input_value.shift(shift_count * RIGHT)
            self.add(input_value)



            box = SurroundingRectangle(point_r, point_s, color= WHITE, stroke_width= 2).shift(shift_count * RIGHT)
            self.add(box)


            horizontal_vgroup.add(box, arrow_1_horizontal, arrow_2_horizontal, arrow_3_horizontal, calc_1_horizontal, calc_2_horizontal, calc_3_horizontal, input_horizontal, weight_1_value, weight_2_value, weight_3_value, input_value)
            shift_count += 6


        self.wait(1)    
        self.play(horizontal_vgroup.animate.shift(14 * LEFT), run_time= 5)
        self.wait(1)
