"""
URL configuration for project14 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app.views import*
urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert_Product_Category/',insert_Product_Category,name='insert_Product_Category'),
    path('insert_Product/',insert_Product,name='insert_Product'),
    path('display_Product_Categorys/',display_Product_Categorys,name='display_Product_Categorys'),
    path('display_Products/',display_Products,name='display_Products'),
]