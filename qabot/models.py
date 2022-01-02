from datetime import datetime
from sqlalchemy import Integer, BigInteger, Float, Boolean, String, DateTime, Column

from db import Base

class Statement(Base):
    __tablename__ = "StatementList"

    id = Column(Integer, primary_key=True)

    text = Column(String(300), nullable=False)

    entry_time = Column(DateTime(), nullable=False, default=datetime.now())

class Question(Base):
    __tablename__ = "QuestionList"

    id = Column(Integer, primary_key=True)

    text = Column(String(300), nullable=False)

    entry_time = Column(DateTime(), nullable=False, default=datetime.now())