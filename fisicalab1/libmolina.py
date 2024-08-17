import random
import matplotlib.ticker as mticker
from .models import *
import numpy as np
from iminuit import Minuit
from matplotlib import pyplot as plt
import matplotlib
from .utilspdf import render_pdf_view

matplotlib.rcParams["text.usetex"] = True
from probfit import Chi2Regression, linear


def similitud_texto(texto):
    var = "imagenes/" + texto
    return


"""

    # "nombre_grafica_jpg": "file://"
    # + os.path.join(
    #     settings.BASE_DIR,
    #     "static",
    #     "img",
    #     "fisilab1",
    #     "ajuste_de_curvas",
    # ),



    # for i in list_result:
    # request.POST = request.POST.copy()
    # request.POST["ngrafjpg"] = myModelobject.ngrafjpg
    # model_form = LabAjusteCurvasForm(request.POST, instance=myModelobject)

    # request.POST = request.POST.copy()
    # request.POST["soporte"] = similitud_texto(vartext)
    # form = AjusteDeCurva(request.POST)


    lista_datos = DatosExperimentale.objects.all()
    milista = []

    for i, dats in enumerate(lista_datos):
        x = dats + ".x" + str(i)
        milista.append(dats.x1)
    # for o in milista:
    #     eliminar=LabAjusteCurvas.objects.get(id=o)
    #     eliminar.delete()
    print(milista)

    fdata = open("notas_informes.txt", "w", encoding="utf-8")

    try:
        for i in milista:
            fdata.write(i + "\n")
    finally:
        fdata.close()

    contexto = {"lista": milista}
"""


def update_database(reqst_user_username, user_name, MiClase):
    # ------- inicio ----------#

    # esto es para eliminar usuarios repetidos, es decir la base datos
    # debe contener unicamente un usuario por id

    users_names_list = []
    id_objets_list = []

    idd_objets = [uo for uo in MiClase.objects.values("id")]

    for ix in list(idd_objets):
        id_objets_list.append((list(ix.values())[0]))

    list_nombre_usuario = [ri for ri in MiClase.objects.values(user_name)]

    for iu in list(list_nombre_usuario):
        users_names_list.append((list(iu.values())[0]))

    for cont_id, nom_user in enumerate(users_names_list):

        if reqst_user_username == nom_user:

            obj_delete = MiClase.objects.get(id=id_objets_list[cont_id])

            obj_delete.delete()

    # iko = np.where(np.array(users_names_list) == reqst_user_username)

    # if len(np.array(users_names_list)[iko]) == 0:
    #     return False
    # else:
    #     return True

    # ------- fin ----------#


def request_database_notas(usrname, dataset, Modelo):

    user_name = []

    for iu in list([ri for ri in Modelo.objects.values("user_name")]):
        user_name.append((list(iu.values())[0]))

    dats_cot = []

    for dats in dataset:
        list_dats = []
        listdats = [ri for ri in Modelo.objects.values(dats)]
        for iu in list(listdats):
            list_dats.append((list(iu.values())[0]))

        pendte = np.array(list_dats)[np.array(user_name) == usrname]

        dats_cot.append(pendte[0])

    return dats_cot


def request_database_LabajstCurvas(reqst, string_var, grafix):

    users_names = []

    lstgraf = []

    list_name_user = [ri for ri in DatosExperimentale.objects.values(string_var)]

    lista_grafx = [ri for ri in DatosExperimentale.objects.values(grafix)]

    for iu in list(list_name_user):
        users_names.append((list(iu.values())[0]))

    for iu in list(lista_grafx):
        lstgraf.append((list(iu.values())[0]))

    # for io, emlobj in enumerate(users_names):
    #     if reqst == emlobj:
    #         lista_contexto = lstgraf[io]

    return np.array(lstgraf)[np.array(users_names) == reqst]


def request_database_viewLaTex(reqst, strg):

    mis_forms_nombres = [
        "nombre",
        "programa",
        "grupo",
        "calendario",
        "metodologia",
        "conclusiones",
        "ngrafjpg",
    ]

    lista_contexto = []

    users_names = []

    nombre_de_usuario = AjusteDeCurva.objects.values(strg)

    list_name_user = [ri for ri in nombre_de_usuario]

    for iu in list(list_name_user):
        users_names.append((list(iu.values())[0]))

    for im in mis_forms_nombres:
        object_dats = AjusteDeCurva.objects.values(im)
        list_datos = [ri for ri in object_dats]
        info_base_datos = []

        for iu in list(list_datos):
            info_base_datos.append((list(iu.values())[0]))

        for io, emlobj in enumerate(users_names):
            if reqst.user.username == emlobj:
                lista_contexto.append(info_base_datos[io])

    template_name = "ajcvar.tex"
    context = {
        "nombre": lista_contexto[0],
        "programa": lista_contexto[1],
        "grupo": lista_contexto[2],
        "calendario": lista_contexto[3],
        "metodologia": lista_contexto[4],
        "conclusiones": lista_contexto[5],
        "figura": lista_contexto[6],
    }

    return (reqst, template_name, context)


def chi_sqre(csq):
    if csq >= 0.5 and csq <= 2.5:
        return 1
    else:
        return 0.8


def tratamiento_errores(u, du, z, dz):
    eu_mas = u + abs(du)
    eu_men = u - abs(du)
    ez_mas = z + abs(dz)
    ez_men = z - abs(dz)

    ## criterio de igualdad ##

    if (
        (eu_men <= z and eu_mas >= z)
        or (z > eu_mas and ez_men <= eu_mas)
        or (z < eu_men and ez_mas >= eu_men)
    ):
        return 1
        ###fin criterio de igualdad ###

    elif (z > eu_mas and ez_men > eu_mas) or (z < eu_men and ez_mas < eu_men):
        errp = abs((z - u) / u) * 100

        if errp >= 0 and errp <= 2:
            return 1
        elif errp > 2 and errp <= 5:
            return (-1.0 / 3.0) * errp + 5.0 / 3.0
        else:
            return 0
    else:
        return 0


def funcion_lineal(x, m, b):
    return b + x * m


def datos_plot(
    xdat,
    nomgr="graphics",
    label_x=r"eje $x$",
    label_y=r"eje $y$",
    rx=1,
    bx=1,
    titulo_grafico="Square Number",
):

    Nvar = 2
    ngraf = nomgr.replace(" ", "")
    fig, ax = plt.subplots()
    aleatorio = str(random.random()).split(".")[1]
    nombre_grafica = ngraf + "_" + str(aleatorio) + ".png"
    dir_graf = "static/img/fisilab1/ajuste_de_curvas/" + nombre_grafica

    x = np.array(xdat[:, 0], dtype=float)
    y = np.array(xdat[:, 1], dtype=float)
    dy = np.array(xdat[:, 3], dtype=float)
    Npoints = len(x)

    x2r = Chi2Regression(linear, x, y, dy)

    ajt = Minuit(x2r, m=rx, c=bx)
    ajt.migrad()

    m_fit = ajt.values["m"]
    c_fit = ajt.values["c"]
    m_err = ajt.errors["m"]
    c_err = ajt.errors["c"]

    frt = r"${:.5f}$"
    dat_m = frt.format(m_fit) + r" $\pm$ " + frt.format(m_err)
    dat_c = frt.format(c_fit) + r" $\pm$ " + frt.format(c_err)

    Ndof_calc = Npoints - Nvar  # grados de libertad
    Chi2_fit = ajt.fval  # the chi2 value
    fitQty = Chi2_fit / Ndof_calc

    # x2r.draw(ajt, ax=ax)
    # ax.grid()

    plt.errorbar(x, y, dy, fmt="ok", label="hola")
    plt.plot(x, funcion_lineal(x, m_fit, c_fit))

    format = r"${:.5f}$"
    stats = (
        r"$\chi^2 / \nu $ =" + format.format(fitQty) + "\n\n"
        r"$\textup{p}_0$ = " + dat_c + "\n\n"
        r"$\textup{p}_1$ = " + dat_m
    )

    ax.legend(
        [stats],
        loc="best",
        fontsize="large",
        handlelength=0,
    )

    # plt.legend(fontsize="large")

    plt.title(titulo_grafico, fontsize=20)
    plt.tick_params(axis="both", labelsize=15)

    plt.xlabel(label_x, fontsize=20)
    plt.ylabel(label_y, fontsize=20)

    crd_y = np.max(y) - np.min(y)
    crd_x = np.max(x) - np.min(x)

    plt.xlim([np.min(x) - 0.1 * crd_x, np.max(x) + 0.1 * crd_x])
    plt.ylim([np.min(y) - 0.2 * crd_y, np.max(y) + 0.2 * crd_y])

    xlist = np.linspace(np.min(x) - 0.1 * crd_x, np.max(x) + 0.1 * crd_x, 8)
    ax.xaxis.set_major_locator(mticker.FixedLocator(xlist))
    ax.ticklabel_format(style="sci", axis="x", scilimits=(0, 0))

    ylist = np.linspace(np.min(y) - 0.2 * crd_y, np.max(y) + 0.2 * crd_y, 8)

    ax.yaxis.set_major_locator(mticker.FixedLocator(ylist))
    ax.ticklabel_format(style="sci", axis="y", scilimits=(0, 0))

    bbox = dict(boxstyle="round", fc="#FFFFFF", ec="lightgray")

    plt.tight_layout()
    plt.savefig(dir_graf, format="png", bbox_inches="tight")

    return nombre_grafica
