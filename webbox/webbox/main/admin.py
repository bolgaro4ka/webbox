from django.contrib import admin
from .models import CoursesList, UserCourses
# Register your models here.

class CoursesListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at', 'updated_at', 'is_published', "short_name")
    list_display_links = ('id', 'title')
    search_fields = ["title", "description", "short_name"]
    list_editable = ('is_published',)

admin.site.register(CoursesList, CoursesListAdmin)


class UserCoursesAdmin(admin.ModelAdmin):
    list_display = ('user', 'course',)

admin.site.register(UserCourses, UserCoursesAdmin)
