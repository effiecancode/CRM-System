from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'Account'

urlpatterns = [
    path('signup/', views.create_account, name='signup'),
    path('login/', LoginView.as_view(template_name='Account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='Account:login'), name='logout'),
]
