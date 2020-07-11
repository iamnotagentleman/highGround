from django.contrib import admin
from .common import CommonAdmin
from ..Models.Core.site import Site


@admin.site.register(Site)
class SiteAdmin(CommonAdmin):
    list_display = ['name', 'year', 'domain', 'event_start_date', 'event_end_date']
    list_filter = ['year', 'event_start_date', 'event_end_date', 'is_active']