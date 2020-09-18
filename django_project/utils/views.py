from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache
# Create your views here.

"""
	DO NOT MODIFY THESE TWO FUNCTIONS!!
"""
#Use this function to set meta tags in soup
def insertMetaTag(soup, property, content):
	new_meta = soup.new_tag('meta', property=property, content=content)
	soup.head.append(new_meta)

#Get soup object from index.html
def getSoup():
	soup = cache.get('index_base')
	return soup

"""
	MODIFICATIONS ONLY BELOW THIS LINE

	TODO: 
	1. If you haven't already done so, add URL subpaths in urls.py.
	2. Write functions here to handle the various subpaths that you added.


	Writing functions:
	1. Call getSoup() to get the soup object.
	2. Use insertMetaTag() to insert the soup object.
	3. Return the modified soup object as a HttpResponse.
"""
def basePage(request):
	#Get soup object
	soup = getSoup()
	#Insert a meta tag
	insertMetaTag(soup, "og:title", "dailybruin1")
	#Return soup object
	return HttpResponse(soup.prettify())

def withSubpath(request, subpath):
	#Get soup object
	soup = getSoup()
	#Insert a meta tag
	insertMetaTag(soup, "og:title", subpath)
	#Return soup object
	return HttpResponse(soup.prettify())