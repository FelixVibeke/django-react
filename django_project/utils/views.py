from bs4 import BeautifulSoup, Tag
from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache
import logging

# Create your views here.

"""
	DO NOT MODIFY THESE FUNCTIONS!!
"""
#Use this function to set og meta tags in soup
def insert_meta_prop(soup, property, content):
	new_meta = soup.new_tag('meta', property=property, content=content)
	soup.head.append(new_meta)

#Use this function to set twitter meta tags in soup
def insert_meta_name(soup, name, content):
	new_meta = Tag(builder=soup.builder, name='meta', 
               attrs={'name':name,'content':content})

	#new_meta = soup.new_tag('meta', name=name, content=content)
	soup.head.append(new_meta)

#Get soup object from index.html
def get_soup():
	soup = cache.get('index_base')
	return soup

#Insert full set of tags to a single soup object 
def insert_all_tags(soup, title=None, image_link=None, description=None, url=None, site_name=None):

	# DEFAULT TAGS

	insert_meta_prop(soup, "og:locale", "en_US")
	insert_meta_prop(soup, "og:type", "article")
	insert_meta_prop(soup, "article:publisher", "https://www.facebook.com/dailybruin")
	insert_meta_name(soup, "twitter:site", "@dailybruin")
	insert_meta_name(soup, "twitter:creator", "@dailybruin")
	insert_meta_name(soup, "twitter:card", "summary_large_image")

	# OPTIONAL TAGS

	if title:
		insert_meta_prop(soup, "og:title", title)
		insert_meta_name(soup, "twitter:title", title)

	if description:
		insert_meta_prop(soup, "og:description", description)
		insert_meta_name(soup, "twitter:description", description)

	if url:
		""""
		important to remove /django/utils, which exists in the internal URL within the container,
		but not outside
		"""
		insert_meta_prop(soup, "og:url", url.replace("/django/utils",""))

	if image_link:
		insert_meta_prop(soup, "og:image", image_link)
		insert_meta_name(soup, "twitter:image", image_link)


	if site_name:
		insert_meta_prop(soup, "og:site_name", site_name)
	else:
		insert_meta_prop(soup, "og:site_name", "Daily Bruin")


"""
	MODIFICATIONS ONLY BELOW THIS LINE

	TODO: 
	1. If you haven't already done so, add URL subpaths in urls.py.
	2. Write functions here to handle the various subpaths that you added.


	Writing functions:
	1. Call get_soup() to get the soup object.
	2. Use insert_all_tags() to insert meta tags into the soup object.
	3. Return the modified soup object as a HttpResponse.
"""

#View meta tags at http://localhost:8000
def base_page(request):
	#Get soup object
	soup = get_soup()


	"""
	Insert meta tags in a try catch block.
	If insertion fails, we do not want it to affect main functionality
	"""
	try:
		#Gather useful information from request
		http_host = request.META['HTTP_HOST']
		url = request.build_absolute_uri()

		title = "Daily Bruin Starter Code"
		description = "Deploy the container, then go to the website on your browser \
			and find me in element."

		#Insert whatever relevant information we want
		insert_all_tags(soup, description=description, title=title, url=url)
	
	except Exception as e:
		logger = logging.getLogger(__name__)
		logger.error("Error occured with %s", "setting meta tags", exc_info=e)

	#Return soup object
	return HttpResponse(soup.prettify())


#View the meta tags at http://localhost:8000/post/4
def post_page(request, post_id):
	#Get soup object
	soup = get_soup()

	"""
	Insert meta tags in a try catch block.
	If insertion fails, we do not want it to affect main functionality
	"""
	try:
		#Gather useful information from request
		http_host = request.META['HTTP_HOST']
		url = request.build_absolute_uri()

		title = "Post Page for post id {post_id}".format(post_id=post_id)
		description = "Deploy the container, then go to the website on your browser \
			and find me in element."

		#Insert whatever relevant information we want to have in meta tags
		insert_all_tags(soup, description=description, title=title, url=url)
	
	except Exception as e:
		logger = logging.getLogger(__name__)
		logger.error("Error occured with %s", "setting meta tags", exc_info=e)

	#Return soup object
	return HttpResponse(soup.prettify())


#View the meta tags at http://localhost:8000/data/tommy/2018-09-03
def data_page(request, user, date):
	#Get soup object
	soup = get_soup()

	"""
	Insert meta tags in a try catch block.
	If insertion fails, we do not want it to affect main functionality
	"""
	try:
		#Gather useful information from request
		http_host = request.META['HTTP_HOST']
		url = request.build_absolute_uri()

		title = "Data Page for user {user} on {date}".format(user=user, date=date)
		description = "Deploy the container, then go to the website on your browser \
			and find me in element."

		#Insert whatever relevant information we want to have in meta tags
		insert_all_tags(soup, description=description, title=title, url=url)
	
	except Exception as e:
		logger = logging.getLogger(__name__)
		logger.error("Error occured with %s", "setting meta tags", exc_info=e)

	#Return soup object
	return HttpResponse(soup.prettify())