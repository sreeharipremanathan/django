from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def display_std(req):
    data=Student.objects.all()
    return render(req,'display_std.html',{"data":data})

def add(req):
    if req.method=='POST':
        roll=req.POST["roll"]
        std_name=req.POST["name"]
        std_age=req.POST["age"]
        std_email=req.POST["email"]
        std_phno=req.POST["phno"]
        data=Student.objects.create(roll_no=roll,name=std_name,age=std_age,email=std_email,phn=std_phno)
        data.save()
        return redirect(display_std)
    else:
        return redirect(display_std)
    
def edit(req,id):
    data=Student.objects.get(pk=id)
    if req.method=='POST':
        roll=req.POST["roll"]
        std_name=req.POST["name"]
        std_age=req.POST["age"]
        std_email=req.POST["email"]
        std_phno=req.POST["phno"]
        Student.objects.filter(pk=id).update(roll_no=roll,nammse=std_name,age=std_age,email=std_email,phn=std_phno)
        return redirect(display_std)
    else:
        return render(req,'edit.html',{'data':data})