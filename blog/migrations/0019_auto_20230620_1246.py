# Generated by Django 3.2.19 on 2023-06-20 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20230620_0019'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('cloth', 'cloth'), ('leather', 'leather'), ('mail', 'mail'), ('plate', 'plate')], default='cloth', max_length=100),
        ),
    ]
