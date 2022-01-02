import logging
import pathlib
import sqlalchemy

from config import QABotTestConfig

print("QA Bot Starting")
print("Loading test config")

conf = QABotTestConfig()

db = sqlalchemy.create_engine(conf.DATABASEURI, echo=conf.SQLALCHEMY_ECHO)

