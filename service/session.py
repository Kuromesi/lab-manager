from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('')
Session = sessionmaker(bind=engine)
session = Session()

