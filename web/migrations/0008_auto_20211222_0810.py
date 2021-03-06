# Generated by Django 2.2 on 2021-12-22 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20211222_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_content',
            name='project_id',
            field=models.ForeignKey(db_column='project_id', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project_id', to='web.Project'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('django', 'django'), ('algorithm', 'algorithm'), ('javascript', 'javascript'), ('python', 'python'), ('css', 'css'), ('html', 'html'), ('node', 'node'), ('DB', 'DB'), ('react', 'react')], default='css', max_length=80, null=True),
        ),
    ]
