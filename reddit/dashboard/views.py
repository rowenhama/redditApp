from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


def dash(request):
	
	#return HttpResponse('<h1>hajajja</h1>')
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def posts(request):
	return render(request,'posts.html')

def trending(request):
	return render(request,'trending.html')

