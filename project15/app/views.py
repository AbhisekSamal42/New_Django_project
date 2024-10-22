from django.shortcuts import render

# Create your views here.
from app.models import *

from django.http import HttpResponse

def insertTopic(request):

    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)
        return HttpResponse('Topic is Created')

    return render(request,'insertTopic.html')


def insertWebpage(request):
    LTO=Topic.objects.all()
    D={'LTO':LTO}

    if request.method=='POST':
        tn=request.POST['tn']
        nm=request.POST['nm']
        ul=request.POST['ul']
        em=request.POST['em']
        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=nm,url=ul,email=em)
        return HttpResponse('Webpage is created')
    return render(request,'insertWebpage.html',D)


def insertAccessrecord(request):
    LWO=Webpage.objects.all()
    D={'LWO':LWO}

    if request.method=='POST':
        nm=request.POST['nm']
        au=request.POST['au']
        dt=request.POST['dt']
        WO=Webpage.objects.get(id=nm)
        AO=Accessrecord.objects.get_or_create(name=WO,author=au,date=dt)
        return HttpResponse('Accessrecord is created')
    return render(request,'insertAccessrecord.html',D)
