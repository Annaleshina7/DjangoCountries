from django.shortcuts import render
from django.contrib.staticfiles import finders

# Create your views here.
def index(request):
    return render(request, "index.html")
