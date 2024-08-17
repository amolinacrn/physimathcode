import numpy as np
from django import forms
from .models import *


# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column


# lista_datos=mi_class_forms.objects.all(label="")
# milista=[]
# for i in lista_datos:
#     milista.append(i.nombre)

# for o in milista:
#     eliminar=mi_class_forms.objects.get(id=o)
#     eliminar.delete(label="")


def definir_atributos_formulario(opn):

    m = [None, "medicina", "carto", "moto", "Ingenieria agroforestal"]
    mx = [None, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    GRUPOS_LABORATORIO = []
    for i in mx:
        if i == None:
            x = [None, "-----"]
        else:
            x = [i, i]
        GRUPOS_LABORATORIO.append(x)

    PROGRAMAS_UDENAR = []
    for i in m:
        if i == None:
            x = [None, "-------- "]
        else:
            x = [i, i]
        PROGRAMAS_UDENAR.append(x)

    grupo = forms.CharField(
        max_length=2,
        label="Grupo:",
        required=False,
        widget=forms.Select(choices=GRUPOS_LABORATORIO, attrs={"required": "True"}),
    )

    programa = forms.CharField(
        max_length=100,
        label="Programa: ",
        required=False,
        widget=forms.Select(choices=PROGRAMAS_UDENAR, attrs={"required": "True"}),
    )

    nombre = forms.CharField(
        max_length=300,
        label="Nombre:",
        required=False,
        widget=forms.TextInput(
            attrs={
                # "placeholder": "Nombres ",
                "required": "True",
            }
        ),
        # widget=forms.Textarea(attrs={"rows": 1, "cols": 50}),
    )

    calendario = forms.DateField(
        label="Fecha:",
        required=False,
        widget=forms.DateInput(
            format="%Y-%m-%d",
            attrs={
                "type": "date",
                "required": "True",
            },
        ),
        input_formats=["%Y-%m-%d"],
    )

    # -------------  ----------------------------

    metodologia = forms.CharField(
        max_length=2000,
        label="",
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 16,
                "cols": 1,
                # "placeholder": "Nombres ",
                "required": "True",
            }
        ),
    )

    descripcion_grafica = forms.CharField(
        max_length=500,
        label="Descripción de la gráfica:",
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 5,
                "cols": 1,
                # "placeholder": "Nombres ",
                "required": "True",
            }
        ),
    )

    descripcion_tabla = forms.CharField(
        max_length=500,
        label="Descripción de la tabla:",
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 7,
                "cols": 1,
                # "placeholder": "Nombres ",
                "required": "True",
            }
        ),
    )

    resultados = forms.CharField(
        max_length=2000,
        label="",
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 16,
                "cols": 1,
                # "placeholder": "Nombres ",
                "required": "True",
            }
        ),
    )

    conclusiones = forms.CharField(
        max_length=2000,
        label="",
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 16,
                "cols": 1,
                # "placeholder": "Nombres ",
                "required": "True",
            }
        ),
    )

    # ------------ medida 1---------------------

    mensurando_1 = forms.FloatField(
        label=" ",
        required=False,
        widget=forms.NumberInput(attrs={"required": "True"}),
    )
    # max_length=20,label=' ',widget=forms.Textarea(attrs={"rows":1, "cols":20}))
    error_1 = forms.FloatField(
        label=" ",
        required=False,
        widget=forms.NumberInput(attrs={"required": "True"}),
    )  # max_length=20,label=' ',widget=forms.Textarea(attrs={"rows":1, "cols":20}))

    # ------------ medida 2---------------------

    mensurando_2 = forms.FloatField(
        label=" ",
        required=False,
        widget=forms.NumberInput(attrs={"required": "True"}),
    )  # (max_length=20,label=' ',widget=forms.Textarea(attrs={"rows":1, "cols":20}))
    error_2 = forms.FloatField(
        label=" ",
        required=False,
        widget=forms.NumberInput(attrs={"required": "True"}),
    )  # (max_length=20,label=' ',widget=forms.Textarea(attrs={"rows":1, "cols":20}))

    # ------------ medida 3---------------------

    mensurando_teo = forms.FloatField(
        label=" ",
        required=False,
        widget=forms.NumberInput(attrs={"required": "True"}),
    )  # (max_length=20,label=' ',widget=forms.Textarea(attrs={"rows":1, "cols":20}))
    error_teo = forms.FloatField(
        label=" ",
        required=False,
        widget=forms.NumberInput(attrs={"required": "True"}),
    )  # (max_length=20,label=' ',widget=forms.Textarea(attrs={"rows":1, "cols":20}))

    # ------------ medida 4---------------------

    chicuadrado_1 = forms.FloatField(
        label=" ",
        required=False,
        widget=forms.NumberInput(attrs={"required": "True"}),
    )  # (max_length=20,label=' ',widget=forms.Textarea(attrs={"rows":1, "cols":20}))

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


class LabAjusteCurvasForm(forms.ModelForm):

    class Meta:
        model = AjusteDeCurva
        fields = "__all__"

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
    ) = definir_atributos_formulario("ajuste_de_curvas")

    user_name = forms.CharField(
        max_length=50,
        initial="o",
    )

    nota_pendiente = forms.CharField(
        max_length=5,
        initial="o",
    )
    nota_chisquare = forms.CharField(
        max_length=5,
        initial="o",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nota_pendiente"].disabled = True
        self.fields["nota_chisquare"].disabled = True
        self.fields["user_name"].disabled = True


# class NotasDeEstudiantesForm(forms.ModelForm):
#     class Meta:
#         model = NotasDeEstudiantes
#         fields = "__all__"

#     nombres_estudiates = forms.CharField(
#             max_length=50,
#             initial="o",
#         )
#     calificacion_lab = forms.CharField(
#         max_length=50,
#         initial="o",
#     )

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields["nombres_estudiates"].disabled = True
#         self.fields["calificacion_lab"].disabled = True

#         self.fields["nombres_estudiates"].initial = args[1][0]
#         self.fields["calificacion_lab"].initial = args[1][1]


class ErrorEnMedicionesForm(forms.ModelForm):

    class Meta:
        model = ErroresEnMedicione
        fields = "__all__"

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
    ) = definir_atributos_formulario("errores_en_mediciones")


class ReportePDFForms(forms.ModelForm):

    class Meta:
        model = ReportePDF
        fields = "__all__"

    soporte = forms.FileField(label="Cargar informe en formato pdf:")


class DatosExperimentalesForms(forms.ModelForm):

    class Meta:
        model = DatosExperimentale
        fields = "__all__"

    x1 = forms.FloatField(label="")
    x2 = forms.FloatField(label="")
    x3 = forms.FloatField(label="")
    x4 = forms.FloatField(label="")
    x5 = forms.FloatField(label="")
    x6 = forms.FloatField(label="")
    x7 = forms.FloatField(label="")
    x8 = forms.FloatField(label="")
    #################
    y1 = forms.FloatField(label="")
    y2 = forms.FloatField(label="")
    y3 = forms.FloatField(label="")
    y4 = forms.FloatField(label="")
    y5 = forms.FloatField(label="")
    y6 = forms.FloatField(label="")
    y7 = forms.FloatField(label="")
    y8 = forms.FloatField(label="")
    #################
    dx1 = forms.FloatField(label="")
    dx2 = forms.FloatField(label="")
    dx3 = forms.FloatField(label="")
    dx4 = forms.FloatField(label="")
    dx5 = forms.FloatField(label="")
    dx6 = forms.FloatField(label="")
    dx7 = forms.FloatField(label="")
    dx8 = forms.FloatField(label="")
    #################
    dy1 = forms.FloatField(label="")
    dy2 = forms.FloatField(label="")
    dy3 = forms.FloatField(label="")
    dy4 = forms.FloatField(label="")
    dy5 = forms.FloatField(label="")
    dy6 = forms.FloatField(label="")
    dy7 = forms.FloatField(label="")
    dy8 = forms.FloatField(label="")

    nombre_grafico = forms.CharField(max_length=15, label="Nombre del gráfico * :")

    titulo_grafico = forms.CharField(
        max_length=100, label="Título del gráfico :", initial="Título del gráfico"
    )

    eje_x = forms.CharField(max_length=50, label="Titulo eje $x$ *:")

    eje_y = forms.CharField(max_length=50, label="Titulo eje $y$ *:")

    pendiente = forms.FloatField(label="Pendiente :", initial=1)

    intercepto = forms.FloatField(label="Intercepto :", initial=1)

    ngrafjpg = forms.CharField(
        max_length=50,
        initial="o",
    )

    user_name = forms.CharField(
        max_length=50,
        initial="o",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["ngrafjpg"].disabled = True
        self.fields["user_name"].disabled = True

        # self.fields["ngrafjpg"].initial = "o"
        # self.fields["user_name"].initial = "o"  # args[1]
        # print(args)


# def __init__(self, *args, **kwargs):
#     super(label="").__init__(*args, **kwargs)
#     self.helper = FormHelper(label="")
#     self.helper.layout = Layout(
#         Row(
#             Column('nombre', css_class='form-group col-md-6 mb-0'),
#             Column('programa', css_class='form-group col-md-3 mb-0'),
#             Column('calendario', css_class='form-group col-md-2 mb-0'),
#              Column('grupo', css_class='form-group col-md-1 mb-0'),
#             css_class='form-row'
#         ),
#         #'contenido',

#     #     Row(
#     #     Column('city', css_class='form-group col-md-6 mb-0'),
#     #     Column('state', css_class='form-group col-md-4 mb-0'),
#     #     Column('zip_code', css_class='form-group col-md-2 mb-0'),
#     #     css_class='form-row'
#     # ),

#         # 'check_me_out',
#         # Submit('submit', 'Enviar')
#     )
