from django.urls import path
from .views import *


urlpatterns = [
    path("", VRegistro.as_view(), name="autenticacion"),
    path("cerrar_sesion", cerrar_sesion, name="cerrar_sesion"),
    path("logear", logear, name="logear"),
    path("PerUser", PermisosDocentesView.as_view(), name="PerUser"),
]
