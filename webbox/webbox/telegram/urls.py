from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('money/<int:cid>/', views.pay, name='pay'),
    path('l/', views.login, name="login"),
    path('r/', views.register, name='req'),
    path('a/', views.lessions, name="lessions"),
    path('a/<int:id>/', views.article, name="article"),
    path('u/', views.user_unlogin, name='unlogin'),
]