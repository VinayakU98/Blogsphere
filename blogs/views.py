import email
from multiprocessing import context
from re import template
import re
from tokenize import Number
from unicodedata import category, name
from urllib import request
from blogs.models import Post,Category
from django.shortcuts import render ,HttpResponse,get_object_or_404,HttpResponseRedirect
from django.views.generic import DetailView,ListView,CreateView,UpdateView,DeleteView
from .forms import PostForm
from django.urls import reverse_lazy,reverse
from django.core.exceptions import PermissionDenied

#def index(request):
#   return render(request,'index.html')
class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']

    def dispatch(self, request, *args, **kwargs):
        # get the post object being updated
        post = self.get_object()
        # check if the current user is the author of the post
        if post.author != self.request.user:
            # raise PermissionDenied exception if not authorized
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
def AddComment(request):
       if request.method=="POST":
              comment=request.POST.get('comment')

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
              liked=False
              if stuff.likes.filter(id=self.request.user.id).exists():
                     liked=True
              total_likes=stuff.total_likes()
              context["total_likes"]=total_likes
              context["liked"]=liked
              return context
class ArticleCreateView(CreateView):
       model=Post
       form_class=PostForm
       template_name='add_post.html'
       def form_valid(self, form):
              form.instance.author = self.request.user
              return super().form_valid(form)      
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
       liked=False
       if post.likes.filter(id=request.user.id).exists():
              post.likes.remove(request.user)
              liked=False
       else:
              post.likes.add(request.user)
              liked=True
       return HttpResponseRedirect(reverse('indexDetail',args=[str(pk)]))