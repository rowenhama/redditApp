from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import CreatePost
from .models import Post
# Create your views here.

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