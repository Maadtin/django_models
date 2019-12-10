from django.db import models
from .tipo_telefono import TipoTelefono
from django.contrib.auth.models import User

class Telefono(models.Model):
    tipo_telefono = models.ForeignKey(TipoTelefono, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    numero = models.CharField(max_length=15)