from django.db import models
from django.contrib.auth.models import AbstractUser
from ..base import ModelBase


class UserBase(ModelBase, AbstractUser):
    address = models.CharField(max_length=999, blank=True, unique=False)
    note = models.CharField(max_length=2500, blank=True)
    cellPhone = models.CharField(max_length=13, blank=True)

    class Meta:
        abstract = True
