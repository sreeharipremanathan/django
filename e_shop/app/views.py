from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
# Create your views here.

def shop_login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
    else:
        if req.method=='POST':
            uname=req.POST['uname']
            password=req.POST['password']
            data=authenticate(username=uname,password=password)
            if data:
                login(req,data)
                req.session['shop']=uname     #create
                return redirect(shop_home)
            
        return render(req,'login.html')
    

def shop_logout(req):
    logout(req)
    req.session.flush()     #delete
    return redirect(shop_login)


def shop_home(req):
    if 'shop' in req.session:
        product=products.objects.all()
        print(product)
        return render(req,'shop/shop_home.html',{'product':product})
    else:
        return render(shop_login)