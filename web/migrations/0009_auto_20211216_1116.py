# Generated by Django 2.2 on 2021-12-16 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20211216_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('javascript', 'javascript'), ('html', 'html'), ('DB', 'DB'), ('react', 'react'), ('django', 'django'), ('python', 'python'), ('css', 'css'), ('algorithm', 'algorithm')], default='css', max_length=80, null=True),
        ),
    ]
