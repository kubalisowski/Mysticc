from sqlalchemy import text
from sqlalchemy_utils import database_exists
from database._db import engine, Base

def execute_script(script_path):
    with engine.connect() as con:
        with open(script_path) as file:
            query = text(file.read())
            con.execute(query)


def init_db():
    if not database_exists(engine.url):
        Base.metadata.create_all(engine, Base.metadata.tables.values(), checkfirst=True)