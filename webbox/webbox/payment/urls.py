from django.urls import path
from . import views

urlpatterns = [
    # post views
    path('', views.index, name='payment'),
    path('pre_success/', views.pre_success, name='pre_success'),
    path('success/', views.success, name='success'),
    path('unpay/', views.unpay, name='unpay'),
]