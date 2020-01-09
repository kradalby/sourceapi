#!/usr/bin/env python
# pyre-strict
from flask import Flask
from flask import json
from flask import redirect
# pyre-fixme[21]: Could not find `ext`.
from flask.ext.cors import CORS

from werkzeug.wsgi import DispatcherMiddleware

# pyre-fixme[21]: Could not find `flask_migrate`.
from flask_migrate import Migrate, MigrateCommand

# pyre-fixme[21]: Could not find `flask_script`.
from flask_script import Manager

# pyre-fixme[21]: Could not find `prometheus_client`.
from prometheus_client import make_wsgi_app

from models import Query, db

# pyre-fixme[21]: Could not find `sqlalchemy`.
from sqlalchemy import func
from sqlalchemy.sql import label

from v1 import v1
from werkzeug.wrappers import Response


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    app.register_blueprint(v1, url_prefix='/api/v1')
    return app

# pyre-fixme[5]: Global expression must be annotated.
app = create_app()
# pyre-fixme[16]: Module `flask` has no attribute `ext`.
CORS(app)

# pyre-fixme[5]: Global expression must be annotated.
migrate = Migrate(app, db)

# pyre-fixme[5]: Global expression must be annotated.
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@app.route('/')
def index() -> Response:
    return redirect('https://github.com/kradalby/sourceapi/blob/master/README.md', code=302)


@app.route('/stats')
# pyre-fixme[3]: Return type must be annotated.
def stats():
    # pyre-fixme[16]: `Query` has no attribute `query`.
    total = Query.query.count()
    success = Query.query.filter_by(request_status='success').count()
    errors = Query.query.filter_by(request_status='error').count()
    user_agents_aggregated = db.session.query(Query.user_agent,
                                              # pyre-fixme[18]: Global name
                                              #  `sqlalchemy` is undefined.
                                              label('amount', func.count(Query.user_agent))
                                             ).group_by(Query.user_agent).all()
    request_origin_aggregated = db.session.query(Query.request_origin,
                                              label('amount', func.count(Query.request_origin))
                                             ).group_by(Query.request_origin).all()
    response = {
        'total': total,
        'success': success,
        'errors': errors,
        'user_agents': user_agents_aggregated,
        'request_origin': request_origin_aggregated
    }
    return json.jsonify(response)




if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()

    # app.run()
    # pyre-fixme[16]: Module `wsgi` has no attribute `DispatcherMiddleware`.
    app_dispatch = DispatcherMiddleware(app, {
        '/metrics': make_wsgi_app()
    })
    manager.run()
