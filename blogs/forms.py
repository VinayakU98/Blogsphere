from dataclasses import fields
from logging import PlaceHolder
from operator import mod
from tkinter.ttk import Widget
from turtle import title
from xml.etree.ElementTree import Comment
from django import forms
from .models import Post 
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','body','category']
        
        widgets={
            'title':forms.TextInput(attrs={ 'class':'form-control'}),
            'body':forms.Textarea(attrs={ 'class':'form-control'}),
            'category':forms.Select(attrs={ 'class':'form-control'}),
        }