from django.db import models

# m=['------','medicina', 'carto', 'moto']
# PROGRAMAS_UDENAR=[]
# for i,j in enumerate(m):
#     x=[i,j]
#     PROGRAMAS_UDENAR.append(x)


def atributos_de_formulario(opn, a_1, a_2):
    nombre = models.CharField(max_length=a_1)
    programa = models.CharField(max_length=a_1)
    grupo = models.CharField(max_length=2)
    calendario = models.DateField()

    # ------metodologias, conclusiones, descripcion y resultados-------------
    metodologia = models.TextField()
    conclusiones = models.TextField()
    descripcion_grafica = models.TextField()
    descripcion_tabla = models.TextField()
    resultados = models.TextField()
    referencias = programa = models.CharField(max_length=50)

    # ------------ medida 1---------------------
    mensurando_1 = models.FloatField()
    error_1 = models.FloatField()

    # ------------ medida 2---------------------
    mensurando_2 = models.FloatField()
    error_2 = models.FloatField()

    # ------------ medida 3---------------------
    chicuadrado_1 = models.FloatField()

    # ------------ medida 4---------------------
    mensurando_teo = models.FloatField()
    error_teo = models.FloatField()

    # # ------------ medida 5---------------------
    # mensurando_4 = models.FloatField()
    # error_4 = models.FloatField()

    # # ------------ medida 6---------------------
    # chicuadrado_2 = models.FloatField()

    # # ------------ medida 7---------------------
    # mensurando_5 = models.FloatField()
    # error_5 = models.FloatField()

    # ------------ imagenes---------------------

    if opn == "ajuste_de_curvas":

        return (
            nombre,
            programa,
            grupo,
            calendario,
            metodologia,
            conclusiones,
            resultados,
            descripcion_grafica,
            descripcion_tabla,
            chicuadrado_1,
            mensurando_1,
            error_1,
            mensurando_2,
            error_2,
            mensurando_teo,
            error_teo,
        )

    if opn == "errores_en_mediciones":

        return (
            nombre,
            programa,
            grupo,
            calendario,
            metodologia,
            conclusiones,
            # soporte,
            chicuadrado_1,
            mensurando_1,
            error_1,
            mensurando_2,
            error_2,
            mensurando_teo,
            error_teo,
        )


class DatosExperimentale(models.Model):

    user_name = models.CharField(
        max_length=50,
    )
    ngrafjpg = models.CharField(
        max_length=50,
    )

    x1 = models.FloatField()
    x2 = models.FloatField()
    x3 = models.FloatField()
    x4 = models.FloatField()
    x5 = models.FloatField()
    x6 = models.FloatField()
    x7 = models.FloatField()
    x8 = models.FloatField()
    #################
    y1 = models.FloatField()
    y2 = models.FloatField()
    y3 = models.FloatField()
    y4 = models.FloatField()
    y5 = models.FloatField()
    y6 = models.FloatField()
    y7 = models.FloatField()
    y8 = models.FloatField()
    #################
    dx1 = models.FloatField()
    dx2 = models.FloatField()
    dx3 = models.FloatField()
    dx4 = models.FloatField()
    dx5 = models.FloatField()
    dx6 = models.FloatField()
    dx7 = models.FloatField()
    dx8 = models.FloatField()
    #################
    dy1 = models.FloatField()
    dy2 = models.FloatField()
    dy3 = models.FloatField()
    dy4 = models.FloatField()
    dy5 = models.FloatField()
    dy6 = models.FloatField()
    dy7 = models.FloatField()
    dy8 = models.FloatField()

    nombre_grafico = models.CharField(max_length=15)

    titulo_grafico = models.CharField(max_length=50)

    eje_x = models.CharField(max_length=20)

    eje_y = models.CharField(max_length=20)

    pendiente = models.FloatField()

    intercepto = models.FloatField()


class AjusteDeCurva(models.Model):

    user_name = models.CharField(max_length=50)

    (
        nombre,
        programa,
        grupo,
        calendario,
        metodologia,
        conclusiones,
        resultados,
        descripcion_grafica,
        descripcion_tabla,
        chicuadrado_1,
        mensurando_1,
        error_1,
        mensurando_2,
        error_2,
        mensurando_teo,
        error_teo,
    ) = atributos_de_formulario("ajuste_de_curvas", 300, 1000)

    nota_pendiente = models.CharField(
        max_length=5,
    )
    nota_chisquare = models.CharField(
        max_length=5,
    )


class ReportePDF(models.Model):

    soporte = models.FileField(upload_to="files/ajuste_de_curvas")


class ErroresEnMedicione(models.Model):
    (
        nombre,
        programa,
        grupo,
        calendario,
        metodologia,
        conclusiones,
        # soporte,
        chicuadrado_1,
        mensurando_1,
        error_1,
        mensurando_2,
        error_2,
        mensurando_teo,
        error_teo,
    ) = atributos_de_formulario("errores_en_mediciones", 100, 500)
