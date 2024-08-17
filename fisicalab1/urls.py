from django.urls import path
from fisicalab1 import views
from .views import *

urlpatterns = [
    path("", views.fisi_lab_uno, name="fisilab1"),
    path("analisys", AnalisisDeDatos.as_view(), name="analisys"),
    path("ajuste_de_curvas", LabAjusteDeCurvas.as_view(), name="ajuste_de_curvas"),
    path("verPDF", views.ver_informePDF, name="verPDF"),
    path("viewLaTex", views.viewLaTex, name="viewLaTex"),
    path("generando_reporte", GenerandoReporte.as_view(), name="generando_reporte"),
    path("eval_inf", views.evaluar_informes, name="eval_inf"),
    path("delete_file", views.delete_file_pdf, name="delete_file"),
]
