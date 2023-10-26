from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginPage(request):
    context={'page':'Login Form'}
    if request.method == "POST":
      username=request.POST.get('username')
      password=request.POST.get('password')

      if not User.objects.filter(username=username).exists():
        messages.error(request,'Invalid Username')
        return redirect('/log/')
      
      user=authenticate(username=username,password=password)

      if user is None:
        messages.error(request,'Invalid Password')
        return redirect('/log/')
      else:
        login(request,user)
        request.session['user_authenticated'] = True
        return redirect('/')
    return render(request,"login.html",context)
def regPage(request):
    if request.method =="POST":
       first_name=request.POST.get('first_name')
       last_name=request.POST.get('last_name')
       username=request.POST.get('username')
       password=request.POST.get('password')
       email=request.POST.get('email')
       
       user=User.objects.filter(username=username)
       if user.exists():
           messages.info(request,'User already taken')
           return redirect('/reg/')
       user = User.objects.create(
           first_name=first_name,
           last_name=last_name,
           username=username,
           email=email
       )
       user.set_password(password)
       user.save()
       request.session['user_authenticated'] = True
       messages.info(request,'Account sucessfully created')
       return redirect('/log/')
    context={'title':'Registration Form'}
    return render(request,'reg.html',context)
@login_required(login_url='/log/')
def logoutPage(request):
    logout(request)
    request.session.flush()
    request.session.clear_expired()
    messages.info(request,'Logout...')
    return redirect('/log/')
@login_required(login_url='/log/')
def userProfile(request):
    context={'title':'Profile'}
    return render(request,'index.html',context)