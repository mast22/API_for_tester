from flask_restplus import reqparse

question_post_parser = reqparse.RequestParser()

question_post_parser.add_argument("q_type", required=True, choices=['check', 'radio', 'match', 'string'])
question_post_parser.add_argument("question_text", required=True)
question_post_parser.add_argument("variant_1")
question_post_parser.add_argument("variant_2")
question_post_parser.add_argument("variant_3")
question_post_parser.add_argument("variant_4")
question_post_parser.add_argument("right_var", required=True)
question_post_parser.add_argument("match_variant_1")
question_post_parser.add_argument("match_variant_2")
question_post_parser.add_argument("match_variant_3")
question_post_parser.add_argument("match_variant_4")