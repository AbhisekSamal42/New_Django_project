from django.db import models

# Create your models here.
class Product_Category(models.Model):
    PC_id=models.IntegerField(primary_key=True)
    PC_type=models.CharField(max_length=30)

    def __str__(self):
        return self.PC_id
    def __str__(self):
        return self.PC_type
    
class Product(models.Model):
    P_id=models.IntegerField(primary_key=True)
    P_name=models.CharField(max_length=30)
    Price=models.IntegerField()
    MF_date=models.DateField()
    MF_place=models.CharField(max_length=30)
    PC_id=models.ForeignKey(Product_Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.P_id
    def __str__(self):
        return self.P_name
    def __str__(self):
        return self.Price
    def __str__(self):
        return self.MF_date
    def __str__(self):
        return self.MF_place
    
    
    