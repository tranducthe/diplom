from django.shortcuts import render
from django.http import HttpResponse
from .models import ListUni
# Create your views here.

def home_view(request):

    object_list = ListUni.objects.all()
    return  render(request,"home/home.html", {
        'object_list': object_list
    })

def about_view(request):
    return render(request, 'home/about.html')

