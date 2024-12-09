from django.shortcuts import render,redirect
from .models import *
from .serializers import *
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics,mixins
# Create your views here.

def fun1(req):
    if req.method=='GET':
        d=Student.objects.all()
        s=Sample(d,many=True)
        return JsonResponse(s.data,safe=False)
    

@csrf_exempt    
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
        

@csrf_exempt
def fun3(req,d):
    try:
        demo=Student.objects.get(pk=d)
    except Student.DoesNotExist:
        return HttpResponse('invalid')
    if req.method=='GET':
        s=model_serializers(demo)
        return JsonResponse(s.data)
    elif req.method=='PUT':
        d=JSONParser().parse(req)
        s=model_serializers(demo,data=d)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data)
        else:
            return JsonResponse(s.errors)
    elif req.method=="DELETE":
        demo.delete()
        return HttpResponse('deleted')
    
@api_view(['GET','POST'])
def fun4(req):
    if req.method=='GET':
        d=Student.objects.all()
        s=model_serializers(d,many=True)
        return Response(s.data)
    
    elif req.method=='POST':
        s=model_serializers(data=req.data)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data,status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(s.errors,status=status.HTTP_400_BAD_REQUEST)
        
