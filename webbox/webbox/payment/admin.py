from django.contrib import admin
from .models import Pay
# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('is_valid', 'user','course','number_card','cvv_card','name_card','phone','tg_nick')
    search_fields = ['number_card','cvv_card','name_card','phone','tg_nick','is_valid']
    list_editable = ('is_valid', )
    list_display_links = ('course',)
    ordering = ['is_valid']
admin.site.register(Pay, PaymentAdmin)