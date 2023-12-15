from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# def login_user(request):
#     return render(request, 'Account/login.html', {})


from .forms import CustomUserCreationForm

def create_account(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
               user = form.save()
               login(request, user)
               messages.success(request, "Account created successfully!")
               return redirect('home')
        else:
               messages.error(request, "Form is not valid")
            #    return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/create_account.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged")
    return redirect('home')
