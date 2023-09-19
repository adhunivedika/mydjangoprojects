from django.http import HttpResponse
from django.shortcuts import render
from. models import Place
from. models import Person
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    ren=Person.objects.all()
    return render(request,"index1.html",{"result":obj,"result1":ren})