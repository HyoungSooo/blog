from django.core import paginator
from django.db.models.base import Model
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from .forms import PostForm
from .models import Post, Project, Project_content
from .forms import PostForm
from django.urls import reverse
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    post_list = Post.objects.all().order_by('-dt_created')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(post_list, 10)
    object_list = paginator.get_page(page)
    context = {
        'object': object_list
    }
    return render(request, 'web/index.html', context)


def project_index(request, pro_id):
    project_contents = Project_content.objects.filter(
        project_id=pro_id)
    page = int(request.GET.get('p', 1))
    paginator = Paginator(project_contents, 10)
    object_list = paginator.get_page(page)
    context = {
        'object': object_list
    }

    return render(request, 'web/project_content_index.html', context)


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


def project_detail(request, pro_id, post_id):
    project_object = Project_content.objects.filter(
        project_id=pro_id).get(id=post_id)
    context = {
        'object': project_object,
    }
    return render(request, 'web/project_post_detail.html', context)


def javascript_list(request):
    object = Post.objects.filter(type='javascript').order_by('-dt_created')
    context = {
        'object': object
    }
    return render(request, 'web/index.html', context)


def html_list(request):
    object = Post.objects.filter(type='html').order_by('-dt_created')
    context = {
        'object': object
    }
    return render(request, 'web/index.html', context)


def css_list(request):
    object = Post.objects.filter(type='css').order_by('-dt_created')
    context = {
        'object': object
    }
    return render(request, 'web/index.html', context)


def django_list(request):
    object = Post.objects.filter(type='django').order_by('-dt_created')
    context = {
        'object': object
    }
    return render(request, 'web/index.html', context)


def react_list(request):
    object = Post.objects.filter(type='react').order_by('-dt_created')
    context = {
        'object': object
    }
    return render(request, 'web/index.html', context)


def python_list(request):
    object = Post.objects.filter(type='python').order_by('-dt_created')
    context = {
        'object': object
    }
    return render(request, 'web/index.html', context)


def DB_list(request):
    object = Post.objects.filter(type='DB').order_by('-dt_created')
    context = {
        'object': object
    }
    return render(request, 'web/index.html', context)


def algorithm_list(request):
    object = Post.objects.filter(type='algorithm').order_by('-dt_created')
    context = {
        'object': object
    }
    return render(request, 'web/index.html', context)


def node_list(request):
    object = Post.objects.filter(type='node').order_by('-dt_created')
    context = {
        'object': object
    }
    return render(request, 'web/index.html', context)
