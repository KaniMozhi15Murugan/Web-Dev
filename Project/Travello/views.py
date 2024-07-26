from django.shortcuts import render
from django.http import HttpResponse
from .models import destination


# # Create your views here.
# def index(request):
#     return render(request,'index.html',{'price':700})
def index(request):
    dest1=destination()
    dest1.name='Mumbai',
    dest1.desc='The city that never sleeps'
    dest1.img='destination_1.jpg'
    dest1.price=700

    dest2=destination()
    dest2.name='Kerala',
    dest2.desc='The city that never bored'
    dest2.price=1700

    dest3=destination()
    dest3.name='Goa',
    dest3.desc='XXXXXXXXXXXX '
    dest3.price=1000

    dests=[dest1,dest2,dest3]
    return render (request,"index.html",{'dests':dests})






