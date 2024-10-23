from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import*


def insertSchool(request):

    if request.method=='POST':
        sn=request.POST['sn']
        SO=School.objects.get_or_create(school_name=sn)
        return HttpResponse('School name is created')
    
    return render(request,'insertSchool.html')


def insertStudent(request):
    LSO=School.objects.all()
    D={'LSO':LSO}

    if request.method=='POST':
        sn=request.POST['sn']
        nm=request.POST['nm']
        rn=request.POST['rn']
        pn=request.POST['pn']
        em=request.POST['em']
        SO=School.objects.get(school_name=sn)
        STUO=Student.objects.get_or_create(school_name=SO,name=nm,rollno=rn,phno=pn,email=em)
        return HttpResponse('Student detail is created')
    
    return render(request,'insertStudent.html',D)


def select_Multiple(request):
    LSO=School.objects.all()
    D={'LSO':LSO}

    if request.method=='POST':
        MSN=request.POST.getlist('sn')
        EQSS=Student.objects.none()
        for school in MSN:
            EQSS=EQSS|Student.objects.filter(school_name=school)
        D1={'EQSS':EQSS}
        return render(request,'display_Student.html',D1)
    
    return render(request,'select_Multiple.html',D)


def Checkbox(request):
    LSO=School.objects.all()
    D={'LSO':LSO}

    return render(request,'Checkbox.html',D)