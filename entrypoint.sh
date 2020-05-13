#!/bin/bash
set -e #stops execution of script if failure occurs somewhere

#init Django project
./django_project/manage.py collectstatic --noinput
./django_project/manage.py migrate

cd django_project
gunicorn --bind 0.0.0.0:5000 --access-logfile - django_project.wsgi:application --daemon #change django_project to folder name
cd ..
echo "django_project initialized."

echo "Starting nginx."
exec "$@"