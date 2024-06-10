from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.cabinet, name='index'),
    path('course/lessions/<int:cid>/', views.lessions, name='lessions'),
    path('course/<str:short_name>/<int:cid>/', views.course, name='course'),
    path('course/<str:short_name>/<int:cid>/raw/', views.course_raw, name='course_raw'),
    path('homework/<str:short_name>/<int:cid>/raw/', views.course_raw, name='homework_raw'),
    path('homework/<str:short_name>/<int:cid>/', views.course, name='homework'),
    
]