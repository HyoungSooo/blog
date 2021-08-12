from web.models import Post
from django.shortcuts import render
import os
import sys
# 프로젝트 root를 import 참조 경로에 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Create your views here.


def introduce(request):
    object = Post.objects.all()
    p = len(object)
    object_sub = object[p-3:p]
    return render(request, 'startpage/index.html', {'obj': object_sub})
