from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout,login
from .forms import DT_form, UserRegisterFormAdmin, Connect_form
from .models import DT_model,User
from django import forms
from django.conf import settings
from django.core.mail import send_mail


def home_page(request):
    context = {}
    return render(request, 'base/home.html', context)

# Create your views here.


def register_page(request):
    form = UserRegisterFormAdmin()
    if request.method == 'POST':
        form = UserRegisterFormAdmin(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login_page')
        
    context = {"form":form}
    return render(request, 'base/register_page.html', context)


def login_page(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            print(user)
            login(request,user)
            return redirect('home_page')
    context = {"form":form}
    return render(request,'base/login_page.html',context)


def logout_page(request):
    logout(request)
    return redirect("login_page")

def designers_page(request):
    designers = User.objects.filter(is_superuser = True )
    context = {'designers':designers}
    
    return render(request, 'base/designers_page.html',context)


def designer_page(request, pk):
    designer = User.objects.get(id = pk)
    context = {'designer':designer}
    return render(request, 'base/designer_page.html',context)


def hire_page(request, pk):
    form = DT_form()
    form.fields['status'].widget = forms.HiddenInput()
    designer = User.objects.get(id = pk)
    
    if request.method == "POST":
        time_model = DT_model(desiger = designer, date = request.POST['date'], time = request.POST['time'], email = request.POST['email'] )
        time_model.save()
        return redirect("home_page")

    context = {'form':form, 'designer':designer}
    return render(request, 'base/hire_page.html',context)



def session_page(request):
    
    user = User.objects.filter(username =request.user )
    dts = DT_model.objects.filter(desiger__username = request.user)
    context = {"dts":dts}
    return render(request, 'base/session_page.html',context)

def status_page(request,pk):
    subject = 'welcome to Fashion App'
    email_from = settings.EMAIL_HOST_USER

    

    dt = DT_model.objects.get(id = pk)
    form = DT_form(instance=dt)
    form.fields['email'].widget = forms.HiddenInput()
    if request.method == "POST":
        form = DT_form(data=request.POST,instance=dt)

        if form.is_valid():
            if dt.status == True:
                print(dt.email, "Accepted")
                message = 'Hi , thank you for registering in Fashio APP, Your session is Accepted'
                recipient_list = [dt.email]
                send_mail( subject, message, email_from, recipient_list, fail_silently=False)
            elif dt.status == False:
                print(dt.email, "Refused")
                message = 'Hi , thank you for registering in Fashio APP, Your session is Refused'
                recipient_list = [dt.email]
                send_mail( subject, message, email_from, recipient_list, fail_silently=False)
            form.save()
            return redirect("session_page")
        
    context = {'form':form}
    return render(request, 'base/status_page.html',context)

def connect_page(request):
    
    form = Connect_form()
    if request.method == "POST":
        form = Connect_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_page")
    context = {'form':form}
    return render(request, "base/connect_page.html",context)