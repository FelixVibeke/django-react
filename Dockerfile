FROM python

#RUN pip install pipenv --no-cache-dir
#RUN pipenv install --deploy --system


RUN pip install uwsgi
RUN pip install gunicorn
#RUN apk -U add nginx
#RUN apk - build-essential python-dev
#RUN pip install pipenv --no-cache-dir
RUN apt-get update
RUN apt-get install -y nginx
ADD nginx.conf /etc/nginx/nginx.conf
ADD nginx.default /etc/nginx/conf.d/default.conf

EXPOSE 8000

WORKDIR /var/www
COPY /wwwroot /var/www/

RUN chmod 777 -R /var/www/entrypoint.sh

ENTRYPOINT ["/var/www/entrypoint.sh"]
CMD ["nginx"]
