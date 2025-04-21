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
        weight_dic = {}
        input_dic = {}


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
            weight_dic[f"weight_{i}"] = VGroup(weight_1_value, weight_2_value, weight_3_value)
            input_dic[f"input_{i}"] = VGroup(input_value)

            self.play(AnimationGroup(Create(arrow_1_horizontal), Create(input_horizontal), FadeIn(input_value), Create(calc_1_horizontal), FadeIn(weight_1_value), Create(arrow_2_horizontal), Create(calc_2_horizontal), FadeIn(weight_2_value), Create(arrow_3_horizontal), Create(calc_3_horizontal), FadeIn(weight_3_value), Create(box),
            lag_ratio= 0.5, run_time= 5))

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
            weight_dic[f"weight_{i}"].add(weight_1_value_colour, weight_2_value_colour, weight_3_value_colour)
            horizontal_vgroup.add(weight_1_value_colour, weight_2_value_colour, weight_3_value_colour)

            self.play(AnimationGroup(FadeIn(weight_1_value_colour, weight_2_value_colour, weight_3_value_colour),
            lag_ratio= 0.9, run_time= 1))

            self.play(self.camera.frame.animate.move_to(camera_shift * RIGHT))



        # --- WAITING WAITING WAITING --- #

        # self.wait(20)


        # --- Compressing HorizontalBERT Traditional --- #

        self.wait(1)
        
        # Zooming out and centering the camera to view the entire scene
        self.play(AnimationGroup(self.camera.frame.animate.move_to(box_dic["box_3"]).set(width= horizontal_vgroup.width + 2), rate_func= linear, run_time= 7))

        self.wait(1)

        self.play(FadeOut(arrow_4_horizontal), FadeOut(last_output))

        # Shifting boxes and removing the following box
        for i in range (5, 0, -1):
            next_box = box_dic[f"box_{i}"]
            next_text = text_dic[f"text_{i}"]
            next_colour = colour_dic[f"colour_{i}"]
            temp = VGroup(next_box, next_text, next_colour)

            if i > 1:
                self.play(temp.animate.move_to(box_dic[f"box_{i-1}"].get_center() + 0.7 * LEFT), rate_func= smoothstep, run_time= 1.75)

            if i == 1:
                break

            self.remove(temp)
        
        # Zooming back in to the 1st box
        self.play(Restore(self.camera.frame), run_time= 5)

        self.wait(1)

        weight_text_1 = [MathTex(r"\text{Input } \times ", color= WHITE).scale(0.5).shift(3.94 * LEFT + 0.77 * UP)]
        weight_text_2 = [MathTex(r"\text{Calc 1 + }", color= WHITE).scale(0.5).shift(3.9 * LEFT + 0.81 * DOWN)]
        weight_text_3 = [MathTex(r"\dfrac{\text{Calc 2}}{}", color= WHITE).scale(0.5).shift(1.65 * LEFT + 0.915 * UP)]
        weight_text = VGroup(weight_text_1, weight_text_2, weight_text_3)

        # Removing 1st set of weight values to begin the animation to show data running
        self.play(FadeTransform(weight_dic["weight_1"], weight_text))

        self.wait(1)
        


        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        # --- Creating CompressedBERT --- #

        lpddr_text = Text("LPDDR", color= WHITE).scale(1).shift(2 * UP + 3 * RIGHT)
        lpddr_1_1 = Text("1", color= MAROON).scale(0.5).shift(2 * RIGHT + 1 * UP)
        lpddr_1_2 = Text("8", color= MAROON).scale(0.5).shift(2 * RIGHT + 0.5 * UP)
        lpddr_1_3 = Text("12", color= MAROON).scale(0.5).shift(2 * RIGHT + 0 * UP)
        lpddr_2_1 = Text("2", color= GREEN).scale(0.5).shift(2.5 * RIGHT + 1 * UP)
        lpddr_2_2 = Text("9", color= GREEN).scale(0.5).shift(2.5 * RIGHT + 0.5 * UP)
        lpddr_2_3 = Text("2", color= GREEN).scale(0.5).shift(2.5 * RIGHT + 0 * UP)
        lpddr_3_1 = Text("3", color= YELLOW).scale(0.5).shift(3 * RIGHT + 1 * UP)
        lpddr_3_2 = Text("4", color= YELLOW).scale(0.5).shift(3 * RIGHT + 0.5 * UP)
        lpddr_3_3 = Text("1", color= YELLOW).scale(0.5).shift(3 * RIGHT + 0 * UP)
        lpddr_4_1 = Text("4", color= BLUE).scale(0.5).shift(3.5 * RIGHT + 1 * UP)
        lpddr_4_2 = Text("6", color= BLUE).scale(0.5).shift(3.5 * RIGHT + 0.5 * UP)
        lpddr_4_3 = Text("2", color= BLUE).scale(0.5).shift(3.5 * RIGHT + 0 * UP)
        lpddr_5_1 = Text("5", color= ORANGE).scale(0.5).shift(4 * RIGHT + 1 * UP)
        lpddr_5_2 = Text("9", color= ORANGE).scale(0.5).shift(4 * RIGHT + 0.5 * UP)
        lpddr_5_3 = Text("7", color= ORANGE).scale(0.5).shift(4 * RIGHT + 0 * UP)

        lpddr_copies = {}
        for i in range(1, 6):
            for j in range(1, 4):
                var_name = f"lpddr_{i}_{j}"
                copy_var = eval(var_name).copy()
                lpddr_copies[(i, j)] = copy_var
    
        point_v = Dot(1.1 * UP + 1.9 * RIGHT)
        point_w = Dot(0.1 * DOWN + 4.1 * RIGHT)
        lpddr_box = SurroundingRectangle(point_v, point_w, stroke_width= 2, color= WHITE)

        # Points for swapping the weights
        point_x = Dot(0.8 * UP + 3.35 * LEFT)
        point_y = Dot(0.8 * DOWN + 3.25 * LEFT)
        point_z = Dot(0.6 * UP + 1.65 * LEFT)

        # Points for the lines for the moving data point
        dot_a = Dot(0.48 * UP + 6.3 * LEFT)
        dot_b = Dot(0.48 * UP + 4.25 * LEFT)
        dot_c = Dot(0.48 * DOWN + 4.25 * LEFT)
        dot_d = Dot(0.48 * UP + 2.55 * LEFT)
        
        # Lines for the moving data point
        arc_ab = ArcBetweenPoints(dot_a.get_center(), dot_b.get_center(), angle= PI/6, stroke_width= 2)
        arc_bc = ArcBetweenPoints(dot_b.get_center(), dot_c.get_center(), angle= -PI/6, stroke_width= 2)
        arc_cd = ArcBetweenPoints(dot_c.get_center(), dot_d.get_center(), angle= PI/6, stroke_width= 2)
        arc_da = ArcBetweenPoints(dot_d.get_center(), dot_a.get_center(), angle= PI/1.5, stroke_width= 2)

        moving_dot = Dot(dot_a.get_center(), color= PURPLE, radius= 0.1)
        
        

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        # --- Animating Weight-Swapping --- #
        
        self.play(Create(lpddr_1_1), Create(lpddr_1_2), Create(lpddr_1_3), Create(lpddr_2_1), Create(lpddr_2_2), Create(lpddr_2_3),
                  Create(lpddr_3_1), Create(lpddr_3_2), Create(lpddr_3_3), Create(lpddr_4_1), Create(lpddr_4_2) ,Create(lpddr_4_3),
                  Create(lpddr_5_1), Create(lpddr_5_2), Create(lpddr_5_3), Create(lpddr_box), Create(lpddr_text))
        
        self.wait(1)

        self.play(Create(moving_dot))

        # 1st instance of weights being loaded
        self.play(lpddr_copies[(1, 1)].animate.move_to(point_x),
                lpddr_copies[(1, 2)].animate.move_to(point_y),
                lpddr_copies[(1, 3)].animate.move_to(point_z),
                rate_func= smoothstep, run_time= 1.5)
        
        
        # Weight-swapping animation
        for i in range(1, 5):
            input_dic[f"input_{i + 1}"].move_to(5.75 * LEFT + 0.8 * UP)

            self.play(MoveAlongPath(moving_dot, arc_ab, rate_func= smoothstep, run_time= 1))
            self.play(MoveAlongPath(moving_dot, arc_bc, rate_func= smoothstep, run_time= 0.75))
            self.play(MoveAlongPath(moving_dot, arc_cd, rate_func= smoothstep, run_time= 1))
            
            self.play(AnimationGroup(FadeOut(lpddr_copies[(i, 1)]), FadeOut(lpddr_copies[(i, 2)]), FadeOut(lpddr_copies[(i, 3)]), run_time= 1),
                      FadeTransform(input_dic[f"input_{i}"], input_dic[f"input_{i + 1}"], run_time= 1),
                      MoveAlongPath(moving_dot, arc_da, rate_func= smoothstep, run_time= 1.5),
                      AnimationGroup(lpddr_copies[(i + 1, 1)].animate.move_to(point_x),
                                     lpddr_copies[(i + 1, 2)].animate.move_to(point_y),
                                     lpddr_copies[(i + 1, 3)].animate.move_to(point_z),
                                     rate_func= smoothstep, run_time= 1.5))
            i += 1

        self.play(MoveAlongPath(moving_dot, arc_ab), rate_func= smoothstep, run_time= 1)
        self.play(MoveAlongPath(moving_dot, arc_bc), rate_func= smoothstep, run_time= 0.75)
        self.play(MoveAlongPath(moving_dot, arc_cd), rate_func= smoothstep, run_time= 1)
        self.play(MoveAlongPath(moving_dot, arc_da), rate_func= smoothstep, run_time= 1.5)

        last_output.move_to(0.25 * LEFT + 0.8 * UP)
        arrow_4_horizontal.move_to(0.25 * LEFT + 0.35 * UP)
        self.play(Create(last_output), FadeIn(arrow_4_horizontal))
        self.wait(1)

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

