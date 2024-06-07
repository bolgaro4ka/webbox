from django.urls import path
from . import views

urlpatterns = [
    # post views
    path('', views.user_login, name='login'),
    path('u/', views.user_unlogin, name='unlogin'),
    path('r/', views.register, name='reg'),
    path('comment/', views.commentsForm, name='test'),
]