from django.db import models
from django.utils import timezone, datetime_safe
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django_countries.data import COUNTRIES
from django_countries.fields import CountryField
from simple_history.models import HistoricalRecords
import uuid


class ModelBase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(default=timezone.now, editable=False, blank=True)
    modified = models.DateTimeField(auto_now=True)
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True
        get_latest_by = 'created'
        app_label = 'mainsite'


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



EDUCATIONS = [
    ("mid", _("Middle School")),
    ("high", _("High School")),
    ("univ", _("University")),
    ("mas", _("Master")),
    ("doc", _("Doctorate")),
    ("none", _("Not a Student")),
]


def user_directory_path(instance, filename):
    return f'{instance.user.id}/{filename}'


class User(ModelBase, AbstractUser):
    address = models.CharField(verbose_name=_("Home Address"), max_length=999, blank=True, unique=False)
    note = models.CharField(verbose_name=_("Note about User"), max_length=2500, blank=True)
    phone_number = models.CharField(verbose_name=_("Mobil phone number"), max_length=13, blank=True)
    birth_date = models.DateField(verbose_name=_("Birth Date"), default=datetime_safe.date(2000, 1, 1))
    job = models.CharField(verbose_name=_("Job"), max_length=40, )
    gender = models.CharField(choices={'E': _("Male"), 'K': _("Female")}.items(), verbose_name=_("Gender"),max_length=1,
                              blank=True)
    country = CountryField(verbose_name=_("Nationality"), choices=COUNTRIES, default='UK')
    current_education = models.CharField(verbose_name=_("Current Education"), choices=EDUCATIONS, max_length=4)
    organization = models.CharField(verbose_name=_("Organization"), max_length=200, null=True, blank=True)
    experience = models.CharField(verbose_name=_("Work Experience"), max_length=1000, null=True, blank=True)
    emergency_contact_information = models.CharField(max_length=5000, verbose_name=_("Emergency Contact Information"),
                                                     null=True, blank=True)
    profile_photo = models.ImageField(upload_to=user_directory_path, verbose_name=_("Profile Picture"),
                                     help_text=_("Maximum 5 MB file is allowed."))

    class Meta:
        app_label = 'mainsite'

    def __str__(self):
        return f"{self.email}-{self.phone_number}"