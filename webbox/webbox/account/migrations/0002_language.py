# Generated by Django 5.0.4 on 2024-06-10 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Язык')),
                ('code', models.CharField(max_length=255, verbose_name='Код языка')),
            ],
        ),
    ]