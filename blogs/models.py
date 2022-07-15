import email
from logging import PlaceHolder
from django.contrib.auth.models import User
from unicodedata import category, name
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField
from django.urls import reverse
from datetime import datetime ,date

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200,default="uncategorized")
    def __str__(self):
            return self.name
    def get_absolute_url(self):
        return reverse('indexDetail',args=[self.id])
class Post(models.Model):
    title=models.CharField(max_length=2000)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField(default="Hi")
    date_posted=models.DateField(auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    likes=models.ManyToManyField(User,related_name='blog_posts')
    comments=models.TextField(default="comment here")
    def total_likes(self):
        return self.likes.count()
    def __str__(self):
        return self.title + str(self.author)
    def get_absolute_url(self):
        return reverse('indexDetail',args=[self.id])
