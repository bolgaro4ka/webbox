# Generated by Django 5.0.3 on 2024-04-02 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_comment_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Публикация комментария'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(default='Текст комментария', unique=True, verbose_name='Текст комментария'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания комментария'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Имя'),
        ),
    ]
