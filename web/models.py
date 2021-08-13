# Create your models here.
from django.db import models
from django_summernote import models as summer_model
from django_summernote import fields as summer_fields

LANG_TYPE = {
    ('python', 'python'),
    ('javascript', 'javascript'),
    ('html', 'html'),
    ('css', 'css'),
    ('react', 'react'),
    ('django', 'django')
}

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = summer_fields.SummernoteTextField(default='')
    type = models.CharField(max_length=80, choices=LANG_TYPE, null=True)
    description = models.CharField(max_length=200, default='')
    dt_created = models.DateField()

    def __str__(self):
        return self.title
