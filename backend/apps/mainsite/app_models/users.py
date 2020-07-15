from apps.mainsite.app_models.base import ModelBase
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django_countries.data import COUNTRIES
from django_countries.fields import CountryField
from django.utils import datetime_safe

EDUCATIONS = [
    ("mid", _("Middle School")),
    ("high", _("High School")),
    ("univ", _("University")),
    ("mas", _("Master")),
    ("doc", _("Doctorate")),
    ("none", _("Not a Student")),
]


def user_directory_path(instance, filename):
    return f'images/users/{instance.id}/{filename}'


class User(ModelBase, AbstractUser):
    'General UserModel'
    address = models.CharField(verbose_name=_("Home Address"), max_length=999, blank=True, unique=False)
    note = models.CharField(verbose_name=_("Note about User"), max_length=2500, blank=True)
    phone_number = models.CharField(verbose_name=_("Mobil phone number"), max_length=13, blank=True)
    birth_date = models.DateField(verbose_name=_("Birth Date"), default=datetime_safe.date(2000, 1, 1))
    job = models.CharField(verbose_name=_("Job"), max_length=60, )
    gender = models.CharField(choices={'M': _("Male"), 'F': _("Female")}.items(), verbose_name=_("Gender"),max_length=1,
                              blank=True)
    country = CountryField(verbose_name=_("Nationality"), choices=COUNTRIES, default='UK')
    current_education = models.CharField(verbose_name=_("Current Education"), choices=EDUCATIONS, max_length=4)
    organization = models.CharField(verbose_name=_("Organization"), max_length=200, null=True, blank=True)
    experience = models.CharField(verbose_name=_("Work Experience"), max_length=1000, null=True, blank=True)
    emergency_contact_information = models.CharField(max_length=5000, verbose_name=_("Emergency Contact Information"),
                                                     null=True, blank=True)
    profile_photo = models.ImageField(upload_to=user_directory_path, verbose_name=_("Profile Picture"),
                                     help_text=_("Maximum 5 MB file is allowed."), blank=True)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        app_label = 'mainsite'

    def __str__(self):
        return f"{self.email}-{self.phone_number}"
