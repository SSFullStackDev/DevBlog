from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="tracker"),
    path("about/", views.about, name="tracker-about"),
    path("track_item/", views.track_item, name="track_item"),
    path('track/', views.track, name="track"),
]
