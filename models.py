from app.db import Column, DateTime, String, Integer, func
from app.db.dialects import postgresql


class Query(Base):
    __tablename__ = "query"
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime, default=func.now())
    request_origin = Column(postgresql.INET)
    request_status = Column(String(10))
    request_error_message = Column(String(100), nullable=True)
    api_endpoint = Column(String(100))
    game_server = Columnt(String(30))

    def __init__(self, request_origin, request_status, request_error_message, api_endpoint, game_server):
        self.request_origin = request_origin
        self.request_status = request_status
        self.request_error_message = request_error_message
        self.api_endpoint = api_endpoint
        self.game_server = game_server

    def __repr__(self):
        return 'Query from: {} to {} at {}'.format(
            self.request_origin,
            self.game_server,
            self.datetime
        )
