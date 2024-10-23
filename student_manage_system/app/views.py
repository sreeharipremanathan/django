from django.shortcuts import render
from .models import *
# Create your views here.
def display_std(req):
    data=Student.objects.all()
    return render(req,'display_std.html',{"data":data})