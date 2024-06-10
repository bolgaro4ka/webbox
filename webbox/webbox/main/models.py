from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from lessions.models import Theme

# Create your models here.




class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название курса")
    description = models.TextField(verbose_name="Описание курса")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания курса")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления курса")
    picture_preview = models.ImageField(upload_to='base/img/%Y/%m/%d', help_text='Эта картинка отображается на главной странице в карточкке курса.', default="webbox/img/placeholders/my_friend.jpg", verbose_name="Картинка курса (маленькая)")
    picture = models.ImageField(upload_to='base/img/%Y/%m/%d', help_text='Большая картинка.', default="webbox/img/placeholders/my_friend.jpg", verbose_name="Картинка курса (средняя)")
    is_published  = models.BooleanField(default=True, verbose_name="Публикация курса")
    short_name = models.CharField(max_length=20, default="none", verbose_name="Сокращенное название курса")
    price=models.CharField(max_length=255, default="none рублей", verbose_name="Цена курса с указанием единиц", help_text="Можно использовать html")
    clear_price=models.BigIntegerField(default=0, verbose_name="Цена (только число)")
    long_description = models.TextField(default="nn", help_text="Полное описание курса. Отображается на странице курса", verbose_name="Описание курса")
    themes = models.ManyToManyField(Theme, verbose_name="Темы курса")

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self) -> str:
        return self.title
    

class UserCourses(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=4, verbose_name="Курс")

    @receiver(post_save, sender=User)
    def create_user_usercourses(sender, instance, created, **kwargs):
        if created:
            UserCourses.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_usercourses(sender, instance, **kwargs):
        instance.usercourses.save()


    class Meta:
        verbose_name = 'Курс пользователя'
        verbose_name_plural = 'Курсы пользователей'

    def __str__(self) -> str:
        return self.user.username


