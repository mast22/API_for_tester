from flask_restplus import reqparse, abort, Api, Resource
from models import Question, Test, ma
from main import app
import parsers
import methods
from flask import request, jsonify

api = Api(app)

# question api

question_api = api.namespace('question/', description='Question related APIs')

from api_models import get_question_model, post_question_model, get_test_model

class QuestionSchema(ma.ModelSchema):
    class Meta:
        model = Question

class TestSchema(ma.ModelSchema):
    class Meta:
        model = Test

@question_api.route('/')
class QuestionAPI(Resource):
    @api.expect(post_question_model)
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
class QuestionByIdAPI(Resource):
    @api.marshal_with(get_question_model)
    def get(self, id):
        """
        Returns a single question
        """
        q = Question.query.get(id)
        if not q:
            return abort(404, f'Question {id} does not exist', id=id)
        question_schema = QuestionSchema()
        output = question_schema.dump(q).data
        print(output)
        return output

test_api = api.namespace('test/', description='Test related APIs')

@test_api.route('/<int:id>')
class TestByIdAPI(Resource):
    @api.marshal_with(get_test_model)
    def get(self, id):
        """
        Returns test with related questions
        """
        t = Test.query.get(id)
        if not t:
            return abort(404, f'Test {id} does not exist', id=id)
        test_schema = TestSchema()
        output = test_schema.dump(t).data
        return output
