from django.db import models


class course(models.Model):
    course_name = models.CharField(max_length=200, null=False , blank=False)
    course_code = models.CharField(max_length=15, null=True , blank=True)
    Description = models.TextField()
    likes = models.IntegerField()

    def __str__(self):
        return self.course_name



class department (models.Model):

    
    Departement_name   = models.CharField(max_length=200 )
    description = models.TextField()
    course_list  = models.ManyToManyField(course)

    def __str__(self):
        return self.Departement_name

