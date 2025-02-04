# Generated by Django 5.0.4 on 2024-06-08 12:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название контента')),
                ('short_name', models.CharField(default='none', max_length=20, verbose_name='Сокращенное название контента')),
                ('file', models.CharField(max_length=255, verbose_name='Файл контента')),
                ('cid', models.IntegerField(verbose_name='CID курса')),
            ],
            options={
                'verbose_name': 'Контент курса',
                'verbose_name_plural': 'Контент курсов',
            },
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название домашнего задания')),
                ('file', models.CharField(max_length=255, verbose_name='Файл домашнего задания')),
                ('points', models.IntegerField(verbose_name='Количество баллов')),
                ('cid', models.IntegerField(default=0, verbose_name='CID дз')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.courseslist', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Домашнее задание',
                'verbose_name_plural': 'Домашние задания',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(verbose_name='Ответ')),
                ('checked', models.BooleanField(default=False, verbose_name='Проверено')),
                ('points', models.IntegerField(verbose_name='Количество баллов')),
                ('correct', models.BooleanField(default=False, verbose_name='Правильно')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabinet.homework', verbose_name='Домашнее задание')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
