# Generated by Django 5.0.6 on 2024-06-16 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0004_remove_homework_course'),
        ('main', '0004_alter_course_picture_alter_course_picture_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='homeworks',
            field=models.ManyToManyField(to='cabinet.homework', verbose_name='Домашние задания'),
        ),
    ]