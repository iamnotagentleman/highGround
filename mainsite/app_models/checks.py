from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from mainsite.app_models.base import ModelBase
from mainsite.app_models.courses import Course

class Check(ModelBase):
    course = models.ForeignKey(Course, verbose_name=_("Course of Check"), on_delete=models.CASCADE)
    start_check = models.DateTimeField(verbose_name=_("Event Start Time"), default=timezone.now)
    end_check = models.DateTimeField(verbose_name=_("Event End Time"), default=timezone.now)

    def __str__(self):
        return f"{self.course.name}-{self.course.site}-{self.start_check}"