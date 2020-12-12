# Generated by Django 2.2.6 on 2020-12-09 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20201209_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.ForeignKey(help_text='Введите свой комментарий', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='posts.Comment', verbose_name='Комментарий'),
        ),
    ]
