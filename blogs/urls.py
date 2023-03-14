from urllib.parse import urlparse
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path ,include
from blogs import views
from .views import AddCategoryView, ArticleDeleteView, HomeView,ArticleDetailView,ArticleCreateView,ArticleUpdateView,ArticleDeleteView,Categoryview,LikeView
urlpatterns = [
    path('',HomeView.as_view(),name='Home'),
    path('Article/<int:pk>', ArticleDetailView.as_view(), name='indexDetail'),
    path('add_post/',ArticleCreateView.as_view(),name='add_post'),
    path('Article/edit/<int:pk>',ArticleUpdateView.as_view(),name='update_post'),
    path('Article/<int:pk>/remove/',ArticleDeleteView.as_view(),name='delete_post'),
    path('add_category/',AddCategoryView.as_view(),name='add_category'),
    path('category/<str:cats>/',Categoryview,name='category'),
    path('like/<int:pk>',LikeView,name='like_post'),
    path('category/<str:cats>/', Categoryview, name='category'),
    path('categories/', views.category_list, name='filter'),


]
