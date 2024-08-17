from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .libmolina import *
from django.views.generic import View
from django.contrib.auth.decorators import login_required
import os, requests
from django.conf import settings
import os.path
from reportlab.pdfgen import canvas
from os import remove

from django_tex.shortcuts import render_to_pdf, compile_template_to_pdf


# varialbe global de datos get

matriz_datos_post = np.zeros((4, 8))

######################  ajuste de curvas ######################


def comprobar_existencia_archivos(rqst_user):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    filename_pdf = "informe_" + rqst_user.user.username + ".pdf"

    filepath = (
        BASE_DIR
        + "/"
        + "media"
        + "/"
        + "files"
        + "/"
        + "ajuste_de_curvas"
        + "/"
        + filename_pdf
    )

    if os.path.isfile(filepath):
        return True
    else:
        return False


def fun_aux_files(rqst):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    filnampdf = "informe_" + rqst.user.username + ".pdf"

    fpath = (
        BASE_DIR
        + "/"
        + "media"
        + "/"
        + "files"
        + "/"
        + "ajuste_de_curvas"
        + "/"
        + filnampdf
    )

    return fpath, filnampdf


@login_required(login_url="/autenticacion/logear")
def delete_file_pdf(request):
    filepath, _ = fun_aux_files(request)

    if os.path.isfile(filepath):
        remove(filepath)
        return render(request, "contenido_fisilab1.html")

    else:
        return render(request, "contenido_fisilab1.html")


@login_required(login_url="/autenticacion/logear")
def fisi_lab_uno(request):

    filepath, filename_pdf = fun_aux_files(request)

    if os.path.isfile(filepath):
        contexto = {"true": True, "filename": filename_pdf}
        return render(request, "contenido_fisilab1.html", contexto)
    else:
        return render(request, "contenido_fisilab1.html")


@login_required(login_url="/autenticacion/logear")
def evaluar_informes(request):

    filepath, filename_pdf = fun_aux_files(request)

    if os.path.isfile(filepath):
        contexto = {"true": True, "filename": filename_pdf}
        return render(request, "ver_todos_los_informes.html", contexto)
    else:
        return render(request, "ver_todos_los_informes.html")


# email = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Email"}))


class AnalisisDeDatos(View):

    def get(self, request):

        if request.user.is_authenticated:
            datosform = DatosExperimentalesForms()
            cpbr = comprobar_existencia_archivos(request)
            print(cpbr)
            contexto = {"datosform": datosform, "sifile": cpbr}
            return render(request, "recoleccion_datos.html", contexto)
        else:
            return redirect("logear")

    def post(self, request):

        if request.user.is_authenticated:

            datosform = DatosExperimentalesForms()

            if request.method == "POST":
                datosform = DatosExperimentalesForms(request.POST)

            if datosform.is_valid():

                xx = []
                yy = []
                dxx = []
                dyy = []

                for xi in ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]:
                    xx.append(request.POST[xi])

                for yi in ["y1", "y2", "y3", "y4", "y5", "y6", "y7", "y8"]:
                    yy.append(request.POST[yi])

                for dxi in ["dx1", "dx2", "dx3", "dx4", "dx5", "dx6", "dx7", "dx8"]:
                    dxx.append(request.POST[dxi])

                for dyi in ["dy1", "dy2", "dy3", "dy4", "dy5", "dy6", "dy7", "dy8"]:
                    dyy.append(request.POST[dyi])

                mygraf = request.POST["nombre_grafico"]
                pndt = float(request.POST["pendiente"])
                intrc = float(request.POST["intercepto"])
                label_eje_x = request.POST["eje_x"]
                label_eje_y = request.POST["eje_y"]
                label_titulo_grafico = request.POST["titulo_grafico"]

                global matriz_datos_post

                matriz_datos_post = {"x": xx, "y": yy, "dx": dxx, "dy": dyy}

                nombre_grafica_jpg = datos_plot(
                    np.transpose([xx, yy, dxx, dyy]),
                    mygraf,
                    label_eje_x,
                    label_eje_y,
                    pndt,
                    intrc,
                    label_titulo_grafico,
                )

                update_database(request.user.username, "user_name", DatosExperimentale)

                datosform.save()

                actualizar_username = DatosExperimentale.objects.get(user_name="o")
                actualizar_username.user_name = request.user.username
                actualizar_username.save()

                grafx_jpg = DatosExperimentale.objects.get(ngrafjpg="o")
                grafx_jpg.ngrafjpg = nombre_grafica_jpg
                grafx_jpg.save()

                return redirect("ajuste_de_curvas")
            else:
                return render(request, "errores.html", {"form": datosform.errors})

        else:
            return redirect("logear")


class LabAjusteDeCurvas(View):

    def get(self, request):

        if request.user.is_authenticated:

            form = LabAjusteCurvasForm()

            cpbr = comprobar_existencia_archivos(request)

            contexto = {
                "sifile": cpbr,
                "form": form,
                "matriz_datos_post": matriz_datos_post,
                "nombre_grafica_jpg": request_database_LabajstCurvas(
                    request.user.username, "user_name", "ngrafjpg"
                )[0],
            }

            return render(request, "ajuste_de_curvas.html", contexto)
        else:
            return redirect("logear")

    def post(self, request):

        if request.user.is_authenticated:

            nota_pendte = 0
            nota_chiQ = 0

            form = LabAjusteCurvasForm()

            if request.method == "POST":

                # , request.FILES)
                form = LabAjusteCurvasForm(request.POST)

            if form.is_valid():

                update_database(request.user.username, "user_name", AjusteDeCurva)

                form.save()

                mis_forms_par = [
                    "mensurando_teo",
                    "error_teo",
                    "mensurando_1",
                    "error_1",
                    "mensurando_2",
                    "error_2",
                    "chicuadrado_1",
                ]

                vpar = []

                for ifms in mis_forms_par:
                    vpar.append(float(request.POST[ifms]))

                nota_pendte = AjusteDeCurva.objects.get(nota_pendiente="o")
                nota_pendte.nota_pendiente = tratamiento_errores(
                    vpar[0], vpar[1], vpar[2], vpar[3]
                )
                nota_pendte.save()

                nota_chiQ = AjusteDeCurva.objects.get(nota_chisquare="o")
                nota_chiQ.nota_chisquare = chi_sqre(vpar[6])
                nota_chiQ.save()

                update_username = AjusteDeCurva.objects.get(user_name="o")
                update_username.user_name = request.user.username
                update_username.save()

            else:
                return render(request, "errores.html", {"form": form.errors})
            # render_pdf_view("htmlpdf.html", contexto) #//convertir un atml a un pdf
            return redirect("viewLaTex")
            # return render(request, "index.html", {"form": form})

        else:
            return redirect("logear")


class GenerandoReporte(View):

    def get(self, request):

        if request.user.is_authenticated:

            forms = ReportePDFForms()

            dats = [
                "nombre",
                "programa",
                "grupo",
                "calendario",
                "metodologia",
                "conclusiones",
                "nota_pendiente",
                "nota_chisquare",
            ]

            datsx = request_database_notas(request.user.username, dats, AjusteDeCurva)
            figx = request_database_LabajstCurvas(
                request.user.username, "user_name", "ngrafjpg"
            )[0]

            calific = (float(datsx[6]) + float(datsx[7])) * 5 / 2

            contexto = {
                "nombres": datsx[0].split(";"),
                "Programa": datsx[1],
                "grupo": datsx[2],
                "calendario": datsx[3],
                "metodologia": datsx[4],
                "conclusiones": datsx[5],
                "grafplot": figx,
                "Nota": calific,
                "forms": forms,
            }

            return render(request, "envioexitoso.html", contexto)

        else:

            return redirect("logear")

    def post(self, request):

        if request.user.is_authenticated:

            forms = ReportePDFForms()

            if request.method == "POST":

                forms = ReportePDFForms(request.POST, request.FILES)

            if forms.is_valid():

                forms.save()

                return redirect("fisilab1")
            else:
                return render(request, "errores.html", {"form": forms.errors})
        else:
            return redirect("logear")


def viewLaTex(request):

    if request.user.is_authenticated:

        template_name = "ajcvar.tex"

        forms = ReportePDFForms()

        dats = [
            "nombre",
            "programa",
            "grupo",
            "calendario",
            "metodologia",
            "conclusiones",
            "nota_pendiente",
            "nota_chisquare",
            "resultados",
            "descripcion_grafica",
            "descripcion_tabla",
        ]

        datsx = request_database_notas(request.user.username, dats, AjusteDeCurva)

        figx = request_database_LabajstCurvas(
            request.user.username, "user_name", "ngrafjpg"
        )[0]

        calific = (float(datsx[6]) + float(datsx[7])) * 5 / 2

        nam_eje = ["eje_x", "eje_y"]

        name_ejes = request_database_notas(
            request.user.username, nam_eje, DatosExperimentale
        )

        mxr = [
            ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"],
            ["y1", "y2", "y3", "y4", "y5", "y6", "y7", "y8"],
            ["dx1", "dx2", "dx3", "dx4", "dx5", "dx6", "dx7", "dx8"],
            ["dy1", "dy2", "dy3", "dy4", "dy5", "dy6", "dy7", "dy8"],
        ]

        mxdat = []

        for ix in mxr:
            dat = request_database_notas(request.user.username, ix, DatosExperimentale)
            mxdat.append(dat)

        mx = np.transpose(np.array(mxdat))
        contr = np.arange(len(mx[:, 0]))

        contexto = {
            "nombres": datsx[0].split(";"),
            "Programa": datsx[1],
            "grupo": datsx[2],
            "calendario": datsx[3],
            "metodologia": datsx[4],
            "conclusiones": datsx[5],
            "resultados": datsx[8],
            "descripcion_grafica": datsx[9],
            "descripcion_tabla": datsx[10],
            "grafplot": figx,
            "nota": calific,
            "mxdat": mx,
            "contr": contr,
            "name_ejes": name_ejes,
        }

        name_pdf = "informe_" + request.user.username + ".pdf"

        rqst = render_to_pdf(request, template_name, contexto, filename=name_pdf)

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        filepath = (
            BASE_DIR
            + "/"
            + "media"
            + "/"
            + "files"
            + "/"
            + "ajuste_de_curvas"
            + "/"
            + name_pdf
        )

        with open(filepath, "wb") as xfile:
            xfile.write(rqst.content)

        return redirect("fisilab1")

    else:
        return redirect("logear")


def ver_informePDF(request):

    if request.user.is_authenticated:

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        filename = "informe_" + request.user.username + ".pdf"

        filepath = (
            BASE_DIR
            + "/"
            + "media"
            + "/"
            + "files"
            + "/"
            + "ajuste_de_curvas"
            + "/"
            + filename
        )

        path = open(filepath, mode="rb")

        response["Content-Disposition"] = f"attachment; filename={filename}"

        response = HttpResponse(path, content_type="application/pdf")

        return response

    else:
        return redirect("logear")


# def errores_mediciones(request):
#     form = ErrorEnMedicionesForm()
#     contexto = {"form": form}
#     return render(request, "errores_en_mediciones.html", contexto)
