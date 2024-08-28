from django.http import HttpResponse, HttpRequest
from django.template import Template, Context, loader
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .libmolina import *
from django.views.generic import View
from django.contrib.auth.decorators import login_required
import os
import os.path
from django.http import JsonResponse
from django.views.generic import CreateView
from django.contrib import messages


@login_required(login_url="/autenticacion/logear")
def hoja_de_vida(request):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    filename_pdf = "hojadevida_" + request.user.username + ".pdf"

    filepath = (
        BASE_DIR
        + "/"
        + "media"
        + "/"
        + "files"
        + "/"
        + "hojadevida"
        + "/"
        + filename_pdf
    )

    if os.path.isfile(filepath):
        contexto = {"true": True}
        return render(request, "contenido_HV.html", contexto)
    else:
        return render(request, "contenido_HV.html")


@login_required(login_url="/autenticacion/logear")
def Menu_HV(request):
    return render(request, "datos_HV.html")


@login_required(login_url="/autenticacion/logear")
def delete_regist(request, id_file):
    deletfile = TitulosAcademico.objects.get(id=id_file)
    deletfile.delete()
    return redirect("form_acad", 0)


@login_required(login_url="/autenticacion/logear")
def view_pdf_HV(request):
    if request.user.is_authenticated:
        software_list = [
            "Excel",
            "LibreOffice",
            "Microsoft Word",
            "Nitro Pro",
            "Gimp",
            "Wolfram Matemática",
            "Jupyter Notebook",
            "Google Colab",
            "GitHub",
            "Power BI",
            "Zoom",
            "Meet",
            "VS Code",
            "TexMaker",
            "SO Windows",
            "SO GNU/Linux",
            "Overleaf LaTeX",
            "Python",
            "C++",
            "C#",
            "HTML",
            "LaTeX",
            "JavaScript",
            "CSS",
            "SqLite",
            "MySql",
            "Django",
        ]
        # Defining the lists for each column
        nivBasic = [
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            30,
            30,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            20,
            20,
            80,
            80,
            100,
        ]
        nivInter = [
            10,
            5,
            5,
            80,
            50,
            40,
            50,
            20,
            0,
            0,
            80,
            100,
            50,
            100,
            100,
            100,
            80,
            80,
            30,
            10,
            70,
            100,
            0,
            0,
            0,
            0,
            40,
        ]
        nivAvanz = [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            50,
            0,
            30,
            30,
            50,
            0,
            0,
            0,
            0,
            0,
            5,
            0,
            0,
            0,
            0,
            0,
        ]
        numBasico = np.round((20 / 100) * np.array(nivBasic))
        numInterm = np.round((20 / 100) * np.array(nivInter))
        numaAvanz = np.round((20 / 100) * np.array(nivAvanz))
        herramientas_informaticas = []
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        for i, valor in enumerate(software_list):
            herramientas_informaticas.append(
                {
                    "Software": valor,
                    "Basico": int(numBasico[i]) * "|",
                    "Intermedio": int(numInterm[i]) * "|",
                    "Avanzado": int(numaAvanz[i]) * "|",
                    "Basic": nivBasic[i],
                    "Inter": nivInter[i],
                    "Avanz": nivAvanz[i],
                }
            )

        contexto = {
            "dir_img": BASE_DIR,
            "exp_laboral": [0],
            "herramientas_informaticas": herramientas_informaticas,
        }
        # response = render(request, "ver_pdf_hv.html", contexto)
        response = render_pdf_view("ver_pdf_hv.html", contexto)
        return response
    else:
        return redirect("logear")


@login_required(login_url="/autenticacion/logear")
def delete_experience(request, id_file):
    deletfile = ExperienciasLaborale.objects.get(id=id_file)
    deletfile.delete()
    return redirect("exp_laboral", 0)


@login_required(login_url="/autenticacion/logear")
def delete_prod_acad(request, id_file):
    deletfile = ProduccionAcademica.objects.get(id=id_file)
    deletfile.delete()
    return redirect("prod_acad", 0)


class formDatPersonView(HttpRequest):

    @login_required(login_url="/autenticacion/logear")
    def get_person_dat(request):
        var_estado = False
        datos_personales, fperfiluser = (
            DatosPersonalesForm(current_user=request.user.id),
            FotosPersonalesForm(),
        )
        try:
            name_doc_pdf = DatosPersonale.objects.get(nombre_usuario_id=request.user.id)

            if name_doc_pdf.fotocopia_documento.name != "":
                var_estado = True
            contexto = {
                "form": datos_personales,
                "fotoform": fperfiluser,
                "doc_name_PDF": name_doc_pdf,
                "estvar": var_estado,
            }
        except:
            contexto = {
                "form": datos_personales,
                "fotoform": fperfiluser,
                "doc_name_PDF": "#",
                "estvar": var_estado,
            }

        return render(request, "datos_personales.html", contexto)

    @login_required(login_url="/autenticacion/logear")
    def post_person_dat(request):
        var_estado = False
        (forms, fform) = (
            DatosPersonalesForm(),
            FotosPersonalesForm(),
        )

        try:

            name_doc_pdf = DatosPersonale.objects.get(nombre_usuario_id=request.user.id)

            if name_doc_pdf.fotocopia_documento.name != "":
                var_estado = True

            else:
                pass

            if request.method == "POST":

                forms = DatosPersonalesForm(
                    request.POST, request.FILES, instance=name_doc_pdf
                )

                if forms.is_valid():
                    forms.save()
                    return redirect("menuhv")
                else:

                    return render(
                        request,
                        "datos_personales.html",
                        {
                            "form": forms,
                            "fotoform": fform,
                            "doc_name_PDF": name_doc_pdf,
                            "estvar": var_estado,
                        },
                    )

            else:
                return render(request, "errores.html", {"form": forms.errors})
        except:
            if request.method == "POST":

                forms = DatosPersonalesForm(
                    request.POST, request.FILES, current_user=request.user.id
                )

                if forms.is_valid():
                    forms.save()
                    return redirect("menuhv")
                else:
                    return render(
                        request,
                        "datos_personales.html",
                        {
                            "form": forms,
                            "fotoform": fform,
                            "doc_name_PDF": "",
                            "estvar": var_estado,
                        },
                    )
            else:
                return render(request, "errores.html", {"form": forms.errors})

    @login_required(login_url="/autenticacion/logear")
    def post_person_phot(request):
        forms = FotosPersonalesForm()

        try:
            objdb = FotosPersonale.objects.get(nombre_usuario_id=request.user.id)
            if request.method == "POST":
                forms = FotosPersonalesForm(request.POST, request.FILES, instance=objdb)
                if forms.is_valid():
                    forms.save()
                    return redirect("get_datos")
                else:
                    return redirect("get_datos")
            else:
                return render(request, "errores.html", {"form": forms.errors})
        except:
            if request.method == "POST":
                forms = FotosPersonalesForm(
                    request.POST, request.FILES, current_user=request.user.id
                )
                if forms.is_valid():
                    forms.save()
                    return redirect("get_datos")
                else:
                    return redirect("get_datos")
            else:
                return render(request, "errores.html", {"form": forms.errors})

    @login_required(login_url="/autenticacion/logear")
    def phot_delete(request):
        deletfoto = FotosPersonale.objects.get(nombre_usuario_id=request.user.id)
        deletfoto.foto_perfil.delete()
        return redirect("get_datos")

    def file_delete(request):
        deletfile = DatosPersonale.objects.get(nombre_usuario_id=request.user.id)
        deletfile.fotocopia_documento.delete()
        return redirect("get_datos")

    @login_required(login_url="/autenticacion/logear")
    def get_imgfoto(_request):

        try:
            objdb = FotosPersonale.objects.get(nombre_usuario_id=_request.user.id)
            imgusuario = [
                {
                    "fotoperfil": objdb.foto_perfil.name,
                    "nameimg": objdb.foto_perfil.name.split("/")[3],
                }
            ]

            Context = {"img_usuario": imgusuario}

            return JsonResponse(Context)

        except:
            Context = {"img_usuario": []}
            return JsonResponse(Context)

    @login_required(login_url="/autenticacion/logear")
    def getjs_file(_request):
        try:
            dbfile = DatosPersonale.objects.get(nombre_usuario_id=_request.user.id)

            pathfile = [
                {
                    "filepdf": dbfile.fotocopia_documento.name.split("/")[3],
                }
            ]

            Context = {"file_usuario": pathfile}
            return JsonResponse(Context)
        except:
            Context = {"file_usuario": []}
            return JsonResponse(Context)


class FormacionAcademicaHV(View):

    def get(self, request, id_diploma):
        if request.user.is_authenticated:
            formacion_academica = FormularioTitulosAcademicos(
                current_user=request.user.id
            )
            queryset_dat = TitulosAcademico.objects.filter(
                nombre_usuario_id=request.user.id
            )

            contexto = {
                "form": formacion_academica,
                "querydat": queryset_dat,
            }
            return render(request, "registro_formacion_academica.html", contexto)

        else:
            return redirect("logear")

    def post(self, request, id_diploma=0):
        if request.user.is_authenticated:
            id_actual = id_diploma
            varcondicioonal = False
            formacion_academica = FormularioTitulosAcademicos()

            if request.method == "POST":
                try:
                    edit_soporte = TitulosAcademico.objects.get(id=id_diploma)
                    formacion_academica = FormularioTitulosAcademicos(
                        request.POST, request.FILES, instance=edit_soporte
                    )
                    id_diploma = 0
                except:
                    formacion_academica = FormularioTitulosAcademicos(
                        request.POST, request.FILES, current_user=request.user.id
                    )

                if formacion_academica.is_valid():
                    formacion_academica.save()
                    queryset_dat = TitulosAcademico.objects.filter(
                        nombre_usuario_id=request.user.id
                    )
                    if id_diploma == 0:
                        return redirect("form_acad", id_diploma)

                    else:
                        contexto = {
                            "form": formacion_academica,
                            "querydat": queryset_dat,
                        }
                        return render(
                            request, "registro_formacion_academica.html", contexto
                        )
                else:
                    varcondicioonal = True
                    contexto = {
                        "form": formacion_academica,
                        "errform": varcondicioonal,
                        "id_actual": id_actual,
                    }
                    return render(
                        request, "registro_formacion_academica.html", contexto
                    )
            else:
                return render(
                    request, "errores.html", {"form": formacion_academica.errors}
                )
        else:
            return redirect("logear")


class ExperienciaLaboralHV(View):

    def get(self, request, id_explab):
        if request.user.is_authenticated:
            expe_laboral = FormExperienciaLaboral(current_user=request.user.id)
            queryset_dat = ExperienciasLaborale.objects.filter(
                nombre_usuario_id=request.user.id
            )

            contexto = {
                "form": expe_laboral,
                "querydat": queryset_dat,
            }
            return render(request, "registro_exp_laboral.html", contexto)

        else:
            return redirect("logear")

    def post(self, request, id_explab=0):
        if request.user.is_authenticated:
            id_actual = id_explab
            varcond = False
            expe_laboral = FormExperienciaLaboral()

            if request.method == "POST":
                try:
                    edit_soporte = ExperienciasLaborale.objects.get(id=id_explab)
                    expe_laboral = FormExperienciaLaboral(
                        request.POST, request.FILES, instance=edit_soporte
                    )
                    id_explab = 0
                    # print(request.FILES["soportes_experincias_laborales"])
                except:
                    expe_laboral = FormExperienciaLaboral(
                        request.POST, request.FILES, current_user=request.user.id
                    )

                if expe_laboral.is_valid():
                    expe_laboral.save()
                    queryset_dat = ExperienciasLaborale.objects.filter(
                        nombre_usuario_id=request.user.id
                    )
                    if id_explab == 0:
                        return redirect("exp_laboral", id_explab)

                    else:
                        contexto = {
                            "form": expe_laboral,
                            "querydat": queryset_dat,
                        }
                        return render(request, "registro_exp_laboral.html", contexto)
                else:
                    varcond = True
                    contexto = {
                        "form": expe_laboral,
                        "errform": varcond,
                        "id_actual": id_actual,
                    }
                    return render(request, "registro_exp_laboral.html", contexto)
            else:
                return render(request, "errores.html", {"form": expe_laboral.errors})
        else:
            return redirect("logear")


class ProduccionAcademicaHV(View):

    def get(self, request, id_pracad):
        if request.user.is_authenticated:
            expe_laboral = FormularioProduccionAcademica(current_user=request.user.id)
            queryset_dat = ProduccionAcademica.objects.filter(
                nombre_usuario_id=request.user.id
            )

            contexto = {
                "form": expe_laboral,
                "querydat": queryset_dat,
            }
            return render(request, "produccion_academica.html", contexto)

        else:
            return redirect("logear")

    def post(self, request, id_pracad=0):
        if request.user.is_authenticated:
            id_actual = id_pracad
            varcond = False
            expe_laboral = FormularioProduccionAcademica()

            if request.method == "POST":
                try:
                    edit_soporte = ProduccionAcademica.objects.get(id=id_pracad)
                    expe_laboral = FormularioProduccionAcademica(
                        request.POST, request.FILES, instance=edit_soporte
                    )
                    id_pracad = 0
                    # print(request.FILES["soportes_experincias_laborales"])
                except:
                    expe_laboral = FormularioProduccionAcademica(
                        request.POST, request.FILES, current_user=request.user.id
                    )

                if expe_laboral.is_valid():
                    expe_laboral.save()
                    queryset_dat = ProduccionAcademica.objects.filter(
                        nombre_usuario_id=request.user.id
                    )
                    if id_pracad == 0:
                        return redirect("prod_acad", id_pracad)

                    else:
                        contexto = {
                            "form": expe_laboral,
                            "querydat": queryset_dat,
                        }
                        return render(request, "produccion_academica.html", contexto)
                else:
                    varcond = True
                    contexto = {
                        "form": expe_laboral,
                        "errform": varcond,
                        "id_actual": id_actual,
                    }
                    return render(request, "produccion_academica.html", contexto)
            else:
                return render(request, "errores.html", {"form": expe_laboral.errors})
        else:
            return redirect("logear")


class ParticipacionCientificaHV(View):

    def get(self, request, id_pcient=0):
        if request.user.is_authenticated:
            expe_laboral = FormularioParticipacionCientifica(
                current_user=request.user.id
            )
            queryset_dat = ParticipacionCientifica.objects.filter(
                nombre_usuario_id=request.user.id
            )

            contexto = {
                "form": expe_laboral,
                "querydat": queryset_dat,
            }
            return render(request, "participacion_cientifica.html", contexto)

        else:
            return redirect("logear")

    def post(self, request, id_pcient=0):
        if request.user.is_authenticated:
            id_actual = id_pcient
            varcond = False
            expe_laboral = FormularioParticipacionCientifica()

            if request.method == "POST":
                try:
                    edit_soporte = ParticipacionCientifica.objects.get(id=id_pcient)
                    expe_laboral = FormularioParticipacionCientifica(
                        request.POST, request.FILES, instance=edit_soporte
                    )
                    id_pcient = 0
                except:
                    expe_laboral = FormularioParticipacionCientifica(
                        request.POST, request.FILES, current_user=request.user.id
                    )

                if expe_laboral.is_valid():
                    expe_laboral.save()
                    queryset_dat = ParticipacionCientifica.objects.filter(
                        nombre_usuario_id=request.user.id
                    )
                    if id_pcient == 0:
                        return redirect("prod_acad", id_pcient)

                    else:
                        contexto = {
                            "form": expe_laboral,
                            "querydat": queryset_dat,
                        }
                        return render(
                            request, "participacion_cientifica.html", contexto
                        )
                else:
                    varcond = True
                    contexto = {
                        "form": expe_laboral,
                        "errform": varcond,
                        "id_actual": id_actual,
                    }
                    return render(request, "participacion_cientifica.html", contexto)
            else:
                return render(request, "errores.html", {"form": expe_laboral.errors})
        else:
            return redirect("logear")
