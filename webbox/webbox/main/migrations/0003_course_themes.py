# Generated by Django 5.0.4 on 2024-06-10 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessions', '0001_initial'),
        ('main', '0002_rename_courseslist_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='themes',
            field=models.ManyToManyField(to='lessions.theme', verbose_name='Темы курса'),
        ),
    ]
