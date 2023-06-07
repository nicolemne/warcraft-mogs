# Generated by Django 3.2.19 on 2023-06-06 21:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='usercomments',
            field=models.ManyToManyField(blank=True, related_name='blog_usercomments', to=settings.AUTH_USER_MODEL),
        ),
    ]
