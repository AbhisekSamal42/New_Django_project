from django.urls import path
from app.views import *


urlpatterns = [
    path('',students,name='students'),
]