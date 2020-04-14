#!/bin/bash
set -e #stops execution of script if failure occurs somewhere

#init Django project
cd django_project
./manage.py migrate
./manage.py collectstatic --noinput
gunicorn --bind 0.0.0.0:8000 --access-logfile - django_project.wsgi:application --daemon #change django_project to folder name
cd ..
echo "django_project initialized."

#build react app
#cd react
#npm run build
#cd ..

echo "Fetch static files at localhost:8000/static/file1.html"
echo "Fetch react app at localhost:8000/react/"
echo "Get django data at localhost:8000/django/"
echo "Trailing slash is necessary for /react/ and /django/"
exec "$@"