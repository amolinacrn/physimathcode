from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from .models import AjusteDeCurva_fisilab2
from .forms import *


def similitud_texto(texto):
    var = "imagenes/" + texto
    return


def fisi_lab_dos(request):
    return render(request, "contenido_fislab2.html")


######################  ajuste de curvas ######################


def ajuste_curvas_fisilab2(request):
    form = LabAjusteCurvasForm_fisilab2()
    contexto = {"form": form}
    return render(request, "ajuste_de_curvas_2.html", contexto)


def enviar_datos_fisilab2(request):

    form = LabAjusteCurvasForm_fisilab2()

    if request.method == "POST":
        form = LabAjusteCurvasForm_fisilab2(request.POST, request.FILES)

    if form.is_valid():
        # vartext = request.POST["soporte"]
        # request.POST = request.POST.copy()
        # request.POST["soporte"] = similitud_texto(vartext)
        # form = AjusteDeCurva(request.POST)

        form.save()
    else:
        return render(request, "errores_2.html", {"form": form.errors})

    contexto = {"form": form}

    return render(request, "envio_exitoso_2.html", contexto)


###################### fin ajuste de curvas ######################


def errores_mediciones_fisilab2(request):
    form = ErrorEnMedicionesForm_fisilab2()
    contexto = {"form": form}
    return render(request, "errores_en_mediciones_2.html", contexto)


# def analizar_datos(request):
#     lista_datos = AjusteDeCurva.objects.all()

#     milista = []
#     for i in lista_datos:
#         milista.append(i.nombre)
#     # for o in milista:
#     #     eliminar=LabAjusteCurvas.objects.get(id=o)
#     #     eliminar.delete()
#     # print(milista)

#     fdata = open("notas_informes.txt", "w", encoding="utf-8")

#     try:
#         for i in milista:
#             fdata.write(i + "\n")
#     finally:
#         fdata.close()

#     contexto = {"lista": milista}

#     return render(request, "index.html", contexto)
