from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from pymongo import MongoClient
client=MongoClient("mongodb://127.0.0.1:27017/")
db=client['DOCTOR']
coll=db.details

def sample(request):
    return render(request,"my_app/login.html")

def sample1(request):
    return render(request,"my_app/signin.html")

def sample2(request):
    return render(request,"my_app/register.html")




def getres(request):
    if request.method=='POST':
        name=request.POST.get('name')
        phno=request.POST.get('phno')
        email=request.POST.get('email')
        date=request.POST.get('date')

        db.coll.insert_one({'name': name, 'email': email, 'phone': phno,'date':date})
        return HttpResponse("SAVED")
    return HttpResponse("NOT SAVED")

def signuppost(request):
    if request.method=='POST':
        email=request.POST.get('email')
        passwo=request.POST.get('psw')

        db.coll.insert_one({'email': email, 'passwo':passwo})
        return HttpResponse("REGISTERED")
    return HttpResponse("NOT SAVED")

def recovery(request):
    return render(request,"my_app/recovery.html")

def recoverypass(request):
    return render(request,"my_app/recoverypass.html")


def forgot1(request):
    if request.method=="POST":
        email=request.POST.get("email")
        subject = 'Resert your pass'
        message = 'HELLO, PLEASE RESET YOUR PASSWORD BY USING THE BELOW LINK' \
                  'http://127.0.0.1:8000/recoverypass/'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)
        return render(request,"my_app/signin.html")
    else:
        return HttpResponse("NOT SENT ")

def checknewpass(request):
    if request.method=="POST":
        email=request.POST.get("email")
        passwo=request.POST.get("passwo")
        c=db.coll.find_one({'email':email})
        if c["email"]==email:
            db.coll.update_one({"email":email},{"$set":{"passwo":passwo}})
            return render(request,"my_app/signin.html")


