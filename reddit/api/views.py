from django.shortcuts import render
from .models import Task
import json
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import reverse
# Create your views here.
from .serializers import TaskSerializer

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
	    'List' : '/task-list/',
	    'Detail View' : '/task-detail/<str:pk>/',
	    'Create' : '/task-create/',
	    'Update' : '/task-update/<str:pk>/',
	    'Delete' : '/task-delete/<str:pk>/',
	}
	return JsonResponse (api_urls)

@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all()
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)