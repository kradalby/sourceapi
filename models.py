#from app.db import Column, DateTime, String, Integer, Bool, func
#from app.db.dialects import postgresql
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Query(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, default=db.func.now())
    request_origin = db.Column(db.String(30))
    request_status = db.Column(db.String(10))
    request_error_message = db.Column(db.String(100), nullable=True)
    api_endpoint = db.Column(db.String(100))
    game_server = db.Column(db.String(30))
    user_agent = db.Column(db.String(2**16))

    def __init__(self, request_origin, request_status, request_error_message, api_endpoint, game_server, user_agent):
        self.request_origin = request_origin
        self.request_status = request_status
        self.request_error_message = request_error_message
        self.api_endpoint = api_endpoint
        self.game_server = game_server
        self.user_agent = user_agent

    def __repr__(self):
        return 'Query from: {} to {} at {}'.format(
            self.request_origin,
            self.game_server,
            self.datetime
        )

def record_query(req, err):
    query = None
    if err != None:
        game_server = ""
        try:
            game_server = req.json['data']
        except:
            pass
        query = Query(
            req.remote_addr,
            'error',
            err['type'],
            req.path,
            game_server,
            req.headers.get('User-Agent')
        )
    else:
        query = Query(
            req.remote_addr,
            'success',
            None,
            req.path,
            req.json['data'],
            req.headers.get('User-Agent')
        )
    db.session.add(query)
    db.session.commit()
