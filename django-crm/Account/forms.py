from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

        labels = {
            "username": "Username",
            "email": "Email",
            "password1": "Password",
            "password2": "Confirm Password"
        }

        widgets ={
            "username": forms.TextInput(attrs={
                "class":"username form-control m-2 p-2",
                "placeholder":"enter username"
                }),
            "email": forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"enter email"
                }),
        }
