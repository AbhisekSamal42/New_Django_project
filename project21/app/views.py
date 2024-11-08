from django.shortcuts import render

# Create your views here.


def filters(request):
    import datetime
    dt=datetime.datetime.now()

    D={'data':'Odisha is famous for Puri Jagannath temple','dt':dt,'c':2}
    return render(request,'filters.html',D)