from flask_restplus import reqparse, abort, Api, Resource, fields
from models import Question, ma
from main import app
import parsers
import methods
from flask import request, jsonify

api = Api(app)

question_api = api.namespace('question/', description='Question related APIs')

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



class QuestionSchema(ma.ModelSchema):
    class Meta:
        model = Question

@question_api.route('/')
class QuestionAPI(Resource):
    @api.expect(post_model)
    def post(self):
        """
        Creates a new question
        """
        data = request.json
        q_id = methods.create_question(data)
        response = jsonify(id=q_id, message='Question has been created')
        response.status_code = 201
        return response

@question_api.route('/<int:id>')
# @api.response(404, 'Question not found.')
class QuestionByIdAPI(Resource):
    @api.marshal_with(get_model)
    def get(self, id):
        """
        Returns a single question
        """
        q = Question.query.get(id)
        if not q:
            return abort(404, f'Question {id} does not exist', id=id)
        question_schema = QuestionSchema()
        output = question_schema.dump(q).data
        return output