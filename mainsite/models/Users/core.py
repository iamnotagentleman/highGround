from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import datetime_safe
from django.utils.translation import ugettext_lazy as _
from ..base import ModelBase
from django_countries.data import COUNTRIES
from django_countries.fields import CountryField

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


class User(ModelBase):
    address = models.CharField(verbose_name=_("Home Address"), max_length=999, blank=True, unique=False)
    note = models.CharField(verbose_name=_("Note about User"), max_length=2500, blank=True)
    phone_number = models.CharField(verbose_name=_("Mobil phone number"), max_length=13, blank=True)
    birth_date = models.DateField(verbose_name=_("Birth Date"), default=datetime_safe.date(2000, 1, 1))
    job = models.CharField(verbose_name=_("Job"), max_length=40, )
    gender = models.CharField(choices={'E': _("Male"), 'K': _("Female")}.items(), verbose_name=_("Gender"),max_length=1)
    country = CountryField(verbose_name=_("Nationality"), choices=COUNTRIES, default='UK')
    current_education = models.CharField(verbose_name=_("Current Education"), choices=EDUCATIONS, max_length=4)
    organization = models.CharField(verbose_name=_("Organization"), max_length=200, null=True, blank=True)
    experience = models.CharField(verbose_name=_("Work Experience"), max_length=1000, null=True, blank=True)
    emergency_contact_information = models.CharField(max_length=5000, verbose_name=_("Emergency Contact Information"),
                                                     null=True, blank=True)
    profile_photo = models.ImageField(upload_to=user_directory_path, verbose_name=_("Profile Picture"),
                                     help_text=_("Maximum 5 MB file is allowed."))

    class Meta:
        abstract = True
        app_label = 'mainsite'