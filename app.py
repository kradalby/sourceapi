#!/usr/bin/env python
import logging
import logging.config

from SourceLib.SourceQuery import SourceQuery

from flask import Flask
from flask import json
from flask import request

from logconf import LOGGING

app = Flask(__name__)
logger = logging.getLogger(__name__)
logging.config.dictConfig(LOGGING)

MISSING_DATA = {
    'status': 'error',
    'data': 'Missing data field'
}

NO_RESPONSE = {
    'status': 'error',
    'data': 'The server did not respond'
}

NOT_VALID_JSON = {
    'status': 'error',
    'data': 'The JSON is not valid'
}


@app.route('/api/v1/all', methods=['POST'])
def all():
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
        response['data'][servername]['ping'] = s.ping()
        response['data'][servername]['rules'] = s.rules()
        response['data'][servername]['players'] = s.player()
        response['status'] = 'success'
        return json.jsonify(response)
    except:
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
