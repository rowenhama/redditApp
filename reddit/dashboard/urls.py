from django.urls import path
from .import views

urlpatterns = [
    path('', views.dash, name='dash'),
    path('about/',views.about,name='about'), 
    path('posts/',views.posts,name='posts'),
    path('trending/',views.trending,name='trending'),
    
    ]
