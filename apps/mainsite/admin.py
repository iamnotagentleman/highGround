from django.contrib import admin
from django.http import HttpResponse
from simple_history.admin import SimpleHistoryAdmin
from apps.mainsite.app_models.sites import Site
from apps.mainsite.app_models.checks import Check
from apps.mainsite.app_models.users import User
from apps.mainsite.app_models.courses import Course
import csv


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response

    export_as_csv.short_description = "Export Selected"


class CommonAdmin(SimpleHistoryAdmin, ExportCsvMixin):
    empty_value_display = '-empty-'
    actions = ['export_as_csv']
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