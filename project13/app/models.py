from django.db import models

# Create your models here.
class DEPT(models.Model):
    DEPTNO=models.IntegerField(primary_key=True)
    DNAME=models.CharField(max_length=14)
    LOC=models.CharField(max_length=13)

    
    def __str__(self):
        return str(self.DEPTNO)
    
  
class EMP(models.Model):
    EMPNO=models.IntegerField(primary_key=True)
    ENAME=models.CharField(max_length=10)
    JOB=models.CharField(max_length=9)
    MGR=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    HIREDATE=models.DateField()
    SAL=models.FloatField(max_length=7)
    COMM=models.FloatField(max_length=7,null=True,blank=True)
    DEPTNO=models.ForeignKey(DEPT,on_delete=models.CASCADE)
   
    
    def __str__(self):
        return self.ENAME
   
class BONUS(models.Model):
    ENAME=models.CharField(max_length=10)
    JOB=models.CharField(max_length=9)
    SAL=models.IntegerField()
    COMM=models.IntegerField()

    def __str__(self):
        return self.ENAME
  
class SALGRADE(models.Model):
    GRADE=models.IntegerField()
    LOSAL=models.IntegerField()
    HISAL=models.IntegerField()

    def __str__(self):
        return str(self.GRADE)
    