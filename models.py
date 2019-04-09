from main import app
from sqlalchemy import Column
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    __tablename__ = 'users'
    id =        db.Column(db.Integer, primary_key=True)
    username =      db.Column(db.String(50))
    email =     db.Column(db.String(50), unique=True)
    password =  db.Column(db.String(50))
    role =      db.Column(db.String(30), default='user')

    def __init__(self, username, email, password, role):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.role = role

"""
Assosiation table to connect test and question
"""
question_in_test = db.Table('question_in_test',
    db.Column('question_id', db.Integer, db.ForeignKey('questions.id')),
    db.Column('test_id', db.Integer, db.ForeignKey('test.id'))
)


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
    in_tests
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
    In case of a "match" question, the variants will be choosen from the variants below
    variant_1: match_variant_1
    """
    match_variant_1 = db.Column(db.String(255))
    match_variant_2 = db.Column(db.String(255))
    match_variant_3 = db.Column(db.String(255))
    match_variant_4 = db.Column(db.String(255))
    in_tests = db.relationship('Test', secondary=question_in_test, backref=db.backref('questions', lazy='dynamic'))


class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True)