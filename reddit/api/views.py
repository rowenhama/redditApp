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

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	return JsonResponse(serializer.data)

@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return JsonResponse(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=tasks, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return JsonResponse(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
	tasks = Task.objects.get(id=pk)
	tasks.delete()

	return JsonResponse('Item succsesfully delete!')