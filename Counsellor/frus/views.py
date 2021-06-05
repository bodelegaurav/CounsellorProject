from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from frus.models import Contact, Appointment
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
# Create your views here.


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })

@login_required(login_url="/login")
def index(request):
    return render(request, 'index.html')

@login_required(login_url="/login")
def ibs(request):
    return render(request, 'ibs.html')

def home(request):
    return render(request, 'home.html')

@login_required(login_url="/login")
def book(request):     
    return render(request, 'appo.html')

@login_required(login_url="/login")
def Happo(request):  
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        counsellor=request.POST['counsellor']
        content=request.POST['content']
        send_mail('Request to fix an appointment at '+counsellor , 'I, '+name+' want to have one-on-one session with you. My issue is:\n\n'+content, settings.EMAIL_HOST_USER, [email], fail_silently=False)
        co=Appointment(name=name, email=email, counsellor=counsellor, content=content)
        co.save()
        messages.success(request, "Sent")
        return HttpResponseRedirect(reverse('home'))
    else:
        return HttpResponse('404-not found')

        

    
    
    

@login_required(login_url="/login")
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        send_mail(name+' with email address '+email+' wants to communicate something to you', content, settings.EMAIL_HOST_USER, [phone], fail_silently=False)
        contact=Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
        messages.success(request, "Sent")
    return render(request, 'contact.html')

@login_required(login_url="/login")
def coun(request):
    return render(request, 'oc.html')

@login_required(login_url="/login")
def rk(request):
    return render(request, 'rakesh.html')

@login_required(login_url="/login")
def f1(request):
    return render(request, 'f1.html')

@login_required(login_url="/login")
def f2(request):
    return render(request, 'f2.html')


def handleSignup(request):
    if request.method == 'POST':
        username=request.POST["username"]
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        pass1=request.POST["pass1"]
        pass2=request.POST["pass2"]

        if len(username)>10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric")
            return redirect('home')
        if pass1!=pass2:
            messages.error(request, "Passwords do not match")
            return redirect('home')

        myuser=User.objects.create_user(username, email, pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request, "Created User successfully")
        return redirect('home')
        

    else:
        return HttpResponse('404 Not Found')


def handleLogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpass']
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "successfully logged in")
            return redirect('home')
        else:
            messages.error(request, "Invalid info")
            return redirect('home')
    else:
        messages.error(request, "Login First")
        return redirect('home')
        

def handleLogout(request):

        logout(request)
        messages.success(request, "successfully logged out")
        return redirect('home')


def index(request):
    return render(request, 'index.html')