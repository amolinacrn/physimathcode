from typing import Any
from django.db import models

# m=['------','medicina', 'carto', 'moto']
# PROGRAMAS_UDENAR=[]
# for i,j in enumerate(m):
#     x=[i,j]
#     PROGRAMAS_UDENAR.append(x)


def atributos_de_formulario_fisilab2(opn, a_1, a_2):
    nombre = models.CharField(max_length=a_1)
    programa = models.CharField(max_length=a_1)
    grupo = models.CharField(max_length=2)
    calendario = models.DateField()

    # ------------ medida 1---------------------
    mensurando_1 = models.FloatField()
    error_1 = models.FloatField()
    sustentacion_1 = models.CharField(max_length=a_2)

    # ------------ medida 2---------------------
    mensurando_2 = models.FloatField()
    error_2 = models.FloatField()
    sustentacion_2 = models.CharField(max_length=a_2)

    # ------------ medida 3---------------------
    mensurando_3 = models.FloatField()
    sustentacion_3 = models.CharField(max_length=a_2)

    # ------------ medida 4---------------------
    mensurando_4 = models.FloatField()
    error_4 = models.FloatField()
    sustentacion_4 = models.CharField(max_length=a_2)

    # ------------ medida 5---------------------
    mensurando_5 = models.FloatField()
    error_5 = models.FloatField()
    sustentacion_5 = models.CharField(max_length=a_2)

    # ------------ medida 6---------------------
    mensurando_6 = models.FloatField()
    sustentacion_6 = models.CharField(max_length=a_2)

    # ------------ medida 7---------------------
    mensurando_7 = models.FloatField()
    error_7 = models.FloatField()
    sustentacion_7 = models.CharField(max_length=a_2)

    # ------------ imagenes---------------------
    soporte = models.FileField(upload_to="files/" + opn)

    if opn == "ajuste_de_curvas":

        return (
            nombre,
            programa,
            grupo,
            calendario,
            mensurando_1,
            error_1,
            sustentacion_1,
            mensurando_2,
            error_2,
            sustentacion_2,
            mensurando_3,
            sustentacion_3,
            mensurando_4,
            error_4,
            sustentacion_4,
            mensurando_5,
            error_5,
            sustentacion_5,
            mensurando_6,
            sustentacion_6,
            mensurando_7,
            error_7,
            sustentacion_7,
            soporte,
        )

    if opn == "errores_en_mediciones":

        return (
            nombre,
            programa,
            grupo,
            calendario,
            mensurando_1,
            error_1,
            sustentacion_1,
            mensurando_2,
            error_2,
            sustentacion_2,
            mensurando_3,
            sustentacion_3,
            mensurando_4,
            error_4,
            sustentacion_4,
            mensurando_5,
            error_5,
            sustentacion_5,
            mensurando_6,
            sustentacion_6,
            mensurando_7,
            error_7,
            sustentacion_7,
            soporte,
        )


##----------Modelos de aqui hacia abajo---------###########


class AjusteDeCurva_fisilab2(models.Model):

    (
        nombre,
        programa,
        grupo,
        calendario,
        mensurando_1,
        error_1,
        sustentacion_1,
        mensurando_2,
        error_2,
        sustentacion_2,
        mensurando_3,
        sustentacion_3,
        mensurando_4,
        error_4,
        sustentacion_4,
        mensurando_5,
        error_5,
        sustentacion_5,
        mensurando_6,
        sustentacion_6,
        mensurando_7,
        error_7,
        sustentacion_7,
        soporte,
    ) = atributos_de_formulario_fisilab2("ajuste_de_curvas", 100, 500)


class ErroresEnMediciones_fisilab2(models.Model):
    (
        nombre,
        programa,
        grupo,
        calendario,
        mensurando_1,
        error_1,
        sustentacion_1,
        mensurando_2,
        error_2,
        sustentacion_2,
        mensurando_3,
        sustentacion_3,
        mensurando_4,
        error_4,
        sustentacion_4,
        mensurando_5,
        error_5,
        sustentacion_5,
        mensurando_6,
        sustentacion_6,
        mensurando_7,
        error_7,
        sustentacion_7,
        soporte,
    ) = atributos_de_formulario_fisilab2("errores_en_mediciones", 100, 500)
