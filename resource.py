from flask_restplus import reqparse, abort, Api, Resource, fields
from models import Question, ma
from main import app
import parsers
import methods
from flask import request, jsonify
from api_models import get_model, post_model

api = Api(app)

question_api = api.namespace('question/', description='Question related APIs')


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