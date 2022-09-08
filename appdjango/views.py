from ast import Not
from email.mime import message
from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'template/index.html')





def signup(request)  :
     if request.method==('POST') :
         username=request.POST['username']
         email = request.POST['email']
         password = request.POST['password']
         confirmpass = request.POST['recheck-pass']
         user = User.objects.create_user(username,email,password)
         user.first_name='singh'
         user.save()          
         return redirect('/')



def   userlogin(request):
    username= ''
    password=''                            
    if request.method==('POST'):
       username=request.POST['username']
       password = request.POST['password']
      
         
    user=authenticate(username= username, password= password) 
    if user is not None:
      auth_login(request,user)
      messages.success(request, "Your message has been successfully sent")
      return redirect('/')

    else:
        return HttpResponse('<h1>Invalid Credentials</h1>')
        
def handelLogout(request):
    logout(request)

    return redirect('/')            