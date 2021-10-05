from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.home, name="tracker-home"),
]
