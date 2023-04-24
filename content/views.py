from django.shortcuts import render
from django.http import HttpResponse

# Local imports
from .models import Course, Area

# Create your views here.

def index(request):
    area_list = Area.objects.all()
    course_list = Course.objects.all()
    output = ", ".join([course.name for course in course_list])

    return render(request, 'content/base.html')