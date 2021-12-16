# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django_summernote import models as summer_model
from django_summernote import fields as summer_fields

LANG_TYPE = {
    ('python', 'python'),
    ('javascript', 'javascript'),
    ('html', 'html'),
    ('css', 'css'),
    ('react', 'react'),
    ('django', 'django'),
    ('DB', 'DB'),
    ('algorithm', 'algorithm')
}

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = summer_fields.SummernoteTextField(default='')
    type = models.CharField(
        max_length=80, choices=LANG_TYPE, null=True, default='css')
    description = models.CharField(max_length=200, default='')
    dt_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Create your models here.


class Super_User(AbstractUser):
    pass
