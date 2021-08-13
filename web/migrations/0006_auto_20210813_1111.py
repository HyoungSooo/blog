# Generated by Django 2.1 on 2021-08-13 11:11

from django.db import migrations, models
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20210813_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django_summernote.fields.SummernoteTextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('html', 'html'), ('javascript', 'javascript'), ('css', 'css'), ('react', 'react'), ('python', 'python'), ('django', 'django')], max_length=80, null=True),
        ),
    ]
