from table.base import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'lab_user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40), nullable=False, index=True)

