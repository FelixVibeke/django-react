# docker-nginx-simple
Simplest possible Nginx webserver running on top of Alpine Linux in a container

[Nginx](http://nginx.org) is a powerfull web server.

This container may be used to deliver static content only.

# Building the container

Clone this repository, go into the directory and run a command like: `docker build --tag nginx-simple .`

One can also use the docker-compose.yml file provided here: `docker-compose build`

# Using the container

## Normal usage

Use a command like this one:

  `docker run --detach --rm=true --volumes ./wwwroot/:/var/www/ --name=nginx --hostname=nginx nginx-simple`

Or use docker-compose:

  `docker-compose up -d`

## Debugging

Use a command like this one:

  `docker run -it --rm=true --volumes ./wwwroot/:/var/www/ --name=nginx --hostname=nginx --entrypoint=sh nginx-simple`

Or use docker-compose:

  `docker-compose up`


