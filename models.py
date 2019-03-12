from main import app
from sqlalchemy import Column
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy(app)
ma = Marshmallow(app)

# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(50), unique=True)
#     password = db.Column(db.String(50))
#     role = db.Column(db.String(30), default='user')

class Question(db.Model):
    """
    q_type
    question_text
    variant_1
    variant_2
    variant_3
    variant_4
    right_var
    variant_1
    match_variant_1
    match_variant_2
    match_variant_3
    match_variant_4
    """
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    q_type = db.Column(db.String(50))

    question_text = db.Column(db.String(255))

    variant_1 = db.Column(db.String(255))
    variant_2 = db.Column(db.String(255))
    variant_3 = db.Column(db.String(255))
    variant_4 = db.Column(db.String(255))
    right_var = db.Column(db.String(50))

    """
    В случае если это match вопрос, то из нижеследующих полей выбирается ответ для соответствия вариантам
    variant_1: match_variant_1
    """
    match_variant_1 = db.Column(db.String(255))
    match_variant_2 = db.Column(db.String(255))
    match_variant_3 = db.Column(db.String(255))
    match_variant_4 = db.Column(db.String(255))