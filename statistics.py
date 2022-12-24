from app import db


def count_average_text_length():
    texts = db.Table['PostText']
    result = self.query.with_entities(db.func.avg(PostText.text_length).label("average_text_length")).filter()