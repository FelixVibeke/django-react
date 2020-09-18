from django.urls import path
from . import views

"""
	TODO: 
	1. Add URL subpaths here.
	2. Write functions in views.py to handle the various subpaths that you added.
"""

urlpatterns = [
    path('', views.basePage, name='basePage'),
    path('<subpath>/', views.withSubpath, name='withSubpath'),
]