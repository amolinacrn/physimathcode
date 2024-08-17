tipo_documento = [
    None,
    "Cédula de ciudadanía (CC)",
    "Targeta de identidad (TI)",
    "Registro civil (RC)",
    "Cédula de extranjería (CE)",
    "Carné de identidad (CI)",
    "Documento nacional de identidad (DNI)",
]

TIPO_DOCUMENTO = []
for i in tipo_documento:
    if i == None:
        document = [None, "Seleccione..."]
    else:
        document = [i, i]
    TIPO_DOCUMENTO.append(document)

tipo_sexo = [None, "Masculino", "Femenino"]

TIPO_SEXO = []
for i in tipo_sexo:
    if i == None:
        sexx = [None, "Seleccione..."]
    else:
        sexx = [i, i]
    TIPO_SEXO.append(sexx)

tipo_sangre = [None, "O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-", "no informa"]

TIPO_SANGRE = []
for i in tipo_sangre:
    if i == None:
        sangre = [None, "Seleccione..."]
    else:
        sangre = [i, i]
    TIPO_SANGRE.append(sangre)

tipo_estado_civil = [
    None,
    "Madre soltera",
    "Religioso(a)",
    "Casado(a)",
    "Divorciado(a)",
    "Soltero(a)",
    "Union libre",
    "Viudo(a)",
]

ESTADO_CIVIL_TIPO = []
for i in tipo_estado_civil:
    if i == None:
        civil = [None, "Seleccione..."]
    else:
        civil = [i, i]
    ESTADO_CIVIL_TIPO.append(civil)

lib_militar = [
    None,
    "Primera clase",
    "Segunda clase",
]

LIBRETA_MILITAR_CLASE = []
for i in lib_militar:
    if i == None:
        militar = [None, "Seleccione..."]
    else:
        militar = [i, i]
    LIBRETA_MILITAR_CLASE.append(militar)

NACIONALIDAD_CLASE = []
for i in [None, "Estrangero", "Colombiano"]:
    if i == None:
        nacion = [None, "Seleccione..."]
    else:
        nacion = [i, i]
    NACIONALIDAD_CLASE.append(nacion)

grado_profesional = [
    None,
    "Diplomado",
    "Cursos y seminarios",
    "Educación básica y media",
    "Formación técnica",
    "Formación tecnológica",
    "Título Profesional",
    "Título de especialización",
    "Título de Maestría o magíster",
    "Título de doctorado o phd",
    "Posdoctorado",
]

GRADO_ACADEMICO_PROFESIONAL = []
for i in grado_profesional:
    if i == None:
        grado = [None, "Seleccione..."]
    else:
        grado = [i, i]
    GRADO_ACADEMICO_PROFESIONAL.append(grado)

egresado_con_distincion = [None, "Si", "No"]

GRADUADO_CON_DISTINCION = []
for i in egresado_con_distincion:
    if i == None:
        grad_ditincion = [None, "Seleccione..."]
    else:
        grad_ditincion = [i, i]
    GRADUADO_CON_DISTINCION.append(grad_ditincion)

esgraduado_unieversitario = [None, "Si", "No"]

ES_GRADUADO_UNIVERSITARIO = []
for i in esgraduado_unieversitario:
    if i == None:
        grad_univ = [None, "Seleccione..."]
    else:
        grad_univ = [i, i]
    ES_GRADUADO_UNIVERSITARIO.append(grad_univ)

modalidad_empresa_laboral = [None, "Privada", "Publica", "Independiente"]

TIPO_DE_EMPRESA_LABORAL = []
for i in modalidad_empresa_laboral:
    if i == None:
        tipo_empresa = [None, "Seleccione..."]
    else:
        tipo_empresa = [i, i]
    TIPO_DE_EMPRESA_LABORAL.append(tipo_empresa)

tipo_contrato_con_empresa_laboral = [
    None,
    "Término fijo",
    "Término indefinido",
    "Obra o labor",
    "Orden de prestación de servicios",
    "Contrato de aprendisaje",
    "Contrato ocasional de trabajo",
]

TITPO_CONTRATO_EMPRESA_LABORAL = []
for i in tipo_contrato_con_empresa_laboral:
    if i == None:
        tipo_contrato_empresa = [None, "Seleccione..."]
    else:
        tipo_contrato_empresa = [i, i]
    TITPO_CONTRATO_EMPRESA_LABORAL.append(tipo_contrato_empresa)


tipo_del_evento_cientifico = [
    None,
    "Conferencias",
    "Congresos",
    "Simposios",
    "Seminarios",
    "Talleres",
    "Foros",
    "Coloquios",
    "Jornadas",
    "Mesas redondas",
    "Presentaciones de pósteres",
    "Webinars",
    "Cursos cortos",
    "Reuniones anuales",
    "Cumbres",
    "Hackatones",
    "Paneles de discusión",
    "Clínicas científicas",
    "Feria de ciencias",
    "Escuelas de verano",
]
TIPO_EVENTO_CIENTIFICO = []
for i in tipo_del_evento_cientifico:
    if i == None:
        tipo_evento = [None, "Seleccione..."]
    else:
        tipo_evento = [i, i]
    TIPO_EVENTO_CIENTIFICO.append(tipo_evento)


rol_del_evento_cientifico = [
    None,
    "Conferencista principal",
    "Ponente",
    "Moderador",
    "Panelista",
    "Miembro del comité organizador",
    "Revisor científico",
    "Expositor de póster",
    "Asistente",
    "Miembro del comité científico",
    "Evaluador de trabajos",
    "Presentador de taller",
    "Miembro del comité técnico",
    "Responsable de logística",
    "Moderador de mesa redonda",
    "Responsable de relaciones públicas",
    "Miembro del equipo de comunicación",
    "Traductor o intérprete",
    "Colaborador en redes sociales",
    "Instructor de tutorial",
    "Participante en discusión",
]
MODALIDAD_EVENTO_CIENTIFICO = []
for i in rol_del_evento_cientifico:
    if i == None:
        rol_evento = [None, "Seleccione..."]
    else:
        rol_evento = [i, i]
    MODALIDAD_EVENTO_CIENTIFICO.append(rol_evento)


nive_suficiencia_idioma = [
    None,
    "insuficiente(-)",
    "Insuficiente",
    "Insuficiente(+)",
    "regular(-)",
    "regular",
    "Regular(+)",
    "Basico(-)",
    "Basico",
    "Basico(+)",
    "Intermedio(-)",
    "Intermedio",
    "Intermedio(+)",
    "Avanzado(-)",
    "Avanzado",
    "Avanzado(+)",
    "Excelente(-)",
    "Excelente",
    "Excelente(+)",
    "Experto",
]
NIVEL_SUFICIENCIA_INGLES = []
for i in nive_suficiencia_idioma:
    if i == None:
        idioma = [None, "Seleccione..."]
    else:
        idioma = [i, i]
    NIVEL_SUFICIENCIA_INGLES.append(idioma)


nivel_de_ingles = [None, "A1", "A2", "B1", "B2", "C1", "C2"]
NIVEL_INGLES_CERTIFICADO = []
for i in nivel_de_ingles:
    if i == None:
        nivel_idioma = [None, "Seleccione..."]
    else:
        nivel_idioma = [i, i]
    NIVEL_INGLES_CERTIFICADO.append(nivel_idioma)
