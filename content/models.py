from django.db import models
from django.utils import timezone

# Create your models here.

class Instructor(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 

# Abstract model for all things related to content
class BaseContent(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300, null=True, blank=True)
    visible = models.BooleanField(default=True)
    index = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['name', 'index']

    def __str__(self):
        return self.name


class Area(BaseContent):
    pass


class Course(BaseContent):
    instructor = models.ForeignKey("Instructor", on_delete=models.SET_NULL, null=True) 
    area = models.ForeignKey("Area", on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['area', 'index', 'name']


class Module(BaseContent):
    course = models.ForeignKey("Course", on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['course', 'index', 'name']

# Specific abstract model for classes (there will be different types of classes)
class BaseLecture(BaseContent):
    module = models.ForeignKey("Module", on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True
        ordering = ['module', 'index', 'name']


class VideoLecture(BaseLecture):
    video_url = models.URLField(null=True) # TODO: Choose proper video delivery method

