from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun1(requset):
    return HttpResponse("welcome")
def index_page(request):
    name='hari'
    age='22'
    place='thrissur'
    return render(request,'index.html',{'name':name,'age':age,'place':place})

def demo(request):
    # l=[1,2,3,4,5,6]
    l=[{'name':'achu','age':22},{'name':'athi','age':18},{'name':'ayu','age':24},{'name':'hari','age':22}]
    d={'name':'achu','age':22}
    return render(request,'demo.html',{"data":l,'data1':d})
def second(request):
    return render(request,'second_page.html')