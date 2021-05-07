#!/bin/bash
set -e #stops execution of script if failure occurs somewhere

python wait_for_postgres.py

#init Django project
./django_project/manage.py collectstatic --noinput
./django_project/manage.py migrate

echo "Starting django project."
cd django_project
params=()
if [[ ${DEBUG} = "True" ]]
then
    params+=(--reload)
fi
gunicorn --bind 0.0.0.0:5000 --access-logfile - django_project.wsgi:application --daemon -R "${params[@]}" #change django_project to folder name
cd ..

#echo "Starting React development server."
#cd react
#node ./node_modules/react-scripts/scripts/start.js >/dev/null </dev/null &
#cd ..

echo "Starting nginx."
exec "$@"