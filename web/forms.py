from django import forms
from django.db.models import fields
from .models import Post
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostForm(forms.ModelForm):
    class Meta:
        # model = 모델 클래스명  괄호는 뺄것
        model = Post
        fields = ['title', 'content', 'type', 'dt_created']
        widget = {
            'content': SummernoteInplaceWidget()
        }
