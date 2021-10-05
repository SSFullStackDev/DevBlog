from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="tracker"),
    path("about/", views.about, name="tracker-about"),
]
