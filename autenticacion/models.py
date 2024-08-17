from django.db import models
from django.contrib.auth.models import User


class PermisosParaDocente(models.Model):
    permiso_docente = models.CharField(max_length=50)
    id_usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=50)
