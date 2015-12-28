#!/usr/bin/env python
import logging
import logging.config

from SourceLib.SourceQuery import SourceQuery

from flask import Flask
from flask import json
from flask import request
from flask.ext.sqlalchemy import SQLAlchemy


from logconf import LOGGING

app = Flask(__name__)
db = SQLAlchemy(app)

app.config.from_pyfile('config.py')

logger = logging.getLogger(__name__)
logging.config.dictConfig(LOGGING)

MISSING_DATA = {
    'status': 'error',
    'data': 'Missing data field',
    'type': 'MD'
}

NO_RESPONSE = {
    'status': 'error',
    'data': 'The server did not respond',
    'type': 'NR'
}

NOT_VALID_JSON = {
    'status': 'error',
    'data': 'The JSON is not valid',
    'type': 'NVJ'
}

def record_query(req, err):
    query = None
    if err != None:
        query = Query(
            req.remote_addr,
            'error',
            err['type'],
            req.endpoint,
            req.json['data']
        )
    else:
        query = Query(
            req.remote_addr,
            'success',
            None,
            req.endpoint,
            req.json['data']
        )
    db.session.add(query)
    db.commit()


@app.route('/api/v1/all', methods=['POST'])
def all():
    response = {
        'data': {}
    }

    if not request.json:
        record_query(request, NOT_VALID_JSON)
        return json.jsonify(NOT_VALID_JSON)

    if not 'data' in request.json.keys():
        record_query(request, MISSING_DATA)
        return json.jsonify(MISSING_DATA)

    try:
        ip, port = request.json['data'].split(':')
    except:
        record_query(request, NOT_VALID_JSON)
        return json.jsonify(NOT_VALID_JSON)

    try:
        s = SourceQuery(ip, int(port))
        servername = '{}:{}'.format(ip, port)
        response['data'][servername] = s.info()
        response['data'][servername]['ping'] = s.ping()
        response['data'][servername]['rules'] = s.rules()
        response['data'][servername]['players'] = s.player()
        response['status'] = 'success'
        record_query(request, None)
        return json.jsonify(response)
    except:
        record_query(request, NO_RESPONSE)
        return json.jsonify(NO_RESPONSE)


@app.route('/api/v1/serverinfo', methods=['POST'])
def serverinfo():
    response = {
        'data': {}
    }

    if not request.json:
        return json.jsonify(NOT_VALID_JSON)

    if not 'data' in request.json.keys():
        return json.jsonify(MISSING_DATA)

    try:
        ip, port = request.json['data'].split(':')
    except:
        return json.jsonify(NOT_VALID_JSON)

    try:
        s = SourceQuery(ip, int(port))
        servername = '{}:{}'.format(ip, port)
        response['data'][servername] = s.info()
        response['status'] = 'success'
        return json.jsonify(response)
    except:
        return json.jsonify(NO_RESPONSE)


@app.route('/api/v1/playerinfo', methods=['POST'])
def playerinfo():
    response = {
        'data': {}
    }

    if not request.json:
        return json.jsonify(NOT_VALID_JSON)

    if not 'data' in request.json.keys():
        return json.jsonify(MISSING_DATA)

    try:
        ip, port = request.json['data'].split(':')
    except:
        return json.jsonify(NOT_VALID_JSON)

    try:
        s = SourceQuery(ip, int(port))
        servername = '{}:{}'.format(ip, port)
        response['data'][servername] = s.player()
        response['status'] = 'success'
        return json.jsonify(response)
    except:
        return json.jsonify(NO_RESPONSE)


@app.route('/api/v1/ping', methods=['POST'])
def ping():
    response = {
        'data': {}
    }

    if not request.json:
        return json.jsonify(NOT_VALID_JSON)

    if not 'data' in request.json.keys():
        return json.jsonify(MISSING_DATA)

    try:
        ip, port = request.json['data'].split(':')
    except:
        return json.jsonify(NOT_VALID_JSON)

    try:
        s = SourceQuery(ip, int(port))
        servername = '{}:{}'.format(ip, port)
        response['data'][servername] = s.ping()
        response['status'] = 'success'
        return json.jsonify(response)
    except:
        return json.jsonify(NO_RESPONSE)


@app.route('/api/v1/rules', methods=['POST'])
def rules():
    response = {
        'data': {}
    }

    if not request.json:
        return json.jsonify(NOT_VALID_JSON)

    if not 'data' in request.json.keys():
        return json.jsonify(MISSING_DATA)

    try:
        ip, port = request.json['data'].split(':')
    except:
        return json.jsonify(NOT_VALID_JSON)

    try:
        s = SourceQuery(ip, int(port))
        servername = '{}:{}'.format(ip, port)
        response['data'][servername] = s.rules()
        response['status'] = 'success'
        return json.jsonify(response)
    except:
        return json.jsonify(NO_RESPONSE)

if __name__ == '__main__':
    app.debug = True

    app.run()
