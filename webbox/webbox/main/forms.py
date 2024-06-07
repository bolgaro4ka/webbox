from django import forms
from django.contrib.auth.models import User

class Filter(forms.Form):
    field_search = forms.CharField(max_length=255, required=False, label='Поиск')
    price_from = forms.IntegerField(label="Цена от", required=False)
    price_to = forms.IntegerField(label="до", required=False)
