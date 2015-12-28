#!/usr/bin/env python

from models import db

from flask import Flask

from v1 import v1

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    app.register_blueprint(v1, url_prefix='/api/v1')
    return app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run()
