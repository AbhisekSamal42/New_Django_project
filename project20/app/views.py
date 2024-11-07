from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from app.models import *
from app.forms import *

def insert_Student(request):
    EMFSO=StudentModelForm()
    d={'EMFSO':EMFSO}
    if request.method=='POST':
        SMFDO=StudentModelForm(request.POST)
        if SMFDO.is_valid():
            SMFDO.save()
            return HttpResponse('Student data is created')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'insert_Student.html',d)