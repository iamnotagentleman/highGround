from django.db import models
from django.utils import timezone
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
