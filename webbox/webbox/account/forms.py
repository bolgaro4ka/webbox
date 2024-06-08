from django import forms
from django.contrib.auth.models import User

from .models import Comment

class LoginForm(forms.Form):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'login-username'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'login-password'}))

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')