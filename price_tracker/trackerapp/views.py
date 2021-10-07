from django.shortcuts import render
from django.http import HttpResponse
from .models import price_history


def home(request):
    data = price_history.objects.all
    return render(request, "trackerapp/home.html", {"data": data})


def about(request):
    return render(request, "trackerapp/about.html")
