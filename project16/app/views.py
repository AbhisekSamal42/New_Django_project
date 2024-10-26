from django.shortcuts import render

# Create your views here.

from app.forms import *
from django.http import HttpResponse


def student_djf(request):
    ESFO=StudentForm()
    D={'ESFO':ESFO}

    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            return HttpResponse(str(SFDO.cleaned_data))
        else:
            return HttpResponse('Invalid data')
    return render(request,'student_djf.html',D)