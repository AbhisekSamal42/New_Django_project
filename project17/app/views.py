from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
from app.forms import *

def insert_Topic(request):
    ETFO=TopicForm()
    D={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=request.POST['tn']
            TO=Topic.objects.get_or_create(topic_name=tn)
            return HttpResponse('Topic is Created')
        else:
            return HttpResponse('Topic is already Exist')
    return render(request,'insert_Topic.html',D)

def insert_Webpage(request):
    EWFO=WebpageForm()
    D={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            tn=request.POST['tn']
            nm=request.POST['nm']
            ul=request.POST['ul']
            el=request.POST['el']
            TO=Topic.objects.get(topic_name=tn)
            WO=Webpage.objects.get_or_create(topic_name=TO,name=nm,url=ul,email=el)
            return HttpResponse('Webpage is Created')
        else:
            return HttpResponse('Webpage is already Exist')
    return render(request,'insert_Webpage.html',D)

def insert_Accessrecord(request):
    EAFO=AccessrecordForm()
    D={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=AccessrecordForm(request.POST)
        if AFDO.is_valid():
            nm=request.POST['nm']
            au=request.POST['au']
            dt=request.POST['dt']
            WO=Webpage.objects.get(id=nm)
            AO=Accessrecord.objects.get_or_create(name=WO,author=au,date=dt)
            return HttpResponse('Accessrecord is Created')
        else:
            return HttpResponse('Accessrecord is already Exist')
    return render(request,'insert_Accessrecord.html',D)