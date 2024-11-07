from django.db import models

# Create your models here.


from django.core.validators import *

class Student(models.Model):
    sname=models.CharField(max_length=20,primary_key=True)
    sid=models.IntegerField()
    semail=models.EmailField()