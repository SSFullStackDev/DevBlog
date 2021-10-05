from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Tracker Home is Up!!!</h1>")


def about(request):
    return HttpResponse("<h1>About My Tracker!</h1>")
