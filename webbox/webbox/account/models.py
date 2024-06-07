from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Comment(models.Model):
    name = models.CharField(max_length=80, verbose_name='Имя')
    email = models.EmailField(verbose_name='Электронная почта')
    body = models.TextField(default='Текст комментария', unique=True, verbose_name='Текст комментария')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания комментария')
    active = models.BooleanField(default=False, verbose_name='Публикация комментария')

    class Meta:
        ordering = ['created_on']
        verbose_name = 'коментарий'
        verbose_name_plural = 'коментарии'

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)