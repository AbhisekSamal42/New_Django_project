from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import*
from django.db.models.functions import Length

def insert_Product_Category(request):
    pc_id=input("Enter product category id: ")
    PCO=Product_Category.objects.get_or_create(PC_id=pc_id)
    pt=input("Enter product type: ")
    PTO=Product_Category.objects.get_or_create(PC_type=pt)
 

    if PCO[1]:
        Product_Categorys=Product_Category.objects.all()
        D={'Product_Categorys':Product_Categorys}
        return render(request,'display_Product_Categorys.html',D)
        #return HttpResponse("New object is created.")
    else:
        return HttpResponse("Dear user the Product Category is already exist.")
    
 
    
def insert_Product(request):
    p_id=input("Enter product id: ")
    p_name=input("Enter product name: ")
    P_price=input("Enter product price: ")
    Date=input("Enter mf date: ")
    Place=input("Enter mf place: ")
    pc_id=input("Enter product category id: ")
    PCO=Product_Category.objects.get(PC_id=pc_id)
    PO=Product.objects.get_or_create(PC_id=PCO,P_id=p_id,P_name=p_name,Price=P_price,MF_date=Date,MF_place=Place)[0]


    if PO:
        Products=Product.objects.all()
        D={'Products':Products}
        return render(request,'display_Products.html',D)
        #return HttpResponse("Product is created.")
    else:
        return HttpResponse("Dear user the Product is already exist.")
    

def display_Product_Categorys(request):
    Product_Categorys=Product_Category.objects.all()
    D={'Product_Categorys':Product_Categorys}
    return render(request,'display_Product_Categorys.html',D)


def display_Products(request):
    Products=Product.objects.all()
    D={'Products':Products}
    return render(request,'display_Products.html',D)