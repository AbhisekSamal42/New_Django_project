from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView,DetailView
from app.models import *

class SchoolList(ListView):
    model=School
    context_object_name='schools'

class StudentList(ListView):
    model=Student
    context_object_name='stus'

class SchoolDetails(DetailView):
    model=School