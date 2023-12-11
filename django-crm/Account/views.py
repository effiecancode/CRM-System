from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# def login_user(request):
#     return render(request, 'Account/login.html', {})

# def logout_user(request):
#     pass

def create_account(request):
    return render(request, 'account/create_account.html', {})
