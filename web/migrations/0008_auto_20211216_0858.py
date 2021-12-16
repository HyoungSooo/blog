# Generated by Django 2.2 on 2021-12-16 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20211216_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dt_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('django', 'django'), ('javascript', 'javascript'), ('python', 'python'), ('html', 'html'), ('algorithm', 'algorithm'), ('react', 'react'), ('css', 'css'), ('DB', 'DB')], default='css', max_length=80, null=True),
        ),
    ]