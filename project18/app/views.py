from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
from app.forms import *

def insert_Topic(request):
    EMFTO=TopicModelForm()
    d={'EMFTO':EMFTO}
    if request.method=='POST':
        TMFDO=TopicModelForm(request.POST)
        if TMFDO.is_valid():
            TMFDO.save()
            return HttpResponse('Topic is created')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'insert_Topic.html',d)
def insert_Webpage(request):
    EMFWO=WebPageModelForm()
    d={'EMFWO':EMFWO}
    if request.method=='POST':
        WMFDO=WebPageModelForm(request.POST)
        if WMFDO.is_valid():
            WMFDO.save()
            return HttpResponse('WebPage is created')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'insert_Webpage.html',d)
def insert_Accessrecord(request):
    EMFAO=AccessRecordModelForm()
    d={'EMFAO':EMFAO}
    if request.method=='POST':
        AMFDO=AccessRecordModelForm(request.POST)
        if AMFDO.is_valid():
            AMFDO.save()
            return HttpResponse('AccessRecord is created')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'insert_Accessrecord.html',d)
