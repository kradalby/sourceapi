from sqlalchemy import Column, DateTime, String, Integer, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import postgresql

Base = declarative_base()


class Query(Base):
    __tablename__ = "query"
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime, default=func.now())
    request_origin = Column(postgresql.INET)
    api_enpoint = Column(String)
    game_server = Columnt(String)
    request_status = Column(String)
    request_error_message = Column(String, nullable=True)

