from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def loginUser(request):
    page = 'login'

    context = {'page': page}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist.")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
             messages.error(request, "Username OR password does not exist!! .")

    return render(request, 'base/login_register.html', context)    

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request): 
    form = UserCreationForm()
    return render(request, 'base/login_register.html', {'form':form})

def home(request):
    return render(request,'base/home.html' )




