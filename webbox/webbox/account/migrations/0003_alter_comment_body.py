# Generated by Django 5.0.3 on 2024-03-31 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_comment_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(default='Текст комментария', unique=True),
        ),
    ]
