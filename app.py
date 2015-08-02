#!/usr/bin/env python

from flask import Flask, request, json, abort
from SourceLib.SourceQuery import SourceQuery as q

app = Flask(__name__)

@app.route('/api/v1/all', methods=['POST'])
def all():
    response = {}
    if not request.json:
        abort(400)
    for ip, port in request.json:
        s = q(ip, int(port))
        servername = "%s:%s" % (ip,port)
        response[servername] = s.info()
        response[servername]["ping"] = s.ping()
        response[servername]["rules"] = s.rules()
        response[servername]["players"] = s.player()
    return json.jsonify(response)

@app.route('/api/v1/serverinfo', methods=['POST'])
def serverinfo():
    response = {}
    if not request.json:
        abort(400)
    for ip, port in request.json:
        s = q(ip, int(port))
        response["%s:%s" % (ip,port)] = s.info()
    return json.jsonify(response)

@app.route('/api/v1/playerinfo', methods=['POST'])
def playerinfo():
    response = {}
    if not request.json:
        abort(400)
    for ip, port in request.json:
        s = q(ip, int(port))
        response["%s:%s" % (ip,port)] = s.player()
    return json.jsonify(response)

@app.route('/api/v1/ping', methods=['POST'])
def ping():
    response = {}
    if not request.json:
        abort(400)
    for ip, port in request.json:
        s = q(ip, int(port))
        response["%s:%s" % (ip,port)] = s.ping()
    return json.jsonify(response)

@app.route('/api/v1/rules', methods=['POST'])
def rules():
    response = {}
    if not request.json:
        abort(400)
    for ip, port in request.json:
        s = q(ip, int(port))
        response["%s:%s" % (ip,port)] = s.rules()
    return json.jsonify(response)

if __name__ == '__main__':
    app.debug = True

    app.run()