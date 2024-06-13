from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('money/<int:cid>/', views.pay, name='pay')
]