from django.shortcuts import render
from main.models import Course

# Create your views here.

def index(request):
    courses = Course.objects.all()
    return render(request, 'telegram/index.html', {'courses': courses})