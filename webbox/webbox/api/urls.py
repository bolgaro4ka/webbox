from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from rest_framework import routers

from django.urls import re_path

router = routers.DefaultRouter()
router.register(r'course', views.CourseViewSet)
router.register(r'user', views.UserViewSet)


urlpatterns = [
   # path('v1/course/', views.CourseViewSet.as_view({'get': 'list'}), name='index'),
   # path('v1/course/<int:pk>/', views.CourseViewSet.as_view({'put': 'update'}), name='index_pk'),

    path('v1/', include(router.urls)),
    path('v1/drf-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
