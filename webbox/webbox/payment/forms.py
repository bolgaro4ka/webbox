from django import forms
from main.models import CoursesList
from django.core import validators
from .models import Pay
from main.models import CoursesList
import re

def validate_phone(value):
    patern = re.compile(r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$')
    if not patern.match(value):
        raise forms.ValidationError("Это некорректный номер телефона")
    
def validate_tg_nick(value):
    patern = re.compile(r'^@[\w-]+$')
    if not patern.match(value):
        raise forms.ValidationError("Это некорректный ник в телеграмме (он не начинается с @)")
    
def validate_number_card(value):
    patern = re.compile(r'^[0-9]{16}$')
    if not patern.match(value):
        raise forms.ValidationError("Это некорректный номер карты")
    
def validate_cvv_card(value):
    patern = re.compile(r'^[0-9]{3}$')
    if not patern.match(value):
        raise forms.ValidationError("Это некорректный cvv карты")
class PaymentForm(forms.Form):
    a = CoursesList.objects.all()
    course = forms.ModelChoiceField(queryset=a)
    number_card = forms.CharField(validators=[validate_number_card], help_text="16 цифр. Например: 1234567890123456")
    cvv_card = forms.CharField(help_text="3 цифры", validators=[validate_cvv_card], max_length=3)
    name_card = forms.CharField(max_length=255, help_text="Например: Иванов Иван Иванович, Ivanov Ivan Ivanov или Ivanov Ivan")
    phone = forms.CharField(max_length=255, validators=[validate_phone], help_text="Например: +7 (999) 999-99-99 или 8 999 999 99 99")
    tg_nick = forms.CharField(max_length=255, validators=[validate_tg_nick], help_text="Например: @IvanovIvanIvanov")

    class Meta:
        model = Pay
        fields = ['number_card', 'cvv_card', 'name_card', 'phone', 'tg_nick']