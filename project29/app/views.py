from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,TemplateView,DetailView,CreateView,UpdateView,DeleteView
from app.models import *
from django.urls import reverse_lazy

class SchoolList(ListView):
    model=School
    #queryset=School.objects.all()
    context_object_name='schools'
    #template_name='app/school_list.html'
    #ordering=['scname']

class Home(TemplateView):
    template_name='app/home.html'

class SchoolDetail(DetailView):
    model=School
    context_object_name='scobject'


class SchoolCreate(CreateView):
    model=School
    fields='__all__'


class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'

class SchoolDelete(DeleteView):
    model=School
    context_object_name='schoolobject'
    success_url=reverse_lazy('SchoolList')