from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# to register user
def register(request):
     return render(request, 'registration/register.html')

#user login              
def user_login(request):
    return render(request, 'registration/login.html')

#checks if the user exists or not
def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(        
            reverse('user:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('user:show_user')
)  
#Reading user data 
def show_user(request):
    print(request.user.username)
    return render(request, 'registration/user.html', {
        "username": request.user.username,
        "password": request.user.password
})
