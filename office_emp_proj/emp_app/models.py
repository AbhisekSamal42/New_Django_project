from django.db import models

class Department(models.Model):
    dept_name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.dept_name

class Role(models.Model):
    role_name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.role_name

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dept_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField()
    bonus = models.IntegerField()
    role_name = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone_no = models.BigIntegerField()
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
