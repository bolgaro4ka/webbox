# Generated by Django 5.0.6 on 2024-06-27 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0005_answer_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='comment',
            field=models.TextField(default='Замечательная работа!', help_text='Можно использовать HTML', null=True, verbose_name='Коментарий к дз'),
        ),
    ]