from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.create_post,name='posts'), 
    path('forms/',views.get_name,name='name'),
    path('<slug>/', views.detail_post_view, name="detail"),
    path('<slug>/edit/', views.edit_post_view, name="edit"),
   
]