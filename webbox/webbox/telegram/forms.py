from django import forms
from django.contrib.auth.models import User
from payment.forms import *

class TelegramGenericForm(forms.Form):
    full_name = forms.CharField(max_length=255)
    tg_nick = forms.CharField(max_length=255, validators=[validate_tg_nick], help_text="Например @vova")
    a = Course.objects.all().filter(is_published=True)
    course = forms.ModelChoiceField(queryset=a)
    number_card = forms.CharField(validators=[validate_number_card], help_text="16 цифр. Например: 1234567890123456")
    cvv_card = forms.CharField(help_text="3 цифры", validators=[validate_cvv_card], max_length=3)
    phone = forms.CharField(max_length=255, validators=[validate_phone], help_text="Например: +7 (999) 999-99-99 или 8 999 999 99 99")



