from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.create_post,name='posts'), 
    path('forms/',views.get_name,name='name'),
    #path('<slug>/', views.detail_post_view, name="detail"),
    path('<slug>/edit/', views.edit_post_view, name='edit'),
   
    #path('', views.apiOverview, name ="api-overview"),
    path('post-list/', views.postList, name ='post-list'),
    path('post-detail/<str:pk>/', views.postDetail, name ='post-detail'),
    path('post-create/', views.postCreate, name ='post-create'),
    path('post-update/<str:pk>/', views.postUpdate, name ='post-update'),
    path('post-delete/<str:pk>/', views.postDelete, name ='post-delete'),
]