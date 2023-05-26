from django.db import models

# Create your models here.
class student (models.Model):
    first_name = models.CharField(max_length=45, null=False)
    last_name = models.CharField(max_length=45, null=True, blank=True)
    bio = models.TextField()
    profile_pic = models.FileField() # ------storage discription
    batch = models.CharField(max_length=5)
    department = models.ForeignKey(department, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class course(models.Model):
    course_name = models.CharField(max_length=200, null=False , blank=False)
    course_code = models.CharField(max_length=15, null=True , blank=True)
    Description = models.TextField()
    likes = models.IntegerField()



class department (models.Model):

    dept_options = [
        ('CSE' , 'Computer Science Engineering')
        ('SE' , 'Software Engineering')
        ('ECE' , 'Electronics and communication Engineering')
        ('EPCE' , 'Electrical Power and Control Engineering')
    ]

    Departement_name   = models.CharField(max_length=200 , choices=dept_options)
    description = models.TextField()
    course_list  = models.ManyToManyField(course)

