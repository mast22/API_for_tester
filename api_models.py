from flask_restplus import fields
from resource import api

"""
QUESTION RELATED MODELS FOR API
"""

post_question_model = api.model('Post question model', {
    "q_type":          fields.String,
    "question_text":   fields.String,
    "variant_1":       fields.String,
    "variant_2":       fields.String,
    "variant_3":       fields.String,
    "variant_4":       fields.String,
    "right_var":       fields.String,
    "match_variant_1": fields.String,
    "match_variant_2": fields.String,
    "match_variant_3": fields.String,
    "match_variant_4": fields.String
})

get_question_model = api.inherit('Get question model', post_question_model, {
    "id":       fields.Integer,
    "in_tests": fields.List(fields.Integer),
})

"""
TEST RELATED MODELS FOR API
"""

get_test_model = api.model('Get test model', {
    "id":        fields.Integer,
    "questions": fields.List(fields.Integer)
})

"""
USER RELATED MODELS FOR API
"""

post_user_model = api.model('Post user model', {
    "name":     fields.String,
    "email":    fields.String,
    "password": fields.String,
    "role":     fields.String
})

get_user_model = api.model('Get user model', {
})