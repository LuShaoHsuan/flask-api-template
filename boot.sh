#!/bin/sh

while true; do
    if flask deploy; then
        break
    fi
    echo Deploy command failed, retrying in 5 secs...
    sleep 5
done

exec gunicorn --workers=2 --threads=4 --worker-class=gthread -b :5000 --access-logfile - flask_api:app