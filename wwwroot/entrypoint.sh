#!/bin/bash
set -e

#uwsgi --http :8000 --wsgi-file test.py
gunicorn -w 4 test:application --daemon
echo "gunicorn daemon success"
exec "$@"