import logging
import pathlib
import sqlalchemy
from sqlalchemy.orm import Session

from config import QABotTestConfig

print("QA Bot Starting")
print("Loading test config")

# Load in the configuration
conf = QABotTestConfig()

# Connect to the DB
db = sqlalchemy.create_engine(conf.DATABASEURI, echo=conf.SQLALCHEMY_ECHO)
session = Session(db)

# import out model definitions
from db import Base
from models import Statement, Question

# Create our tables from the models
Base.metadata.create_all(db)

def user_command_loop():
    running = True
    while running:
        entry = input(">>> ")
        entry = entry.strip()
        if entry.startswith(":"):
            # User entered a statement
            s = Statement(text=entry[1:].strip())
            session.add(s)
            session.commit()
        elif entry.startswith("?"):
            # User entered a question
            q = Question(text=entry[1:].strip())
            session.add(q)
            session.commit()
        else:
            # User entered a command
            cmd = entry.lower()
            if cmd in ("quit", "exit", "stop"):
                running = False
                print("Got QUIT command, exiting...")

            cmd_parts = cmd.split(" ")

    session.close()
    print("Goodbye!")

user_command_loop()