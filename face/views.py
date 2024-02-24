from django.shortcuts import render
from face import faceDetect,imotionDetect,VideoImotionDetection
from django.http import HttpResponse
from face.models import UserSign
from django.db.models import Q
# Create your views here.
def home(request):
    return render(request,'home.html')
def detection(request):
    return render(request,'faceD.html')

def About(request):
    return render(request,'about.html')

def faceDet(request):
    return render(request,'faceD.html',{'result': faceDetect.faceDetect()})
def imotionDetection(request):
    return render(request, 'faceD.html', {'result': imotionDetect.imotionDetect()})
def VideoImotionDetect(request):
    return render(request, 'faceD.html', {'result': VideoImotionDetection.VideoImotionDetection()})

def Register(request):
    return render(request,"register.html")
def input(request):
    return render(request,'sign_up.html')
def SignUp(request):
    nm=request.POST.get('name')
    em=request.POST.get('email')
    mb=request.POST.get('mobile')
    psw=request.POST.get('password')
    psw1=request.POST.get('password1')
    match=UserSign.objects.filter(Email=em,Password=psw)
    if(len(match)!=0):
        return HttpResponse("Sorry You are Old User")
    else:
        res=UserSign(Name=nm,Email=em,Mobile=mb,Password=psw)
        res.save()
        return render(request,'register.html')
def addPicture(request):
    eml=request.POST.get('email')
    pswd=request.POST.get('password')
    data1=UserSign.objects.filter(Email=eml,Password=pswd) 
    if(len(data1)==0):
        return HttpResponse("Your Email or Password is Wrong") 
    else:
        return render(request,'ImageAdd.html') 
