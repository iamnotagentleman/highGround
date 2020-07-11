from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords


class ModelBase(models.Model):
    created = models.DateTimeField(default=timezone.now(), editable=False, blank=True)
    modified = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    class Meta:
        abstract = True
        get_latest_by = 'created'
