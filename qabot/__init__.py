import logging
import pathlib
import sqlalchemy

from config import QABotTestConfig

print("QA Bot Starting")
print("Loading test config")

# Load in the configuration
conf = QABotTestConfig()

# Connect to the DB
db = sqlalchemy.create_engine(conf.DATABASEURI, echo=conf.SQLALCHEMY_ECHO)

# import out model definitions
from models import Base, Statement, Question

# Create our tables from the models
Base.metadata.create_all(db)

def user_command_loop():
    running = True
    while running:
        cmd = input(">>> ")
        cmd = cmd.strip()
        if cmd.startswith(":"):
            # User entered a statement
            print("Got a statement")
        elif cmd.startswith("?"):
            # User entered a question
            print("Got a question")
        else:
            cmd = cmd.lower()
            if cmd in ("quit", "exit", "stop"):
                running = False
                print("Got QUIT command, exiting...")

    print("Goodbye!")

user_command_loop()