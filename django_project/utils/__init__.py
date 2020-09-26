import logging
from bs4 import BeautifulSoup
from django.core.cache import cache


#Get soup object from index.html
def set_soup_object():
	with open("/var/www/react/build/index.html") as fp:
		soup = BeautifulSoup(fp,features="html.parser")
	cache.set("index_base",soup,timeout=None)


logger = logging.getLogger(__name__)
set_soup_object()
logger.info("Cached index.html as BS object.")