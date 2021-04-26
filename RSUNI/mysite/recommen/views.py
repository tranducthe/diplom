from django.shortcuts import render
from django.http import HttpResponse
from .models import recom
# Create your views here.

def recom1_view(request):

    object_list1 = recom.objects.all()
    return  render(request,"recommen/recom1.html", {
        'object_list1': object_list1
    })


