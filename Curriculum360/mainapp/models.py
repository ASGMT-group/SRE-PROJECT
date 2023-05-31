from django.db import models


class course(models.Model):
    course_name = models.CharField(max_length=200, null=False , blank=False)
    course_code = models.CharField(max_length=15, null=True , blank=True)
    Description = models.TextField()
    likes = models.IntegerField()
   # prerequest = models.ForeignKey(course, on_delete=model) 

    def __str__(self):
        return self.course_name

class semister(models.Model):
    semister_number = models.IntegerField(null= False, blank=False)
    year = models.IntegerField(null=False, blank=False)
    courses= models.ManyToManyField(course)


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
    