from urllib.parse import urlparse
from django.contrib import admin
from django.urls import path ,include
from blogs import views
from .views import UserRegisterView

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register')
]
