from django.shortcuts import render

# Create your views here.
def filters(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'chandan ANd AbhiSek Same', 'dt':dt, 'c':1}
    return render(request,'filters.html',d)
def myfilters(request):
    d={'data':'chandan ANd AbhiSek Same'}
    return render(request,'myfilters.html',d)