# Generated by Django 5.0.4 on 2024-06-10 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_course_themes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='picture',
            field=models.ImageField(default='webbox/img/placeholders/my_friend.jpg', help_text='Большая картинка.', upload_to='base/img/%Y/%m/%d', verbose_name='Картинка курса (средняя)'),
        ),
        migrations.AlterField(
            model_name='course',
            name='picture_preview',
            field=models.ImageField(default='webbox/img/placeholders/my_friend.jpg', help_text='Эта картинка отображается на главной странице в карточкке курса.', upload_to='base/img/%Y/%m/%d', verbose_name='Картинка курса (маленькая)'),
        ),
    ]
