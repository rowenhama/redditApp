from django.urls import path
from .import views

urlpatterns = [
    path('', views.apiOverview, name ="api-overview"),
    path('task-list/', views.taskList, name ="task-list"),
    path('task-detail/<str:pk>/', views.taskDetail, name ="task-detail"),
    path('task-create/', views.taskCreate, name ="task-create"),
    path('task-update/<str:pk>/', views.taskUpdate, name ="task-update"),
    path('task-delete/<str:pk>/', views.taskDelete, name ="task-delete"),

]
#path('', views.apiOverview, name ="api-overview"),
    #path('list/', views.postList, name ="posts-list"),
    #path('detail/<str:pk>/', views.postDetail, name ="posts-detail"),
   # path('create/', views.postCreate, name ="posts-create"),
    #path('update/<str:pk>/', views.postUpdate, name ="posts-update"),
    #path('delete/<str:pk>/', views.postDelete, name ="posts-delete"),