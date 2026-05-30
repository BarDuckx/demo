from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Application

admin.site.register(User, UserAdmin)

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'user', 'status', 'start_date', 'created_at')
    list_filter = ('status', 'course_name')
    search_fields = ('user__username', 'user__fio')