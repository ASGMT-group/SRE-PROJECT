from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(department)
admin.site.register(course)
admin.site.register(semister)
admin.site.register(school)
admin.site.register(resource)
admin.site.register(comment)
