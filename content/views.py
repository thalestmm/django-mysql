from django.shortcuts import render
from django.http import HttpResponse

# Local imports
from .models import Course, Area

# Create your views here.

def index(request):
    return HttpResponse("Content app")