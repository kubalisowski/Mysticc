import sqlalchemy 
from sqlalchemy.ext.declarative import declarative_base
from config import *

engine = sqlalchemy.create_engine(CONNECTION_STRING)

Base = declarative_base()
Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

