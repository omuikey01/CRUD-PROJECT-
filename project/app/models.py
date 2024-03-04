from django.db import models

# Create your models here.

class AdminRegister(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)



class Course(models.Model):
    course_title = models.CharField(max_length=200)
    course_lession = models.CharField(max_length=200)
    course_fees = models.IntegerField()
    image = models.ImageField(upload_to="photos", null=True)
