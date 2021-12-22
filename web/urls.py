"""toyproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path('', include('startpage.urls')),
    path('index/', views.index, name='index'),
    path('project-index/<int:pro_id>',
         views.project_index, name='project_index'),
    path('create/', views.PageCreate.as_view(), name='post-create'),
    path('post-detail/<int:post_id>',
         views.post_detail, name='post-detail'),
    path('project-detail/<int:pro_id>/<int:post_id>',
         views.project_detail, name='project-detail'),
    path('python/', views.python_list, name='python_list'),
    path('javascript/', views.javascript_list, name='javascript_list'),
    path('html/', views.html_list, name='html_list'),
    path('css/', views.css_list, name='css_list'),
    path('django/', views.django_list, name='django_list'),
    path('react/', views.react_list, name='react_list'),
    path('DB/', views.DB_list, name='DB_list'),
    path('algorithm/', views.algorithm_list, name='algorithm_list'),
    path('nodejs/', views.node_list, name='node_list'),
]
