from django.shortcuts import render
from main.models import Course
from .forms import TelegramGenericForm

# Create your views here.

def index(request):
    courses = Course.objects.all()
    return render(request, 'telegram/index.html', {'courses': courses})

def pay(request, cid):
    if request.method == 'POST':
        error={}
        form = TelegramGenericForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    else:
        form = TelegramGenericForm()
    return render(request, 'telegram/payment.html', {'cid': cid, 'form': form})