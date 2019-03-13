from flask_restplus import reqparse, abort, Api, Resource
from models import Question, Test, ma
from main import app
import methods
from flask import request, jsonify

api = Api(app)

# question api

from api_models import *

question_api = api.namespace('question/', description='Question related APIs')


class QuestionSchema(ma.ModelSchema):
    class Meta:
        model = Question

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

class TestSchema(ma.ModelSchema):
    class Meta:
        model = Test

@test_api.route('/')
class TestAPI(Resource):
    def post(self):
        t_id = methods.create_test()
        response = jsonify(id=t_id, message='Test has been created')
        response.status_code = 201
        return response

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


user_api = api.namespace('user/', description='User related APIs')

@test_api.route('/')
class UserAPI(Resource):
    @api.marshal_with(post_user_model)
    def post(self):
        pass

@test_api.route('/<int:id>')
class TestByIdAPI(Resource):
    @api.marshal_with(get_user_model)
    def get(self, id):
        pass