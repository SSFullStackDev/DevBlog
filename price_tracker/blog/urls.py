from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('home.html', views.home, name='home'),
    #path('about.html', views.about, name='about'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    #path('contact.html', views.contact, name='contact'),
    path('post/', views.post, name='post'),
    #path('post.html', views.post, name='post'),
    path('edu/', views.edu, name='edu'),
]
