from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def renderHTML(request, subpath=''):
	soup = getSoup()

	print(subpath)
	print("above is subpath")
	setMetaTags(soup, subpath)
	return HttpResponse(soup.prettify())

#Use this function to set meta tags in soup
def insertMetaTag(soup, property, content):
	new_meta = soup.new_tag('meta', property=property, content=content)
	soup.head.append(new_meta)

#Get soup object from index.html
def getSoup():
	with open("/var/www/react/build/index.html") as fp:
		soup = BeautifulSoup(fp)
	return soup


"""
	Todo: modify only this function!
"""
def setMetaTags(soup, subpath):
	"""
		INSERT CODE HERE: example shown
	"""

	if subpath=='':
		insertMetaTag(soup, "og:title", "dailybruin")
	else:
		insertMetaTag(soup, "og:title", subpath)
	return