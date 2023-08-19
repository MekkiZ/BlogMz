from django.shortcuts import render, redirect
from .models import UserCus
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login
from .form import SignupForm, UserCreationForm,LoginForm


def signup(request):


    return render(request,'authenticate/signup.html')


def login_user(request):


    return render(request, 'authenticate/login.html')