from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Site, User, Course, Check


class CommonAdmin(SimpleHistoryAdmin):
    empty_value_display = '-empty-'
    ...


@admin.register(Site)
class SiteAdmin(CommonAdmin):
    list_display = ['name', 'year', 'domain', 'event_start_date', 'event_end_date']
    list_filter = ['year', 'event_start_date', 'event_end_date', 'is_active']
    date_hierarchy =  'event_start_date'


@admin.register(User)
class UserAdmin(CommonAdmin):
    list_display = ['username', 'email', 'phone_number', 'is_staff']
    list_filter = ['is_staff', 'is_superuser', 'gender', 'is_active']


@admin.register(Course)
class CourseAdmin(CommonAdmin):
    list_display = ['name', 'lecturers']
    list_filter = ['site', 'assistant', 'lecturer']

    @staticmethod
    def lecturers(obj):
        return "\n".join([l.email for l in obj.lecturer.filter(is_staff=True)])


@admin.register(Check)
class CheckAdmin(CommonAdmin):
    list_display = ["start_check", "end_check"]
    list_filter = ["start_check", "end_check"]