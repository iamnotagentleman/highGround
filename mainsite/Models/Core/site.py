from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from ..base import ModelBase


class Site(ModelBase):
    name = models.CharField(verbose_name=_("Site Name"), max_length=255)
    year = models.CharField(verbose_name=_("Year"), max_length=4)
    logo = models.ImageField(verbose_name=_("Logo"), upload_to="images/")
    is_active = models.BooleanField(verbose_name=_("Is Active"), default=False)
    home_url = models.CharField(verbose_name=_("Home Url"), max_length=128, null=True)
    domain = models.CharField(verbose_name=_("domain"), max_length=128, null=True,
                              help_text=_("To parse incoming requests and show correct page"))
    application_start_date = models.DateField(verbose_name=_("Course Application Start Date"), default=timezone.now)
    application_end_date = models.DateField(verbose_name=_("Course Application End Date"), default=timezone.now)
    event_start_date = models.DateField(verbose_name=_("Event Start Date"), default=timezone.now)
    event_end_date = models.DateField(verbose_name=_("Event End Date"), default=timezone.now)
    update_accommodation_end_date = models.DateField(verbose_name=_("Accommodation Update End Date"),
                                                     default=timezone.now)
    docs_end_date = models.DateField(verbose_name=_("Docs End Date"), default=timezone.now)
    morning = models.FloatField(verbose_name=_("Total course hours at morning for one day"), default=3.0)
    afternoon = models.FloatField(verbose_name=_("Total course hours at afternoon for one day"), default=3.5)
    evening = models.FloatField(verbose_name=_("Total course hours at evening for one day"), default=2.5)
    needs_document = models.BooleanField(verbose_name=_("Site requires document"), default=True)

    class Meta:
        get_latest_by = 'year'

    def __str__(self):
        return f'{self.name}-{self.year}'
