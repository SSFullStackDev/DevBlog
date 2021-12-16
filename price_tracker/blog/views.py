from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {})
def about(request):
    return render(request, 'about.html', {})
def projects(request):
    return render(request, 'projects.html', {})
def post(request):
    return render(request, 'post.html', {})
def edu(request):
    return render(request, 'edu.html', {})
