from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import PostForm
from .models import Post
from .forms import PostForm
from django.urls import reverse
# Create your views here.


def index(request):
    object_list = Post.objects.all().order_by('-dt_created')
    context = {
        'object': object_list
    }
    return render(request, 'web/index.html', context)


class PageCreate(CreateView):
    model = Post
    template_name = 'web/post_create.html'
    form_class = PostForm

    def get_success_url(self) -> str:
        return reverse('index')


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
    return render(request, 'web/index.html', context)


def html_list(request):
    object = Post.objects.filter(type='html')
    context = {
        'object': object
    }
    return render(request, 'web/index.html', context)


def css_list(request):
    object = Post.objects.filter(type='css')
    context = {
        'object': object
    }
    return render(request, 'web/index.html', context)


def django_list(request):
    object = Post.objects.filter(type='django')
    context = {
        'object': object
    }
    return render(request, 'web/index.html', context)


def react_list(request):
    object = Post.objects.filter(type='react')
    context = {
        'object': object
    }
    return render(request, 'web/index.html', context)


def python_list(request):
    object = Post.objects.filter(type='python')
    context = {
        'object': object
    }
    return render(request, 'web/index.html', context)


def DB_list(request):
    object = Post.objects.filter(type='DB')
    context = {
        'object': object
    }
    return render(request, 'web/index.html', context)


def algorithm_list(request):
    object = Post.objects.filter(type='algorithm')
    context = {
        'object': object
    }
    return render(request, 'web/index.html', context)
