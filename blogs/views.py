import email
from multiprocessing import context
from re import template
import re
from tokenize import Number
from unicodedata import category, name
from urllib import request
from blogs.models import Contactus,Post,Category
from django.shortcuts import render ,HttpResponse,get_object_or_404,HttpResponseRedirect
from django.views.generic import DetailView,ListView,CreateView,UpdateView,DeleteView
from .forms import PostForm
from django.urls import reverse_lazy,reverse
# Create your views here.
#def index(request):
#   return render(request,'index.html')
def contactus(request):
       if request.method=="POST":
              name=request.POST.get('name')
              email=request.POST.get('email')
              phone=request.POST.get('phone')
              contact = Contactus(name=name,email=email,phone=phone)
              contact.save()
          
              
       return render(request,'contactus.html')
class HomeView(ListView):
       model=Post
       template_name='index.html'
       ordering=['id']
class ArticleDetailView(DetailView):
       model=Post
       template_name='indexDetail.html'
       def get_context_data(self, **kwargs):
              context=super(ArticleDetailView,self).get_context_data()
              stuff=get_object_or_404(Post,id=self.kwargs['pk'])
              total_likes=stuff.total_likes()
              context["total_likes"]=total_likes
              return context
class ArticleCreateView(CreateView):
       model=Post
       form_class=PostForm
       template_name='add_post.html'
class ArticleUpdateView(UpdateView):
       model=Post
      # form_class=PostForm
       template_name='update_post.html'
       fields=['title','body']
class ArticleDeleteView(DeleteView):
       model=Post
       template_name='delete_post.html'
       success_url=reverse_lazy('Home')
class AddCategoryView(CreateView):
       model=Category
       template_name='add_category.html'
       success_url=reverse_lazy('Home')
       fields='__all__'
def Categoryview(request,cats):
       category_posts=Post.objects.all
       return render(request,'categories.html',{'cats':cats,'category_posts':category_posts})
def LikeView(request,pk):
       post=get_object_or_404(Post,id=request.POST.get('post_id'))
       post.likes.add(request.user)
       return HttpResponseRedirect(reverse('indexDetail',args=[str(pk)]))