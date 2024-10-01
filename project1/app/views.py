from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def longBoot(request):
    return HttpResponse('This is a good pub for drinks')