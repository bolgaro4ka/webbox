from django.db import models
from main.models import User, CoursesList
# Create your models here.
class Pay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    course = models.ForeignKey(CoursesList, on_delete=models.CASCADE, verbose_name='Курс')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты')
    number_card = models.CharField(max_length=255, verbose_name='Номер карты')
    cvv_card = models.CharField(max_length=255, verbose_name='CVV')
    name_card = models.CharField(max_length=255, verbose_name='Имя владельца карты')
    phone = models.CharField(max_length=255, verbose_name='Телефон')
    tg_nick = models.CharField(max_length=255, verbose_name='Ник в телеграм')
    is_valid=models.BooleanField(default=True, verbose_name='Пользователь не переведён на курс')
    def __str__(self):
        return self.number_card
    
    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'