import numpy as np
from django import forms

from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


# lista_datos=mi_class_models.objects.all()
# milista=[]
# for i in lista_datos:
#     milista.append(i.nombre)

# for o in milista:
#     eliminar=mi_class_models.objects.get(id=o)
#     eliminar.delete()


def definir_atributos_formulario_fisilab2(opn):

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
        max_length=2, label="Grupo:", widget=forms.Select(choices=GRUPOS_LABORATORIO)
    )

    programa = forms.CharField(
        max_length=100,
        label="Programa: ",
        widget=forms.Select(choices=PROGRAMAS_UDENAR),
    )

    nombre = forms.CharField(
        max_length=100,
        label="Nombre:",
        widget=forms.Textarea(attrs={"rows": 1, "cols": 1}),
    )

    calendario = forms.DateField(
        label="Fecha:",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"],
    )

    # ------------ medida 1---------------------
    sustentacion_1 = forms.CharField(
        max_length=590,
        label="Sustentacion:",
        widget=forms.Textarea(attrs={"rows": 4, "cols": 1}),
    )

    mensurando_1 = forms.FloatField(
        label=" "
    )  # max_length=20,label=' ',widget=forms.Textarea(attrs={"rows":1, "cols":20}))
    error_1 = forms.FloatField(
        label=" "
    )  # max_length=20,label=' ',widget=forms.Textarea(attrs={"rows":1, "cols":20}))

    # ------------ medida 2---------------------

    sustentacion_2 = forms.CharField(
        max_length=590,
        label="Sustentacion:",
        widget=forms.Textarea(attrs={"rows": 4, "cols": 1}),
    )

    mensurando_2 = forms.FloatField(
        label=" "
    )  # (max_length=20,label=' ',widget=forms.Textarea(attrs={"rows":1, "cols":20}))
    error_2 = forms.FloatField(
        label=" "
    )  # (max_length=20,label=' ',widget=forms.Textarea(attrs={"rows":1, "cols":20}))

    # ------------ medida 3---------------------
    sustentacion_3 = forms.CharField(
        max_length=590,
        label="¿Qué concluye?:",
        widget=forms.Textarea(attrs={"rows": 4, "cols": 1}),
    )

    mensurando_3 = forms.FloatField(
        label=" "
    )  # (max_length=20,label=' ',widget=forms.Textarea(attrs={"rows":1, "cols":20}))

    # ------------ medida 4---------------------

    sustentacion_4 = forms.CharField(
        max_length=590,
        label="Sustentacion:",
        widget=forms.Textarea(attrs={"rows": 4, "cols": 1}),
    )

    mensurando_4 = forms.FloatField(
        label=" "
    )  # (max_length=20,label=' ',widget=forms.Textarea(attrs={"rows":1, "cols":20}))
    error_4 = forms.FloatField(
        label=" "
    )  # forms.CharField(max_length=20,label=' ',widget=forms.Textarea(attrs={"rows":1, "cols":20}))

    # ------------ medida 5---------------------
    sustentacion_5 = forms.CharField(
        max_length=590,
        label="Sustentacion:",
        widget=forms.Textarea(attrs={"rows": 4, "cols": 1}),
    )

    mensurando_5 = forms.FloatField(
        label=" "
    )  # forms.CharField(max_length=20,label=' ',widget=forms.Textarea(attrs={"rows":1, "cols":20}))
    error_5 = forms.FloatField(
        label=" "
    )  # forms.CharField(max_length=20,label=' ',widget=forms.Textarea(attrs={"rows":1, "cols":20}))

    # ------------ medida 6---------------------

    sustentacion_6 = forms.CharField(
        max_length=590,
        label="¿Qué concluye?:",
        widget=forms.Textarea(attrs={"rows": 4, "cols": 1}),
    )

    mensurando_6 = forms.FloatField(
        label=" "
    )  # forms.CharField(max_length=20,label=' ',widget=forms.Textarea(attrs={"rows":1, "cols":20}))

    # ------------ medida 7---------------------

    sustentacion_7 = forms.CharField(
        max_length=590,
        label="Sustentacion:",
        widget=forms.Textarea(attrs={"rows": 4, "cols": 1}),
    )

    mensurando_7 = forms.FloatField(
        label=" "
    )  # forms.CharField(max_length=20,label=' ',widget=forms.Textarea(attrs={"rows":1, "cols":20}))
    error_7 = forms.FloatField(
        label=" "
    )  # forms.CharField(max_length=20,label=' ',widget=forms.Textarea(attrs={"rows":1, "cols":20}))

    soporte = forms.FileField(label="")

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


class LabAjusteCurvasForm_fisilab2(forms.ModelForm):

    class Meta:
        model = AjusteDeCurva_fisilab2
        fields = "__all__"

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
    ) = definir_atributos_formulario_fisilab2("ajuste_de_curvas")


class ErrorEnMedicionesForm_fisilab2(forms.ModelForm):

    class Meta:
        model = ErroresEnMediciones_fisilab2
        fields = "__all__"

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
    ) = definir_atributos_formulario_fisilab2("errores_en_mediciones")

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
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
