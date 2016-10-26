#!/usr/bin/env sh

cd /srv/app
python app.py db init
python app.py db upgrade

rm /tmp/project-master.pid

echo Starting uwsgi.
exec uwsgi --chdir=/srv/app \
    --callable=app \
    --wsgi-file=app.py \
    --master --pidfile=/tmp/project-master.pid \
    --socket=0.0.0.0:8080 \
    --http=0.0.0.0:8081 \
    --processes=5 \
    --harakiri=20 \
    --max-requests=5000 \
    --vacuum
