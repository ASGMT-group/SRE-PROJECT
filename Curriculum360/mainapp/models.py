from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
#User = settings.AUTH_USER_MODEL
class resource(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(null=False, blank=False, upload_to= 'static/material')

    def __str__(self):

        return self.name

class comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

class course(models.Model):
    course_name = models.CharField(max_length=200, null=False , blank=False)
    course_code = models.CharField(max_length=15, null=True , blank=True)
    Description = models.TextField()
    likes = models.IntegerField(default=0)
    comments = models.ManyToManyField(comment)
    books = models.ManyToManyField(resource)
    course_outline = models.FileField(null=True,upload_to='static/outline' )
   
    def __str__(self):
        return self.course_name

class semister(models.Model):
    semister_no = models.IntegerField(null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)
    courses= models.ManyToManyField(course)
    

    def __str__(self) -> str:
        return self.semister_name


class department (models.Model):

    
    Departement_name   = models.CharField(max_length=200 )
    description = models.TextField()
    Semisters  = models.ManyToManyField(semister)

    def __str__(self):
        return self.Departement_name
    
class school(models.Model):
    school_name =models.CharField(max_length=300)
    department = models.ManyToManyField(department)
    about = models.TextField(null = False, blank=False)
    blog = models.TextField(default=about)
    semisters = models.ManyToManyField(semister)

    def __str__(self):
        return self.school_name
    