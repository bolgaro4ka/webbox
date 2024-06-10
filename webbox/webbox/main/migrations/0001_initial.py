# Generated by Django 5.0.4 on 2024-06-08 12:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursesList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название курса')),
                ('description', models.TextField(verbose_name='Описание курса')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания курса')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления курса')),
                ('picture_preview', models.CharField(default='webbox/img/placeholders/my_friend.jpg', help_text='Эта картинка отображается на главной странице в карточкке курса. Значение - путь к картинке на сервере от папки static', max_length=255, verbose_name='Картинка курса (маленькая)')),
                ('picture', models.CharField(default='webbox/img/placeholders/my_friend.jpg', help_text='Большая картинка. Значение - путь к картинке на сервере от папки static', max_length=255, verbose_name='Картинка курса (средняя)')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация курса')),
                ('short_name', models.CharField(default='none', max_length=20, verbose_name='Сокращенное название курса')),
                ('price', models.CharField(default='none рублей', help_text='Можно использовать html', max_length=255, verbose_name='Цена курса с указанием единиц')),
                ('clear_price', models.BigIntegerField(default=0, verbose_name='Цена (только число)')),
                ('long_description', models.TextField(default='nn', help_text='Полное описание курса. Отображается на странице курса', verbose_name='Описание курса')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='UserCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='main.courseslist', verbose_name='Курс')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Курс пользователя',
                'verbose_name_plural': 'Курсы пользователей',
            },
        ),
    ]