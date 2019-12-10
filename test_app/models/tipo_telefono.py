from django.db import models
from django.utils import timezone
from .utils import AutoDateTimeField


class TipoTelefono(models.Model):
    nombre = models.CharField(max_length=15)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)
    