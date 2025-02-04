from django.shortcuts import render
from rest_framework import generics
from main.models import Course
from rest_framework import viewsets
from .serializers import CourseSerializer, UserSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAdminUser
from .paginations import CourseViewSetPagination, UserViewSetPagination

from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
import psutil

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


class StatusView(generics.GenericAPIView):
    def get(self, request, format=None):
        python_process = psutil.Process()
        return Response({"status": "ok",
                        "cpu": psutil.cpu_percent(), 
                        'name': 'Main server Paia1nik #1',
                        "memory": psutil.virtual_memory().percent,
                        'cores': psutil.cpu_count(logical=False),
                        "disk": psutil.disk_usage('/').percent, 
                        "python_ram": f"{python_process.memory_info()[0] / 2.**30:.2f} GB",
                        "network": f"{psutil.net_io_counters().bytes_sent / 2.**20:.2f} MB отправлено, {psutil.net_io_counters().bytes_recv / 2.**20:.2f} MB получено", 
                        "total_network": psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv,
                        "time": psutil.boot_time(),
                        "users": len(User.objects.all())})