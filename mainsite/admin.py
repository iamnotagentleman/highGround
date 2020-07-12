from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Site, User


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
    list_filter = ['is_staff', 'is_superuser', 'gender']