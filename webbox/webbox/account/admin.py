from django.contrib import admin
from .models import Comment
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'body', 'email', 'created_on',  )
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    list_editable=('active', )


admin.site.register(Comment, CommentAdmin)
