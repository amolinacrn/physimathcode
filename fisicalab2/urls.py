from django.urls import path
from fisicalab2 import views

urlpatterns = [
    path("", views.fisi_lab_dos, name="fisilab2"),
    path("ajuste_de_curvas", views.ajuste_curvas_fisilab2, name="ajuste_de_curvas_2"),
    path(
        "errores_en_mediciones",
        views.errores_mediciones_fisilab2,
        name="error_medicion_2",
    ),
    path("enviar_datos", views.enviar_datos_fisilab2, name="enviar_datos_2"),
]
