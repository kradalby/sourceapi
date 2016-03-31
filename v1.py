from SourceLib.SourceQuery import SourceQuery

from flask import Blueprint
from flask import json
from flask import request

from errors import *

from models import record_query

v1 = Blueprint('v1', __name__)


@v1.route('/<function>', methods=['POST'])
def root(function=None):
    response = {
        'data': {}
    }

    if not request.json:
        record_query(request, NOT_VALID_JSON)
        return json.jsonify(NOT_VALID_JSON)

    if 'data' not in request.json.keys():
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

        if function == 'all':
            response['data'][servername] = s.info()
            response['data'][servername]['players'] = s.player()
        elif function == 'serverinfo':
            response['data'][servername] = s.info()
        elif function == 'playerinfo':
            response['data'][servername] = s.player()
        elif function == 'ping':
            response['data'][servername] = s.ping()
        elif function == 'rules':
            s.timeout = 10
            response['data'][servername] = s.rules()
        else:
            record_query(request, ENDPOINT_NOT_FOUND)
            return json.jsonify(ENDPOINT_NOT_FOUND)

        response['status'] = 'success'
        record_query(request, None)
        return json.jsonify(response)
    except Exception:
        record_query(request, NO_RESPONSE)
        return json.jsonify(NO_RESPONSE)
