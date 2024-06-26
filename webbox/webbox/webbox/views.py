from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from main.models import Course, UserCourses
from account.models import Comment
from main.forms import Filter

def cats(request, code):
    error = {}
    error['name'] = 'Ошибочка!'
    error['description'] = 'Вы нашли секрет!'
    error['code'] = code
    print(error)
    return render(request, 'errors_form.html', {'error': error})

def indexView(request): 
    comments = Comment.objects.all()
    if request.method == 'POST':
        error={}
        form = Filter(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if not cd['price_from']: cd['price_from'] = 0
            if not cd['price_to']: cd['price_to'] = 1000000000000000000000000000000000
            else: cd['price_to']=cd['price_to']+1

            courses_list = Course.objects.all().filter(title__icontains=cd['field_search'], clear_price__gt=cd['price_from'], clear_price__lt=cd['price_to'] )
            if not courses_list:
                courses_list = Course.objects.all().filter(description__icontains=cd['field_search'], clear_price__gt=cd['price_from'], clear_price__lt=cd['price_to'] )
                if not courses_list: courses_list = Course.objects.all().filter(price__icontains=cd['field_search'], clear_price__gt=cd['price_from'], clear_price__lt=cd['price_to'] )
    else:
        form = Filter()
        courses_list = Course.objects.all()

    len_users = len(UserCourses.objects.all())
    return render(request, 'webbox/index.html', {'courses_list':courses_list, 'comments': comments, 'form': form, 'len_users': len_users})
    
def cardInfo(request, short_name):
    error={}
    if Course.objects.all().filter(short_name=short_name):
        course = Course.objects.all().filter(short_name=short_name)[0]
        all_users = len(UserCourses.objects.all().filter(course=course))
    else:
        error['name'] = "Курс не существует"
        error['description'] = "Вы не можете получить доступ к этой странице или такого урока к курсу не существует"
        return render(request, 'errors_form.html', {'error': error})
    return render(request, 'webbox/info_course.html', {'course': course, 'number_of_users': all_users, 'sh': short_name})