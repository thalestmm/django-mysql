from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Instructor)
admin.site.register(Area)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(VideoLecture)