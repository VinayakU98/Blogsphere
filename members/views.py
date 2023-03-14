from django.shortcuts import render
from django.views import generic
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class UserRegisterView(generic.CreateView):
    form_class=CustomUserCreationForm
    template_name='registration/register.html'
    success_url=reverse_lazy('login')
