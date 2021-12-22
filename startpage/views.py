from web.models import Post, Project
from django.shortcuts import render
import os
import sys
# 프로젝트 root를 import 참조 경로에 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Create your views here.


def introduce(request):
    object = Post.objects.order_by('-dt_created')
    object_sub = object[:3]
    pro = Project.objects.all()
    return render(request, 'startpage/index.html', {'obj': object_sub, 'pro_obj': pro})


def about(request):
    return render(request, 'startpage/about.html')
