FROM python

RUN apt-get update
RUN apt-get install -y nginx
RUN apt-get install -y nodejs

ADD nginx.conf /etc/nginx/nginx.conf
ADD nginx.default /etc/nginx/conf.d/default.conf

ADD requirements.txt /var/www/requirements.txt
RUN pip install -U -r /var/www/requirements.txt

ADD . /var/www

#set shared directory to working directoryi;
WORKDIR /var/www


ENTRYPOINT ["/var/www/entrypoint.sh"]
CMD ["nginx"]
