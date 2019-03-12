from models import Question, db

def second_data_parser(data):
    if data:
        return data
    return None

def create_question(data):
    q = Question(
        q_type=data.get('q_type'),
        question_text=data.get('question_text'),
        variant_1=second_data_parser(data.get('variant_1')),
        variant_2=second_data_parser(data.get('variant_2')),
        variant_3=second_data_parser(data.get('variant_3')),
        variant_4=second_data_parser(data.get('variant_4')),
        right_var=data.get('right_var'),
        match_variant_1=second_data_parser(data.get('match_variant_1')),
        match_variant_2=second_data_parser(data.get('match_variant_2')),
        match_variant_3=second_data_parser(data.get('match_variant_3')),
        match_variant_4=second_data_parser(data.get('match_variant_4'))
        )
    db.session.add(q)
    db.session.commit()
    return q.id