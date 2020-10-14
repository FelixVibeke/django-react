from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache
# Create your views here.

"""
	DO NOT MODIFY THESE TWO FUNCTIONS!!
"""
#Use this function to set meta tags in soup
def insert_meta_tag(soup, property, content):
	new_meta = soup.new_tag('meta', property=property, content=content)
	soup.head.append(new_meta)

#Get soup object from index.html
def get_soup():
	soup = cache.get('index_base')
	return soup

"""
	MODIFICATIONS ONLY BELOW THIS LINE

	TODO: 
	1. If you haven't already done so, add URL subpaths in urls.py.
	2. Write functions here to handle the various subpaths that you added.


	Writing functions:
	1. Call get_soup() to get the soup object.
	2. Use insert_meta_tag() to insert the soup object.
	3. Return the modified soup object as a HttpResponse.
"""
def base_page(request):
	#Get soup object
	soup = get_soup()
	#Insert a meta tag
	insert_meta_tag(soup, "og:title", "dailybruin1")
	#Return soup object
	return HttpResponse(soup.prettify())

#View the meta tags at http://localhost:8000/post/4
def post_page(request, post_id):
	#Get soup object
	soup = get_soup()
	#Insert a meta tag
	insert_meta_tag(soup, "og:title", "this is post page number " + str(post_id))
	#Return soup object
	return HttpResponse(soup.prettify())


#View the meta tags at http://localhost:8000/data/tommy/2018-09-03
def data_page(request, user, date):
	#Get soup object
	soup = get_soup()
	#Insert a meta tag
	insert_meta_tag(soup, "og:title", "this is data page for " + user + " on " + date)
	#Return soup object
	return HttpResponse(soup.prettify())