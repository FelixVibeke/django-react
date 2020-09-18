from django.urls import path
from . import views

"""
	TODO: 
	1. Add URL subpaths here.
	2. Write functions in views.py to handle the various subpaths that you added.

	Examples of other subpaths cound be:
    - path('post/<post_id>', views.posts, name='posts')
    - path('data/<date>/<time>', views.data, name='data')
	And then we would need to define the methods post(post_id) and data(date,time) in views.py to return the correct HttpResponse.
"""

urlpatterns = [
    path('', views.basePage, name='basePage'),
    path('<subpath>/', views.withSubpath, name='withSubpath'),
]