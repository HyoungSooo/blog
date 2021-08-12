from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

# Create your views here.


def index(request):
    object_list = Post.objects.all()
    return render(request, 'web/index.html', {'object_list': object_list})


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
    return render(request, 'web/post_detail.html', {'object': object})
