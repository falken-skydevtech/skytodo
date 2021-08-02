from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as __login__, logout as __logout__
from ..forms.users import *
from django.contrib import messages


def logout(request):
    __logout__(request)
    return redirect('/')

def login(request):
    data = {}
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                __login__(request, user)
                return redirect("/task/dashboard")
            else:
                messages.error(request, "L'email ou le mot de passe est erroné")
    else:
        form = UserLoginForm()
    data['form'] = form
    return render(request, 'account/login.html', data)

def register(request):
    data = {}
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.initialize_create_account()
            return redirect("/account/login")
    else:
        form = UserCreationForm()
    data['form'] = form
    return render(request, 'account/register.html', data)


def start(request):
    data = {}
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                __login__(request, user)
                return redirect("/account/company/index")
    else:
        form = UserLoginForm()
    data['form'] = form
    return render(request, 'account/login.html', data)


def resend_email_verification(request):
    if request.method == "POST":
        return redirect("/account/company/index")
    return render(request, 'account/email/verification.html')

def check_email_verification(request):
    if request.method == "POST":
        return redirect("/account/company/index")
    return render(request, 'account/email/check.html')

def update_account(request):
    if request.method == "POST":
        return redirect("/account/company/index")
    return render(request, 'account/update.html')

def lost_password(request):
    if request.method == "POST":
        return redirect("/account/company/indexprofile/select")
    return render(request, 'account/register.html')

def renew_password(request):
    if request.method == "POST":
        return redirect("/account/company/indexprofile/select")
    return render(request, 'account/register.html')
