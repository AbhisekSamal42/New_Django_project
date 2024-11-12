from django.shortcuts import render

# Create your views here.

from app.forms import *

def registration(request):
    EUFO=UserForm()
    EPFO=ProfileForm()
    D={'EUFO':EUFO,'EPFO':EPFO}
    return render(request,'registration.html',D)