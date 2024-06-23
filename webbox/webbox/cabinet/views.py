from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
from cabinet.models import Homework
from django.urls import reverse

from cabinet.forms import HomeworkForm
from cabinet.models import Answer
from lessions.models import Theme

from lessions.models import Lession
from django.views.decorators.clickjacking import xframe_options_exempt
from django.db import connection
from main.models import Course
from .forms import SearchForm

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
    #listofCourses = Lession.objects.all().filter(short_name=request.user.usercourses.course.short_name).order_by('cid')
    themes = Course.objects.all().filter(short_name=request.user.usercourses.course.short_name)[0].themes.all().order_by('cid')
    lens = [len(theme.lessions.all()) for theme in themes]
    homeworks = Course.objects.all().filter(short_name=request.user.usercourses.course.short_name)[0].homeworks.all().order_by('cid')
    return render(request, 'cabinet/cabinet.html', {'text_button_enter': text_button_enter, 'themes': zip(themes, lens), 'homeworks': homeworks})


@login_required(login_url='/a')
def course(request, short_name, cid):
    all_courses = []
    all_homeworks = []
    if request.method == 'POST':
            form = SearchForm(request.POST)
            dz_form = SearchForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                print(cd['search'])
                all_courses = [Lession.objects.all().filter(short_name=request.user.usercourses.course.short_name).filter(name__icontains=cd['search'])]
                print(all_courses)

            if dz_form.is_valid():
                cdz =dz_form.cleaned_data
                print(cdz['search'])
                all_homeworks = Course.objects.all().filter(short_name=request.user.usercourses.course.short_name)[0].homeworks.all().order_by('cid').filter(name__icontains=cdz['search'])
                if not all_homeworks: all_homeworks = 'none'
                print(all_homeworks)
                
    else:
        form = SearchForm()
        dz_form = SearchForm()
    

    url = (request.path)
    print(Lession.objects.all().filter(short_name=request.user.usercourses.course.short_name).filter(cid=cid), request.user.usercourses.course.short_name)
    error={}
    if Lession.objects.all().filter(short_name=request.user.usercourses.course.short_name).filter(cid=cid) and short_name==request.user.usercourses.course.short_name:
        pass
    
    else:
        error['name'] = "Курс не существует"
        error['description'] = "Вы не можете получить доступ к этой странице или такого урока к курсу не существует"
        error['code'] = 404
        return render(request, 'errors_form.html', {'error': error})
    
    if (not all_homeworks) and (all_homeworks != 'none'): all_homeworks = Course.objects.all().filter(short_name=request.user.usercourses.course.short_name)[0].homeworks.all().order_by('cid')
    elif all_homeworks == 'none': all_homeworks = []
    #all_courses = Lession.objects.all().filter(short_name=request.user.usercourses.course.short_name).order_by('cid')
    all_themes = Course.objects.all().filter(short_name=request.user.usercourses.course.short_name)[0].themes.all().order_by('cid')
    print(all_themes)
    if not all_courses:
    
        for item in all_themes:
            all_courses.append(item.lessions.all().order_by('cid'))

    print(all_courses)
    if 'course' in url:
        try:
            listofCourses = Lession.objects.all().filter(short_name=request.user.usercourses.course.short_name).filter(cid=cid)[0]
        except Exception as e:
            error['name'] = "Курс не существует"
            error['description'] = f"Вы не можете получить доступ к этой странице или такого урока к курсу не существует ({e})"
            error['code'] = 404
            return render(request, 'errors_form.html', {'error': error})
        listofHomeworks = False
    else:
        try:
            listofHomeworks = Course.objects.all().filter(short_name=request.user.usercourses.course.short_name)[0].homeworks.all().order_by('cid').filter(cid=cid)[0]
        except Exception as e:
            error['name'] = "ДЗ не существует"
            error['description'] = f"Вы не можете получить доступ к этой странице или такого ДЗ к курсу не существует ({e})"
            error['code'] = 404
            return render(request, 'errors_form.html', {'error': error})
        listofCourses = False
    
    return render(request, 'cabinet/course.html', {'short_name': request.user.usercourses.course.short_name, 'cid': cid, 'listofCourses': listofCourses, 'all_courses': all_courses, 'name_course': listofCourses.name if listofCourses else listofHomeworks.name, 'listofHomeworks': listofHomeworks, 'homeworks': all_homeworks, 'form': form, 'dz_form': dz_form})


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
        error['code'] = 404
        return render(request, 'errors_form.html', {'error': error})
    
    if 'course' in url:
        listofCourses = Lession.objects.all().filter(short_name=request.user.usercourses.course.short_name, cid=cid)
        form = False
        code = ''
    else:
        listofCourses = Course.objects.all().filter(short_name=request.user.usercourses.course.short_name)[0].homeworks.all().filter(cid=cid).order_by('cid')
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


def lessions(request,  cid ):
    theme = Theme.objects.all().filter(short_name=request.user.usercourses.course.short_name).filter(cid=cid)[0]
    lessions = theme.lessions.all().order_by('cid')
    print(lessions)
    return render(request, 'cabinet/lessions.html', {'lessions': lessions, 'theme': theme})