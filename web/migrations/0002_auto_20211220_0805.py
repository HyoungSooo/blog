# Generated by Django 2.2 on 2021-12-20 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('algorithm', 'algorithm'), ('html', 'html'), ('node', 'node'), ('django', 'django'), ('react', 'react'), ('css', 'css'), ('DB', 'DB'), ('javascript', 'javascript'), ('python', 'python')], default='css', max_length=80, null=True),
        ),
    ]
