import sqlalchemy 
from sqlalchemy.ext.declarative import declarative_base
from connection_string import *

engine = sqlalchemy.create_engine(CONNECTION_STRING)

Base = declarative_base()
Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

