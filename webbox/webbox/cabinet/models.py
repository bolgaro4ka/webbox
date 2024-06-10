
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from main.models import Course


class Homework(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название домашнего задания")
    file = models.CharField(max_length=255, verbose_name="Файл домашнего задания")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    points = models.IntegerField(verbose_name="Количество баллов")
    cid = models.IntegerField(verbose_name="CID дз", default=0,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашние задания'

class Answer(models.Model):
    answer = models.TextField(verbose_name="Ответ")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, verbose_name="Домашнее задание")
    checked = models.BooleanField(default=False, verbose_name="Проверено")
    points = models.IntegerField(verbose_name="Количество баллов")
    correct = models.BooleanField(default=False, verbose_name="Правильно")

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'