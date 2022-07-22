from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, logout, login, user_login_failed

# Create your views here.

def home(request, *args, **kwargs):
    return render(request, 'accounts/home.html', {})


def login_view(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username= username, password= password)

        login(request, user)
        return redirect('/')

    return render(request, 'accounts/login.html', {'form' : form})

def logout_view(request):
    logout(request)
    return redirect('/')

def register(request):
    formm = UserRegisterForm()
    if request.method == 'POST':
        formm = UserRegisterForm(request.POST)
        if formm.is_valid():
            formm.save()
            return redirect('/')
    return render(request, 'accounts/register.html', {'formm': formm})