from django.shortcuts import render
from django.http import HttpResponse

# from .model import Movie

def index(request):
    return render(request, 'frontend/index.html')