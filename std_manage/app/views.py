from django.shortcuts import render,redirect
student=[{'roll':1,'name':'achu','age':22,'email':'ach@gmail.com','phno':5353535},{'roll':2,'name':'ayu','age':25,'email':'ayu@gamil.com','phno':32747774}]
# Create your views here.
def display(req):
    if req.method=='POST':
        roll=req.POST['roll']
        name=req.POST['name']
        age=req.POST['age']
        email=req.POST['email']
        phno=req.POST['phno']
        student.append({'roll':roll,'name':name,'age':age,'email':email,'phno':phno})
        return redirect(display)
    return render(req,'index.html',{'data':student})

# def std_dtls(req):
#     if req.method=='POST':
#         roll=req.POST['roll']
#         name=req.POST['name']
#         age=req.POST['age']
#         email=req.POST['email']
#         phno=req.POST['phno']
#         student.append({'roll':roll,'name':name,'age':age,'email':email,'phno':phno})
#         return redirect(std_dtls)
#     return render(req,'index.html',{'data':student})

def edit(req,id):
    # print(id)
    data=''
    for i in student:
        # print(student)
        if i['roll']==id:
            # print(i)
            # print(type(i['roll']))
            data=i
            # print(data)
    if req.method=='POST':
        roll=req.POST['roll']
        name=req.POST['name']
        age=req.POST['age']
        email=req.POST['email']
        phno=req.POST['phno']
        data['roll']=roll
        data['name']=name
        data['age']=age
        data['email']=email
        data['phno']=phno
        print(data)
        return redirect(display)
    return render(req,'edit.html',{'data':data})
    # return render(req,'edit.html')

def delete(req,id):
    print(id)
    for i in student:
        print(i)
        if i['roll']==id:
            print(i)
            student.remove(i)
    return redirect(display)