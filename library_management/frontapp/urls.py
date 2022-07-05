
from django.urls import path,include
from rest_framework import routers
from . import views


urlpatterns = [
    path("",views.homeView,name="home"),
    path("login-signup",views.loginSignUp,name="login-signup"),
]
