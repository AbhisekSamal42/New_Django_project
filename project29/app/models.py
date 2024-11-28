from django.db import models

# Create your models here.
from django.urls import reverse

class School(models.Model):
    scname=models.CharField(max_length=100)
    scprincipal=models.CharField(max_length=100)
    sclocation=models.CharField(max_length=100)

    def __str__(self):
        return self.scname
    
    def get_absolute_url(self):
        return reverse('SchoolDetail',kwargs={'pk':self.pk})
    
class Student(models.Model):
    stname=models.CharField(max_length=100)
    stage=models.IntegerField()
    scname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')

    def __str__(self):
        return self.stname