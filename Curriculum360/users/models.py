from django.db import models
from django.contrib.auth.models import User
from mainapp.models import *
# Create your models here.

class student(User):
    bio = models.TextField()
    profile_pic = models.ImageField(default='')
    department  = models.ForeignKey(department, on_delete=models.CASCADE)
    batch = models.IntegerField()

class instructor(User):
    bio = models.TextField()
    profile_pic = models.ImageField(default='')
    qualification = models.CharField(max_length=300)

class admins (User):
    bio = models.TextField()
    profile_pic = models.ImageField(default='')
    qualification = models.CharField(max_length=300)