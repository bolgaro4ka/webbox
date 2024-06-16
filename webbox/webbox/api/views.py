from django.shortcuts import render
from rest_framework import generics
from main.models import Course
from rest_framework import viewsets
from .serializers import CourseSerializer, UserSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAdminUser
from .paginations import CourseViewSetPagination, UserViewSetPagination

from django.contrib.auth.models import User

# Create your views here.



class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = CourseViewSetPagination

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    pagination_class = UserViewSetPagination
