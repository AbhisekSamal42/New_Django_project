from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import View # (class based view)
from app.forms import *

# Function based view for returning string as Response

def fbv_string(request):
    return HttpResponse('<h1>This function based views string.</h1>')

# Class based view for returning string as Response

class cbv_string(View):
    def get(self,request):
        return HttpResponse('<h1>This is class base view string.</h1>')


# Function based view for returning string as HTML page

def fbv_html(request):
    return render(request,'fbv_html.html')

# Class based view for returning string as HTML page

class cbv_html(View):
    def get(self,request):
        return render(request,'cbv_html.html')
    

# Inserting student in Function based view 

def insert_student_fbv(request):
    ESFO=StudentMF()
    D={'ESFO':ESFO}

    if request.method=='POST':
        SFDO=StudentMF(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Done')
        else:
            return HttpResponse('Invalid')
    return render(request,'insert_student_fbv.html',D)

# Inserting student in Class based view 


class cbvCreateStudent(View):
    def get(self,request):
        ESFO=StudentMF()
        D={'ESFO':ESFO}
        return render(request,'cbvCreateStudent.html',D)
    
    def post(self,request):
        SFDO=StudentMF(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Done')
        else:
            return HttpResponse('Invalid')