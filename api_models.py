from flask_restplus import fields
from resource import api

post_question_model = api.model('Post model', {
    "q_type":           fields.String,
    "question_text":    fields.String,
    "variant_1":        fields.String,
    "variant_2":        fields.String,
    "variant_3":        fields.String,
    "variant_4":        fields.String,
    "right_var":        fields.String,
    "match_variant_1":  fields.String,
    "match_variant_2":  fields.String,
    "match_variant_3":  fields.String,
    "match_variant_4":  fields.String
})

get_question_model = api.inherit('Get model', post_question_model, {
    "id":               fields.Integer,
    "in_tests":         fields.List(fields.Integer),
})


get_test_model = api.model('Get test with question ids', {
    "id": fields.Integer,
    "questions": fields.List(fields.Integer)
})