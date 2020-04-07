FROM python

RUN pip install uwsgi
RUN pip install gunicorn
RUN pip install Django
RUN apt-get update
RUN apt-get install -y nginx
ADD nginx.conf /etc/nginx/nginx.conf
ADD nginx.default /etc/nginx/conf.d/default.conf

#set shared directory to working directory
WORKDIR /var/www

ENTRYPOINT ["/var/www/entrypoint.sh"]
CMD ["nginx"]
