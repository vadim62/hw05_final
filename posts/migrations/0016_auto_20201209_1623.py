# Generated by Django 2.2.6 on 2020-12-09 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_auto_20201209_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(help_text='Введите текст комментария', max_length=200, verbose_name='Текст'),
        ),
    ]
