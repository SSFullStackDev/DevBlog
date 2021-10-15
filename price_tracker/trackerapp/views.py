from django.shortcuts import render
from django.http import HttpResponse
from .models import price_history
from .forms import DataForm
from django.views.decorators.csrf import csrf_exempt

def home(request):
    data = price_history.objects.all
    return render(request, "trackerapp/home.html", {"data": data})


def about(request):
    return render(request, "trackerapp/about.html")

@csrf_exempt
def track_item(request):
    if request.method == "POST":
        form = DataForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request,'trackerapp/track_item.html', {})
    else:
        return render(request, "trackerapp/track_item.html", {})


def track(request):
    return render(request, "track.html", {})
