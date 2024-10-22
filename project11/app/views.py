from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import*
from django.db.models.functions import Length
from django.db.models import Q

def insert_Topic(request):
    tn=input("Enter topic name: ")
    TO=Topic.objects.get_or_create(topic_name=tn)

    if TO[1]:
        Topics=Topic.objects.all()
        D={'Topics':Topics}
        return render(request,'display_Topics.html',D)
        #return HttpResponse("New object is created.")
    else:
        return HttpResponse("Dear user the Topic is already exist.")
    
def insert_Webpage(request):
    tn=input("Enter topic name: ")
    Name=input("Enter name: ")
    Url=input("Enter url: ")
    Email=input("Enter email: ")
    TO=Topic.objects.get(topic_name=tn)
    WO=Webpage.objects.get_or_create(topic_name=TO,name=Name,url=Url,email=Email)[0]
    
    if WO:
        Webpages=Webpage.objects.all()
        D={'Webpages':Webpages}
        return render(request,'display_Webpages.html',D)
        #return HttpResponse("Webpage is created.")
    else:
        return HttpResponse("Dear user the webpage is already exist.")
    
def insert_Accessrecord(request):
    tn=input("Enter topic name: ")
    Name=input("Enter name: ")
    Url=input("Enter url: ")
    Email=input("Enter email: ")
    Author=input("Enter author name: ")
    Date=input("Enter date: ")
    WO=Webpage.objects.get(name=Name)
    AO=Accessrecord.objects.get_or_create(name=WO,author=Author,date=Date)

    if AO: 
        Accessrecords=Accessrecord.objects.all()
        D={'Accessrecords':Accessrecords}
        return render(request,'display_Accessrecords.html',D)
        #return HttpResponse("Webpage is created.")
    else:
        return HttpResponse("Dear user the Accessrecord is already exist.")
    

def display_Topics(request):
    # Topics=Topic.objects.order_by('topic_name')
    # Topics=Topic.objects.order_by('-topic_name')
    # Topics=Topic.objects.order_by(Length('topic_name'))
    # Topics=Topic.objects.order_by(Length('topic_name').desc())
    # Topics=Topic.objects.exclude(topic_name='Java')
    # Topics=Topic.objects.filter(topic_name__startswith='J')
    # Topics=Topic.objects.filter(topic_name__endswith='t')
    # Topics=Topic.objects.filter(topic_name__in=('Java','Python'))
    # Topics=Topic.objects.filter(topic_name__contains='n')
    # Topics=Topic.objects.filter(topic_name__regex=r'h')
    Topics=Topic.objects.all()
    D={'Topics':Topics}
    return render(request,'display_Topics.html',D)
    

def display_Webpages(request):
    # Webpages = Webpage.objects.order_by('name')
    # Webpages = Webpage.objects.order_by('-name')
    # Webpages = Webpage.objects.order_by(Length('name'))
    # Webpages = Webpage.objects.order_by(Length('name').desc())
    # Webpages = Webpage.objects.exclude(name='Smruti')
    Webpages = Webpage.objects.filter(Q(name__startswith='S') & Q(url__endswith='in'))
    Webpages = Webpage.objects.filter(name__startswith='sa',url__endswith='in')
    Webpages = Webpage.objects.filter(Q(name__startswith='s') | Q(url__endswith='in'))
    #Webpages=Webpage.objects.all()
    D={'Webpages':Webpages}
    return render(request,'display_Webpages.html',D)


def display_Accessrecords(request):
    # Accessrecords=Accessrecord.objects.order_by('author')
    # Accessrecords=Accessrecord.objects.order_by('-author')
    # Accessrecords=Accessrecord.objects.order_by(Length('author'))
    # Accessrecords=Accessrecord.objects.order_by(Length('author').desc())
    # Accessrecords=Accessrecord.objects.exclude(author='James Gosling')
    # Accessrecords=Accessrecord.objects.filter(date__gt='1995-05-15')
    # Accessrecords=Accessrecord.objects.filter(date__lt='1995-05-15')
    # Accessrecords=Accessrecord.objects.filter(date__gte='1995-05-15')
    # Accessrecords=Accessrecord.objects.filter(date__lte='1995-06-15')
    # Accessrecords=Accessrecord.objects.filter(date__month='12')
    # Accessrecords=Accessrecord.objects.filter(date__year='1995')
    # Accessrecords=Accessrecord.objects.filter(date__day='15')
    # Accessrecords=Accessrecord.objects.filter(date__day='12')
    Accessrecords=Accessrecord.objects.all()
    D={'Accessrecords':Accessrecords}
    return render(request,'display_Accessrecords.html',D)




def upadate_Webpage(request):
    Webpage.objects.filter(topic_name='Sql').update(email='priyaranjan12@gmail.com')
    Webpage.objects.filter(topic_name='Python').update(email='abhisek42@gmail.com')
    Webpage.objects.filter(topic_name='Python').update(url='https://abhiseksamal.in')
    Webpage.objects.update_or_create(name='Suvendu',defaults={'url':'https://css.in'})

    TO=Topic.objects.get(topic_name='Java')
    Webpage.objects.update_or_create(name='Partha',defaults={'topic_name':TO})

    TO=Topic.objects.get(topic_name='Html')
    Webpage.objects.update_or_create(name='Smruti',defaults={'topic_name':TO})

    Webpages=Webpage.objects.all()
    D={'Webpages':Webpages}
    return render(request,'display_Webpages.html',D)



def delete_Webpage(request):
    Webpage.objects.filter(topic_name='Sql').delete()
    Webpage.objects.filter(email='abhisek42@gmail.com').delete()

    Webpages=Webpage.objects.all()
    D={'Webpages':Webpages}
    return render(request,'display_Webpages.html',D)