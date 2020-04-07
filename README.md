# start.django-react

Fetch static files e.g. simple .html at localhost:8000/static/file1.html

Fetch react app at localhost:8000/react/

Get django data at localhost:8000/django/

Trailing slash is necessary for /react/ and /django/

# How to use

Run this in the react directory to generate the production build:

```
	npm run build 
```

Return to root directory and build container:

```
	docker-compose build
	docker-compose up
```

## Note

### Modifications to React

We need to add `"homepage": "/react/",` to package.json to ensure all files are routed correctly.

### Modifications to Django

In settings.py, we add:
```
	ALLOWED_HOSTS = ['0.0.0.0','172.17.0.2','127.0.0.1', 'localhost']
	FORCE_SCRIPT_NAME = '/django'
```
### Outstanding issues:

1. CSS for Django's admin portal is not showing correctly.
2. React router is currently still untested (not sure if subpaths will map correctly)
3. Trailing slashes seem oddly necessary e.g. localhost:8000/react will not work, but localhost:8000/react/ does
4. Should `npm run build` be included in entrypoint script?


### Useful links

To inspect a container:

```	
	docker exec -it <container-id> /bin/sh
```

Useful links:
	
	https://serverfault.com/questions/562756/how-to-remove-the-path-with-an-nginx-proxy-pass
