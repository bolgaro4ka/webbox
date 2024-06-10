from django.contrib import admin
from .models import Homework, Answer
from lessions.models import Lession, Theme


class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ()
    search_fields = ['name', 'lessions']
    list_editable = ()
    filter_horizontal = ('lessions', )

admin.site.register(Theme, ThemeAdmin)

# Register your models here.
class LessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'file', 'cid')
    list_display_links = ()
    search_fields = ['name', 'short_name', 'file',]
    list_editable = ('cid',)
    

admin.site.register(Lession, LessionAdmin)


class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'file', 'cid', 'points')
    list_display_links = ()
    search_fields = ['name', 'file', 'points', 'cid']
    list_editable = ()

admin.site.register(Homework, HomeworkAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 'homework', 'checked', 'correct')
    list_display_links = ()
    search_fields = ['answer', 'homework', 'checked', 'correct']
    list_editable = ()

admin.site.register(Answer, AnswerAdmin)
