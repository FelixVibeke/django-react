# start.django-react

A single Docker container hosting both React and Django. 

The React App is accessible directly at localhost:8000.
The Django API is accessible at localhost:8000/django/.

The /django_static/ and /media/ subpaths also serve static files.

# How to use

Place the .env file in the root folder, and add the following:
```
	DATABASE_URL=postgres://postgres:postgres@db:5432/postgres
	SECRET_KEY=your_secret_key
	DEBUG=True
```

Run this in the react directory to generate the production build:

```
	npm run build 
```
NGINX container only serves React App's production build.

Return to root directory and build container:

```
	docker-compose build
	docker-compose up
```

## For Production

1. In the Dockerfile, uncomment the line `ADD . /var/www` . This ensures the contents of the directory is copied into the container.
2. Modify ONLY the request URLs from React; change them from `localhost:8000/django/a/b/c` to `your-server.com/django/a/b/c`.
3. Modify .env files accordingly.

# Note

### Modifications to Django

In settings.py, we have to add the following to allow NGINX to serve the files correctly.
```
	FORCE_SCRIPT_NAME = '/django'
	STATIC_URL = '/django_static/'
	STATIC_ROOT = os.path.abspath('/var/www/django_static') 

	MEDIA_URL = '/media/'
	MEDIA_ROOT = os.path.abspath('/var/www/media/')
```
These are explained in comments in settings.py.

### Important details:

1. React Router should be able to handle subpaths correctly e.g. given a subpath /a/b/c/d it routes to the correct 
2. React App must not have any subpaths that conflict with NGINX instructions i.e. /django, /django_static or /media.

### For consideration

1. Should `npm run build` be included in entrypoint script?


### Useful links

To inspect a container:

```	
	docker exec -it <container-id> /bin/sh
```

Useful links:
	
	https://serverfault.com/questions/562756/how-to-remove-the-path-with-an-nginx-proxy-pass
