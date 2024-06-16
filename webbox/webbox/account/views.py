from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from django.views.decorators.clickjacking import xframe_options_exempt
from .forms import CommentForm
from .models import Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Count

def user_login(request):
    if request.method == 'POST':
        error={}
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("/u")
                else:
                    
                    error["name"]="Disabled account"
                    error["description"] = "Пользователь заблокирован. Обратитесь к администратору"

                    return HttpResponse('Disabled account')
            else:
                error["name"] = "Invalid login"
                error["description"] = "Неверное имя пользователя или пароль"
                error["code"] = 403
                return render(request, 'errors_form.html', {'error': error})
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def user_unlogin(request):
    logout(request)
    return redirect("/")

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
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

@xframe_options_exempt
def commentsForm(request):
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_comment = comment_form.save()
    else:
        comment_form = CommentForm()
    comments = Comment.objects.all()
    return render(request, 'account/comments.html', {'comment_form': comment_form, 'new_comment': new_comment, 'comments': comments})