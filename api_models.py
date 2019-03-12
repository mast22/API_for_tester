from flask_restplus import fields

get_model = api.model('Get model', {
    "id": fields.Integer,
    "q_type": fields.String,
    "question_text": fields.String,
    "variant_1": fields.String,
    "variant_2": fields.String,
    "variant_3": fields.String,
    "variant_4": fields.String,
    "right_var": fields.String,
    "match_variant_1": fields.String,
    "match_variant_2": fields.String,
    "match_variant_3": fields.String,
    "match_variant_4": fields.String
})

post_model = api.model('Post model', {
    "q_type": fields.String,
    "question_text": fields.String,
    "variant_1": fields.String,
    "variant_2": fields.String,
    "variant_3": fields.String,
    "variant_4": fields.String,
    "right_var": fields.String,
    "match_variant_1": fields.String,
    "match_variant_2": fields.String,
    "match_variant_3": fields.String,
    "match_variant_4": fields.String
})
