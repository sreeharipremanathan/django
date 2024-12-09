from django.shortcuts import render,redirect
from .models import *
from .serializers import *
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
# Create your views here.

def fun1(req):
    if req.method=='GET':
        d=Student.objects.all()
        s=Sample(d,many=True)
        return JsonResponse(s.data,safe=False)
    
def fun2(req):
    if req.method=='GET':
        d=Student.objects.all()
        s=model_serializers(d,many=True)
        return JsonResponse(s.data,safe=False)
    elif req.method=='POST':
        d=JSONParser().parse(req)
        s=model_serializers(data=d)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data)
        else:
            return JsonResponse(s.errors)