from django.urls import path

from . import views

urlpatterns = [
    path('', views.renderHTML, name='renderHTML'),
    path('<subpath>/', views.renderHTML, name='renderHTML'),
]