from django.db import models

# Create your models here.

class Lession(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название контента")
    short_name = models.CharField(max_length=20, default="none", verbose_name="Сокращенное название контента")
    file = models.CharField(max_length=255, verbose_name="Файл контента")
    cid = models.IntegerField(verbose_name="CID курса")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Theme(models.Model):
    name = models.CharField(max_length=255)
    lessions = models.ManyToManyField(Lession)

    def __str__(self):
        return self.code
    
    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'    
    
