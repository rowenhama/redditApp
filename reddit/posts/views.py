from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import CreatePost
from .models import Post
from .models import Task
import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import reverse

# Create your views here.

from .serializers import TaskSerializer

def create_post(request):

    context = {}

    form = CreatePost(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()

        form = CreatePost()
    context['form'] = form

    return render(request,'posts.html',context)

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

def detail_post_view(request, slug):

    context = {}

    post = get_object_or_404(Post, slug=slug)

    context['post'] = post

    return render(request, 'detail_post.html', context)

def edit_post_view(request, slug):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect("must_authenticate")

    post = get_object_or_404(Post, slug=slug)

    if post.author != user:
        return HttpResponse('You are not the author of that post.')

    if request.POST:
        form = UpdatePostForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated"
            post = obj

    form = UpdatePostForm(
            initial = {
                    "title": post.title,
                    "body":  post.body,
                    "image": post.image,
            }
        )

    context['form'] = form
    return render(request, '/edit_post.html', context)

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
def postList(request):
    tasks = Post.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def postDetail(request, pk):
    tasks = Post.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return JsonResponse(serializer.data)

@api_view(['POST'])
def postCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return JsonResponse(serializer.data)

@api_view(['POST'])
def postUpdate(request, pk):
    tasks = Post.objects.get(id=pk)
    serializer = TaskSerializer(instance=tasks, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return JsonResponse(serializer.data)

@api_view(['DELETE'])
def postDelete(request, pk):
    tasks = Task.objects.get(id=pk)
    tasks.delete()

    return JsonResponse('Item succsesfully delete!')