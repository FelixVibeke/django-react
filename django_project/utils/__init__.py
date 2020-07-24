from bs4 import BeautifulSoup
import logging

#logger = logging.getLogger("samplelogger")
soup = None

def init():
	with open("/var/www/react/build/index.html") as fp:
		soup = BeautifulSoup(fp)

#init()