from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
import json

# Create your views here.


def index(request):
    object_list = Post.objects.all()
    context = {
        'object_list': object_list
    }
    return render(request, 'web/index.html', context)


def page_create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_diary = post_form.save()
            return redirect('index')
    else:
        post_form = PostForm()
    return render(request, 'web/post_form.html', {'form': post_form})


def post_detail(request, post_id):
    object = Post.objects.get(id=post_id)
    context = {
        'object': object,
    }
    return render(request, 'web/post_detail.html', context)


def javascript_list(request):
    object = Post.objects.filter(type='javascript')
    context = {
        'object': object
    }
    return render(request, 'web/javascript_list.html', context)


def html_list(request):
    object = Post.objects.filter(type='html')
    context = {
        'object': object
    }
    return render(request, 'web/html_list.html', context)


def css_list(request):
    object = Post.objects.filter(type='css')
    context = {
        'object': object
    }
    return render(request, 'web/css_list.html', context)


def django_list(request):
    object = Post.objects.filter(type='django')
    context = {
        'object': object
    }
    return render(request, 'web/django_list.html', context)


def react_list(request):
    object = Post.objects.filter(type='react')
    context = {
        'object': object
    }
    return render(request, 'web/react_list.html', context)


def python_list(request):
    object = Post.objects.filter(type='python')
    context = {
        'object': object
    }
    return render(request, 'web/python_list.html', context)
