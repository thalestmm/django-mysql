from django.db import models
from django.utils import timezone


class Instructor(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    profile_photo = models.ImageField(null=True, blank=True) # TODO: Implement static file upload and serving
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
    lecture_text = models.TextField(max_length=1000, blank=True, null=True) # TODO: Implement markdown formatting

    class Meta:
        abstract = True
        ordering = ['module', 'index', 'name']
    
    def __str__(self):
        return str(str(self.module) + ' - ' + self.name)


# TODO: Add specific icons for each lecture type
class VideoLecture(BaseLecture):
    video_url = models.URLField(null=True) # TODO: Choose proper video delivery method


class TextLecture(BaseLecture):
    pass


class Question(BaseLecture):
    question_text = models.TextField(max_length=500)

    alt_a = models.CharField(max_length=50)
    alt_b = models.CharField(max_length=50)
    alt_c = models.CharField(max_length=50)
    alt_d = models.CharField(max_length=50)

    helper_text_a = models.TextField(max_length=200, null=True, blank=True)
    helper_text_b = models.TextField(max_length=200, null=True, blank=True)
    helper_text_c = models.TextField(max_length=200, null=True, blank=True)
    helper_text_d = models.TextField(max_length=200, null=True, blank=True)

    correct_alternative = models.CharField(max_length=1,
                                           choices=[(value, value) for value in 'ABCD'],
                                           default='A')