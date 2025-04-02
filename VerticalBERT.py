from manim import *

class VerticalBERT(MovingCameraScene):
    def construct(self):
        
        # --- Creating VerticalBERT Complex --- #
        # OUTPUT
        output = Text("Output", font = "Arial").scale(0.25).shift(3.55 * UP)

        arrow_1 = Arrow(buff= 0.05, start= 3 * UP, end= 3.45 * UP)
        
        # SOFTMAX
        softmax_text = Text("Softmax", font = "Arial").scale(0.25).shift(2.9 * UP)
        softmax_box = SurroundingRectangle(softmax_text, color=GREEN)
        softmax = VGroup(softmax_box, softmax_text)

        arrow_2 = Arrow(buff= 0.05, start= 2.25 * UP, end= 2.75 * UP)

        # LINEAR
        linear_text = Text("Linear", font = "Arial").scale(0.25).shift(2.15 * UP)
        linear_box = SurroundingRectangle(linear_text, color = PURPLE)
        linear = VGroup(linear_text, linear_box)

        arrow_3 = Arrow(buff= 0.05, start= 1.5 * UP, end= 2 * UP)

        # ADD & NORM
        add_norm_text = Text("Add & Norm", font = "Arial").scale(0.25).shift(1.4 * UP)
        add_norm_box = SurroundingRectangle(add_norm_text, color= YELLOW)
        add_norm_1 = VGroup(add_norm_text, add_norm_box)

        # FEED FORWARD
        feed_forward_text = Text("Feed Forward", font = "Arial").scale(0.25).shift(1.03 * UP)
        feed_forward_box = SurroundingRectangle(feed_forward_text, color= BLUE)
        feed_forward = VGroup(feed_forward_text, feed_forward_box)

        arrow_4 = Arrow(buff= 0.05, start= 0.4 * UP, end= 0.9 * UP)

        # CURVED ARROW 1
        point_a = Dot(0.65 * UP + 0.6 * LEFT)
        point_b = Dot(1.4 * UP + 0.6 * LEFT)
        line_a = Line(0.65*UP, point_a.get_center(), stroke_width = 2)
        arc_a = ArcBetweenPoints(point_a.get_center(), point_b.get_center(), angle=-PI, stroke_width= 2)
        arc_a.add_tip(tip_length= 0.1, tip_width= 0.15)

        # ADD & NORM 2
        add_norm_text_2 = Text("Add & Norm", font = "Arial").scale(0.25).shift(0.3 * UP)
        add_norm_box_2 = SurroundingRectangle(add_norm_text_2, color= YELLOW)
        add_norm_2 = VGroup(add_norm_text_2, add_norm_box_2)

        # MULTI-HEAD ATTENTION
        multi_head_attention_text = Text("Multi-Head Attention", font = "Arial").scale(0.25).shift(0.07 * DOWN)
        multi_head_attention_box = SurroundingRectangle(multi_head_attention_text, color = ORANGE)
        multi_head_attention = VGroup(multi_head_attention_text, multi_head_attention_box)

        arrow_5 = Arrow(buff= 0.05, start= 1.2 * DOWN, end= 0.2 * DOWN, stroke_width= 2, max_tip_length_to_length_ratio= 0.15)

        # TRIDENT ARROW
        point_c = Dot(0.5 * DOWN + 0.4 * LEFT)
        point_d = Dot(0.5 * DOWN + 0.4 * RIGHT)
        line_b = Line(point_c.get_center(), point_d.get_center(), stroke_width= 2)
        point_e = Dot(0.25 * DOWN + 0.6 * LEFT)
        point_f = Dot(0.25 * DOWN + 0.6 * RIGHT)
        arc_b = ArcBetweenPoints(point_c.get_center(), point_e.get_center(), angle= -PI/2, stroke_width= 2)
        arc_b.add_tip(tip_length= 0.1, tip_width= 0.15)
        arc_c = ArcBetweenPoints(point_d.get_center(), point_f.get_center(), angle= PI/2, stroke_width= 2)
        arc_c.add_tip(tip_length= 0.1, tip_width= 0.15)

        # CURVED ARROW 2
        point_g = Dot(0.7 * DOWN)
        point_h = Dot(0.7 * DOWN + 0.6 * LEFT)
        line_c = Line(point_g.get_center(), point_h.get_center(), stroke_width= 2)
        point_i = Dot(0.3 * UP + 0.6 * LEFT)
        arc_d = ArcBetweenPoints(point_h.get_center(), point_i.get_center(), angle= -PI, stroke_width= 2)
        arc_d.add_tip(tip_length= 0.1, tip_width= 0.15)

        # Nx BOX
        point_j = Dot(0.7 * DOWN + 1.1 * LEFT)
        point_k = Dot(1.55 * UP + 1.1 * RIGHT)
        Nx_box = SurroundingRectangle(point_j, point_k, color= WHITE, stroke_width= 2)

        calc_complex = VGroup(add_norm_1, feed_forward, arrow_4, line_a, arc_a, add_norm_2, multi_head_attention, arrow_5, line_b, arc_b, arc_c, line_c, arc_d, Nx_box)

        # POSITIONAL ENCODING
        plus_circle = Circle(radius= 0.15, color= WHITE, stroke_width= 2).shift(1.3 * DOWN)
        plus_sign_text = MathTex("+").scale(0.85).shift(1.3 * DOWN)
        plus_sign = VGroup(plus_circle, plus_sign_text)
        point_l = Dot(1.3 * DOWN + 0.15 * LEFT)
        point_m = Dot(1.3 * DOWN + 0.75 * LEFT)
        line_d = Line(point_l.get_center(), point_m.get_center(), stroke_width= 2)
        pos_enc_circle = Circle(radius= 0.2, color= WHITE, stroke_width= 2).shift(1.3 * DOWN + 0.95 * LEFT)
        point_n = Dot(1.3 * DOWN + 0.95 * LEFT)
        arc_e = ArcBetweenPoints(point_m.get_center(), point_n.get_center(), angle= -PI, stroke_width= 2)
        point_o = Dot(1.3 * DOWN + 1.15 * LEFT)
        arc_f = ArcBetweenPoints(point_n.get_center(), point_o.get_center(), angle= PI, stroke_width= 2)
        pos_enc = VGroup(plus_sign, line_d, pos_enc_circle, arc_e, arc_f)

        arrow_6 = Arrow(buff= 0.05, start= 1.9 * DOWN, end= 1.4 * DOWN)

        # INPUT EMBEDDING
        input_embedding_text = Text("Input Embedding", font= "Arial").scale(0.25).shift(2.05 * DOWN)
        input_embedding_box = SurroundingRectangle(input_embedding_text, color= RED)
        input_embedding = VGroup(input_embedding_text, input_embedding_box)

        arrow_7 = Arrow(buff= 0.05, start= 2.7 * DOWN, end= 2.2 * DOWN)

        # INPUTS
        inputs = Text("Inputs", font= "Arial").scale(0.25).shift(2.85 * DOWN)

        vertical_BERT = VGroup(output, arrow_1, softmax, arrow_2, linear,
                                arrow_3, add_norm_1, feed_forward, arrow_4, line_a, arc_a,
                                add_norm_2, multi_head_attention, arrow_5, line_b, arc_b, arc_c, line_c, arc_d, Nx_box,
                                plus_sign, line_d, pos_enc_circle, arc_e, arc_f,
                                arrow_6, input_embedding, arrow_7, inputs)


        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        # --- Creating VerticalBERT Simple --- #

        # INPUTS
        inputs_simple = Text("Inputs", font= "Arial", color= WHITE).scale(0.25).shift(1.6 * DOWN + 3 * RIGHT)


        # CALCS
        arrow_8 = Arrow(buff= 0.05, start= 1.45 * DOWN + 3 * RIGHT, end= 0.75 * DOWN + 3 * RIGHT)
        calc_1 = Text("Calc 1", font= "Arial", color= WHITE).scale(0.25).shift(0.6 * DOWN + 3 * RIGHT)
        arrow_9 = Arrow(buff= 0.05, start= 0.45 * DOWN + 3 * RIGHT, end= 0.25 * UP + 3 * RIGHT)
        calc_2 = Text("Calc 2", font= "Arial", color= WHITE).scale(0.25).shift(0.4 * UP + 3 * RIGHT)
        arrow_10 = Arrow(buff= 0.05, start= 0.55 * UP + 3 * RIGHT, end= 1.25 * UP + 3 * RIGHT)
        calc_3 = Text("Calc 3", font= "Arial", color= WHITE).scale(0.25).shift(1.4 * UP + 3 * RIGHT)
        arrow_11 = Arrow(buff= 0.05, start= 1.55 * UP + 3 * RIGHT, end= 2.25 * UP + 3 * RIGHT)
        point_p = Dot(0.875 * DOWN + 2.5 * RIGHT)
        point_q = Dot(1.725 * UP + 3.5 * RIGHT)
        calc_box = SurroundingRectangle(point_p, point_q, color= WHITE, stroke_width= 2)

        calc_simple = VGroup(arrow_8, calc_1, arrow_9, calc_2, arrow_10, calc_3, arrow_11, calc_box)

        # OUTPUTS
        output_simple = Text("Output", font= "Arial", color= WHITE).scale(0.25).shift(2.4 * UP + 3 * RIGHT)


        # --- Big Purple Arrows --- #
        big_arrow_1 = Arrow(buff= 0, start= 1.425 * UP + 1 * LEFT, end= 1.425 * UP + 1.7 * RIGHT, color= PURPLE_D)
        big_arrow_2 = Arrow(buff= 0, start= 0.425 * UP + 1 * LEFT, end= 0.425 * UP + 1.7 * RIGHT, color= PURPLE_D)
        big_arrow_3 = Arrow(buff= 0, start= 0.575 * DOWN + 1 * LEFT, end= 0.575 * DOWN + 1.7 * RIGHT, color= PURPLE_D)



        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        # --- Playing VerticalBERT Animation --- #

        self.play(AnimationGroup(Create(inputs), Create(arrow_7),Create(input_embedding), Create(arrow_6),
                lag_ratio= 0.5)
        )
        self.play(AnimationGroup(Create(plus_sign), Create(line_d),
                lag_ratio= 0.5)
        )
        self.play(AnimationGroup(Create(pos_enc_circle), Create(arc_e), Create(arc_f),
                lag_ratio= 0.8)
        )
        self.play(AnimationGroup(Create(arrow_5), Create(multi_head_attention), Create(add_norm_2), Create(line_b),
                lag_ratio= 0.5)
        )
        self.play(Create(arc_b), Create(arc_c), Create(line_c))
        self.play(Create(arc_d))
        self.play(AnimationGroup(Create(arrow_4), Create(feed_forward), Create(add_norm_1), Create(line_a), 
                lag_ratio= 0.5)
        )
        self.play(Create(arc_a), Create(Nx_box))
        self.play(AnimationGroup(Create(arrow_3), Create(linear), Create(arrow_2), Create(softmax), Create(arrow_1), Create(output),
                lag_ratio= 0.5)
        )

        self.wait(1)


        # --- Creating VerticalBERT Simple --- #
        
        vertical_BERT_copy = vertical_BERT.copy()
        self.play(vertical_BERT_copy.animate.shift(3 * LEFT), vertical_BERT.animate.shift(3.5 * RIGHT))
        self.play(Create(big_arrow_1), Create(big_arrow_2), Create(big_arrow_3))

        self.play(AnimationGroup(FadeOut(arrow_1), FadeOut(softmax), FadeOut(arrow_2), FadeOut(linear), FadeOut(arrow_3),
                lag_ratio= 0.5)
        )
        self.play(Transform(output, output_simple))
        self.play(AnimationGroup(FadeOut(arrow_7), FadeOut(input_embedding), FadeOut(arrow_6), FadeOut(pos_enc, plus_sign),
                lag_ratio= 0.5)
        )
        self.play(Transform(inputs, inputs_simple))
        self.play(FadeTransform(calc_complex, calc_simple))


        # --- TRANSITION TO HORIZONTAL BERT --- #
        self.play(FadeOut(vertical_BERT_copy), FadeOut(big_arrow_1), FadeOut(big_arrow_2), FadeOut(big_arrow_3), run_time= 2)

        self.wait(1)


        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        # --- Creating HorizontalBERT Example --- #

        input_horizontal_ex = Text("Input", color= WHITE).scale(0.4).shift(0.8 * UP + 6.35 * LEFT)
        arrow_1_horizontal_ex = Arrow(buff= 0.05, start= 0.35 * UP + 6.9 * LEFT, end= 0.35 * UP + 5.55 * LEFT, stroke_width= 2, max_tip_length_to_length_ratio= 0.12)
        input_horizontal_ex = VGroup(input_horizontal_ex, arrow_1_horizontal_ex)
        
        point_r = Dot(1 * UP + 1.25 * LEFT)
        point_s = Dot(1 * DOWN + 5.25 * LEFT)
        box_horizontal_ex = SurroundingRectangle(point_r, point_s, color= WHITE, stroke_width= 2)
        calc_1_horizontal_ex = Text("Calc 1", color= WHITE).scale(0.4).shift(0.8 * UP + 4.85 * LEFT)
        calc_2_horizontal_ex = Text("Calc 2", color= WHITE).scale(0.4).shift(0.8 * DOWN + 4.85 * LEFT)
        calc_3_horizontal_ex = Text("Calc 3", color= WHITE).scale(0.4).shift(0.8 * UP + 2.55 * LEFT)
        arrow_2_horizontal_ex = Arrow(buff= 0.05, start= 0.6 * UP + 4.8 * LEFT, end= 0.6 * DOWN + 4.8 * LEFT, stroke_width= 2, max_tip_length_to_length_ratio= 0.13)
        arrow_3_horizontal_ex = Arrow(buff= 0.05, start= 0.85 * DOWN + 4.25 * LEFT, end= 0.6 * UP + 3 * LEFT, stroke_width= 2, max_tip_length_to_length_ratio= 0.085)
        calc_horizontal_ex = VGroup(box_horizontal_ex, calc_1_horizontal_ex, calc_2_horizontal_ex, calc_3_horizontal_ex, arrow_2_horizontal_ex, arrow_3_horizontal_ex)

        output_horizontal_ex = Text("Output", color= WHITE).scale(0.4).shift(0.8 * UP + 0.1 * LEFT)
        arrow_4_horizontal_ex = Arrow(buff= 0.05, start= 0.35 * UP + 0.9 * LEFT, end= 0.35 * UP + 0.45 * RIGHT, stroke_width= 2, max_tip_length_to_length_ratio= 0.12)
        output_horizontal_ex = VGroup(output_horizontal_ex, arrow_4_horizontal_ex)
        

        self.remove(inputs, output)
        self.play(FadeTransform(inputs_simple, input_horizontal_ex), FadeTransform(calc_simple, calc_horizontal_ex), FadeTransform(output_simple, output_horizontal_ex),
                  run_time= 2)
        
        self.wait(1)


        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        
        # --- STATS STATS STATS --- #


        # --- WAITING WAITING WAITING --- #


        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        self.play(FadeOut(input_horizontal_ex), FadeOut(calc_horizontal_ex), FadeOut(output_horizontal_ex), FadeOut(box_horizontal_ex))

        self.wait(1)
