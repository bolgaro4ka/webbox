from django.shortcuts import render
from main.models import Course
from .forms import TelegramGenericForm
from account.forms import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponse
from lessions.models import Lession
import random
from payment.models import Pay
from django.utils import timezone

# Create your views here.

def index(request):
    courses = Course.objects.all()
    rand_number = random.randint(0, 9)
    return render(request, 'telegram/index.html', {'courses': courses, 'rand_number': rand_number})

def pay(request, cid):
    if request.method == 'POST':
        error={}
        form = TelegramGenericForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            pay = Pay.objects.create(
                user=request.user,
                course = cd['course'],
                number_card = cd['number_card'],
                cvv_card = cd['cvv_card'],
                name_card = cd['full_name'],
                phone = cd['phone'],
                tg_nick = cd['tg_nick'],
            )

            pay.save()
            info = {'name': f'Ваша оплата прошла успешно!', 'description': f'Ожидайте сообщения в телеграмм по нику {cd["tg_nick"]} об успешном зачислении!'}

            return render(request, 'telegram/info.html', {'info': info})

    else:
        form = TelegramGenericForm()
    return render(request, 'telegram/payment.html', {'cid': cid, 'form': form})

def user_logout(request):
    logout(request)
    return redirect("/t/")

def user_login(request):
    if request.method == 'POST':
        error={}
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user=user)
                    return redirect("/t/")
                else:
                    
                    error["name"]="Disabled account"
                    error["description"] = "Пользователь заблокирован. Обратитесь к администратору"

                    return HttpResponse('Disabled account')
            else:
                error["name"] = "Invalid login"
                error["description"] = "Неверное имя пользователя или пароль"
                return render(request, 'telegram/errors.html', {'error': error})
    else:
        form = LoginForm()
    return render(request, 'telegram/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return redirect("/t/l/")
    else:
        user_form = UserRegistrationForm()
    return render(request, 'telegram/register.html', {'user_form': user_form})
@login_required(login_url='/t/l/')
def article(request, id):
    lession = Lession.objects.all().get(id=id)

    return render(request, lession.file, {'id': id, 'tg_view': True})

@login_required(login_url='/t/l/')
def lessions(request):
    lessions = Lession.objects.all().filter(short_name=request.user.usercourses.course.short_name)
    course = request.user.usercourses.course
    rand_number = random.randint(0, 9)
    return render(request, 'telegram/lessions.html', {'lessions': lessions, 'course': course, 'rand_number': rand_number})