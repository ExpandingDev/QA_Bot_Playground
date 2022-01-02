import pathlib
from os import environ as e
from dotenv import load_dotenv

class QABotTestConfig():
    DATABASEURI = "sqlite+pysqlite:///:memory:"
    SQLALCHEMY_ECHO = False