# Generated by Django 4.1.4 on 2022-12-17 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('panel', '0006_iteam_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iteam',
            old_name='data_updated',
            new_name='date_updated',
        ),
        migrations.RemoveField(
            model_name='iteam',
            name='data_created',
        ),
        migrations.AddField(
            model_name='iteam',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='iteam',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='iteam',
            name='content',
            field=models.TextField(blank=True, help_text='не более 5000 символов', max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='iteam',
            name='title',
            field=models.CharField(help_text='не более 200 символов', max_length=200),
        ),
    ]