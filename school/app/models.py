from django.db import models

# Create your models here.

class School(models.Model):
    school_name=models.CharField(max_length=50,primary_key=True)
    def __str__(self):
        return self.school_name

class Student(models.Model):
    school_name=models.ForeignKey(School,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    rollno=models.IntegerField()
    phno=models.IntegerField()
    email=models.EmailField()
    #email=models.EmailField(default='Abhisek@gmail.com')
    def __str__(self):
        return self.name
    def __str__(self):
        return self.rollno
    def __str__(self):
        return self.phno    
    def __str__(self):
        return self.email