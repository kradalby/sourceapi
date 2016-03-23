#!/usr/bin/env python

from models import db, Query

from flask import Flask
from flask import redirect
from flask import json
from flask.ext.cors import CORS
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from v1 import v1

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    app.register_blueprint(v1, url_prefix='/api/v1')
    return app, db

app, db = create_app()
CORS(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@app.route('/')
def index():
    return redirect("https://github.com/kradalby/sourceapi/blob/master/README.md", code=302)

@app.route('/stats')
def stats():
    total = Query.query.count()
    success = Query.query.filter_by(request_status="success").count()
    errors = Query.query.filter_by(request_status="error").count()
    response = {
        'total': total,
        'success': success,
        'errors': errors
    }
    return json.jsonify(response)

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()

    # app.run()
    manager.run()
