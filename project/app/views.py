from django.shortcuts import render,redirect
from django.http import HttpResponse
todo=[{'id':'1','task':'task1'},{'id':'2','task':'task2'},{'id':'3','task':'task3'}]
# Create your views here.
def fun1(requset):
    return HttpResponse("welcome")
    # return render(requset,'todo.html')
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

def todo1(requst):
    if requst.method=='POST':
        id=requst.POST['id']
        task=requst.POST['task']
        todo.append({'id':id,'task':task})
        print(todo)
        return redirect(todo1)
    return render(requst,'todo.html',{'todo':todo})

def edit_form(request,id):
    task=''
    for i in todo:
        if i['id']==id:
            task=i
    if request.method=='POST':
        id=request.POST['id']
        task1=request.POST['task']
        task['id']=id
        task['task']=task1
        return redirect(todo1)
    return render(request,'edit.html',{'task':task})

def delete_fun(request,id):
    for i in todo:
        if i['id']==id:
            todo.remove(i)
    return redirect(todo1)