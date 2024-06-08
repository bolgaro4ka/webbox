from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
from cabinet.models import Homework
from django.urls import reverse

from cabinet.forms import HomeworkForm
from cabinet.models import Answer

from .models import Lession
from django.views.decorators.clickjacking import xframe_options_exempt
from django.db import connection

def truncate(model):
    with connection.cursor() as cursor:
        cursor.execute(f'DROP TABLE "{model._meta.db_table}";')
# Create your views here.
@login_required(login_url='/a')
def cabinet(request):
    if request.user.is_authenticated:
        text_button_enter = 'Выход'
    else:
        text_button_enter = 'Вход'
    listofCourses = Lession.objects.all().filter(short_name=request.user.usercourses.course.short_name).order_by('cid')
    homeworks = Homework.objects.all().filter(course=request.user.usercourses.course).order_by('cid')
    return render(request, 'cabinet/cabinet.html', {'text_button_enter': text_button_enter, 'listofCourses': listofCourses, 'homeworks': homeworks})


@login_required(login_url='/a')
def course(request, short_name, cid):

    url = (request.path)
    error={}
    if Lession.objects.all().filter(short_name=request.user.usercourses.course.short_name).filter(cid=cid) and short_name==request.user.usercourses.course.short_name:
        pass
    
    else:
        error['name'] = "Курс не существует"
        error['description'] = "Вы не можете получить доступ к этой странице или такого урока к курсу не существует"
        return render(request, 'errors_form.html', {'error': error})
    
    all_homeworks = Homework.objects.all().filter(course=request.user.usercourses.course).order_by('cid')
    all_courses = Lession.objects.all().filter(short_name=request.user.usercourses.course.short_name).order_by('cid')
    if 'course' in url:
        listofCourses = Lession.objects.all().filter(short_name=request.user.usercourses.course.short_name).filter(cid=cid)[0]
        listofHomeworks = False
    else:
        
        listofHomeworks = all_homeworks.filter(cid=cid)[0]
        listofCourses = False
    
    return render(request, 'cabinet/course.html', {'short_name': request.user.usercourses.course.short_name, 'cid': cid, 'listofCourses': listofCourses, 'all_courses': all_courses, 'name_course': listofCourses.name if listofCourses else listofHomeworks.name, 'listofHomeworks': listofHomeworks, 'homeworks': all_homeworks})


@login_required(login_url='/a')
@xframe_options_exempt
def course_raw(request, short_name, cid):
    #truncate(Answer)
    #Answer.save()
    url = (request.path)
    error={}
    if Lession.objects.all().filter(short_name=request.user.usercourses.course.short_name).filter(cid=cid):
        pass
    else:
        error['name'] = "Курс не существует"
        error['description'] = "Вы не можете получить доступ к этой странице или такого урока к курсу не существует"
        return render(request, 'errors_form.html', {'error': error})
    
    if 'course' in url:
        listofCourses = Lession.objects.all().filter(short_name=request.user.usercourses.course.short_name, cid=cid)
        form = False
        code = ''
    else:
        listofCourses = Homework.objects.all().filter(cid=cid, course=request.user.usercourses.course)
        if Answer.objects.all().filter(homework=listofCourses[0], user=request.user):
            
            code = Answer.objects.all().filter(homework=listofCourses[0]).filter(user=request.user)[0].answer
            print(f'Yeap {code}')
        else:
            code = ''
            print('Nope')

        if request.method == 'POST':
            form = HomeworkForm(request.POST)
            if form.is_valid():
                if Answer.objects.all().filter(homework=listofCourses[0]):
                    Answer.objects.filter(homework=listofCourses[0], user=request.user).update(answer=form.cleaned_data['answer'], checked=False, correct=False)
                    
                else:
                    new_ans = Answer.objects.all().create(answer=form.cleaned_data['answer'], homework=listofCourses[0], checked=False, correct=False, points=Homework.objects.all().filter(cid=cid, course=request.user.usercourses.course)[0].points, user=request.user)
                    new_ans.save()
                return HttpResponse('Сохранено')
        else:
            form = HomeworkForm()
            
    return render(request, f'{listofCourses[0].file}', {'form': form, 'lang': request.user.usercourses.course.short_name, 'code': code})
