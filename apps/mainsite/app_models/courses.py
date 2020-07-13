from django.db import models
from apps.mainsite.app_models.sites import Site
from apps.mainsite.app_models.base import ModelBase
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _


def get_sentinel_site():
    return Site.objects.get_or_create(name='deleted')[0]


class Course(ModelBase):
    site = models.ForeignKey(Site, verbose_name=_("Course Site"), on_delete=models.SET(get_sentinel_site))
    name = models.CharField(verbose_name=_("Course Name"), max_length=50, null=True, blank=False)
    description = models.CharField(verbose_name=_("Description of Course"), max_length=5000, null=True, blank=False)
    lecturer = models.ManyToManyField(get_user_model(),
                                       limit_choices_to={'is_staff': True},
                                       verbose_name=_("Lecturers of Course"),
                                       related_name='lecturer',
                                       blank=True)
    assistant = models.ManyToManyField(get_user_model(),
                                       limit_choices_to={'is_staff': True},
                                       verbose_name=_("Assistant of Lecturer"),
                                       related_name='assistant',
                                       blank=True)

    participant = models.ManyToManyField(get_user_model(),
                                          limit_choices_to={"is_staff": False},
                                          verbose_name=_("Participants Of Course"),
                                          related_name='participant',
                                          blank=True)

    def __str__(self):
        return f"{self.name}-{self.site}"
