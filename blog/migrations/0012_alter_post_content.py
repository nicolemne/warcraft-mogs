# Generated by Django 3.2.19 on 2023-06-14 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default='exit'),
            preserve_default=False,
        ),
    ]