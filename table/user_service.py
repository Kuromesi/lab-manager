from table.base import Base
from sqlalchemy import Column, Integer, String

class Service(Base):
    __tablename__ = 'user_service'
    id = Column(Integer, primary_key=True, autoincrement=True)
    service_name = Column(String(100), nullable=False)
    service_port = Column(Integer, nullable=False)
    user = Column(String(40), nullable=False, index=False)