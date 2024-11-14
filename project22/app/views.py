from django.shortcuts import render

# Create your views here.

from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
def registration(request):
    EUFO=UserForm()
    EPFO=ProfileForm()
    D={'EUFO':EUFO,'EPFO':EPFO}

    if request.method=="POST" and request.FILES:
        NMUFDO=UserForm(request.POST)
        NMPFDO=ProfileForm(request.POST,request.FILES)
        if NMUFDO.is_valid() and NMPFDO.is_valid():
            MUFDO=NMUFDO.save(commit=False)
            pw=NMUFDO.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()
            MPFDO=NMPFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()

            send_mail('Registration','Registration is Successfull','abhiseksamal36@gmail.com',[MUFDO.email],fail_silently=False)
            return HttpResponse("Registration is Successfull")
        else:
            return HttpResponse("Invalid data")
    
    return render(request,'registration.html',D)

   

