from datetime import datetime

from qabot.db.db import db

class Statement(db.Model):
    __tablename__ = "StatementList"

    id = db.Column(db.Integer, primary_key=True)

    text = db.Column(db.String(300), nullable=False)

    entry_time = db.Column(db.DateTime(), nullable=False, default=datetime.now())

class Question(db.Model):
    __tablename__ = "QuestionList"

    id = db.Column(db.Integer, primary_key=True)

    text = db.Column(db.String(300), nullable=False)

    entry_time = db.Column(db.DateTime(), nullable=False, default=datetime.now())