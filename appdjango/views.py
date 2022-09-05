from email.mime import message
from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request,'template/index.html')





def submit(request)  :
     if request.method==('POST') :
         username=request.POST['username']
         email = request.POST['email']
         password = request.POST['password']
         confirmpass = request.POST['recheck-pass']
         

         user = User.objects.create_user(username,email,password)
         user.first_name='singh'
         user.save()          
         return redirect('home')