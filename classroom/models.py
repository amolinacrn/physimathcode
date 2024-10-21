from django.db import models
from django.contrib.auth.models import User


class FotosPersonale(models.Model):
    nombre_usuario = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE
    )
    foto_perfil = models.ImageField(upload_to="files/img/foto", blank=True, null=True)


class DatosPersonale(models.Model):
    nombre_usuario = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE
    )
    documento_identificacion = models.CharField(max_length=50, blank=False, null=False)
    numero_identificacion = models.CharField(max_length=20, blank=False, null=False)
    fecha_expedicion_documento = models.DateField(blank=False, null=False)
    ciudad_expedicion_documento = models.CharField(
        max_length=20, blank=False, null=False
    )
    primer_nombre = models.CharField(max_length=20, blank=False, null=False)
    segundo_nombre = models.CharField(max_length=20, blank=False, null=False)
    primer_apellido = models.CharField(max_length=20, blank=False, null=False)
    segundo_apellido = models.CharField(max_length=20, blank=False, null=False)
    genero_sexual = models.CharField(max_length=15, blank=False, null=False)
    grupo_sanguineo = models.CharField(max_length=15, blank=False, null=False)
    estado_civil = models.CharField(max_length=15, blank=False, null=False)
    pais_origen = models.CharField(max_length=15, blank=False, null=False)
    departamento_origen = models.CharField(max_length=20, blank=False, null=False)
    ciudad_nacimiento = models.CharField(max_length=20, blank=False, null=False)
    nacionalidad = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    ciudad_residencia = models.CharField(max_length=20, blank=False, null=False)
    direccion_residencia = models.CharField(max_length=50, blank=True, null=True)
    telefono_celular = models.CharField(max_length=10, blank=False, null=False)
    correo_electronico = models.EmailField(max_length=50, blank=False, null=False)
    libreta_militar = models.CharField(max_length=15, blank=True, null=True)
    distrito_militar = models.CharField(max_length=5, blank=True, null=True)
    cuenta_github = models.URLField(blank=True, null=True)
    fotocopia_documento = models.FileField(
        upload_to="files/docs/documentid", blank=False, null=False
    )
    perfil_profesional = models.TextField(max_length=1500, blank=True, null=True)


class TitulosAcademico(models.Model):
    nombre_usuario = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE
    )
    grado_academico = models.CharField(max_length=80, blank=False, null=False)
    titulo_obtenido = models.CharField(max_length=80, blank=False, null=False)
    institucion_universitaria = models.CharField(max_length=80, blank=False, null=False)
    programa_academico = models.CharField(max_length=80, blank=False, null=False)
    periodos_aprobados = models.CharField(max_length=2, blank=True, null=True)
    numero_semestres_programa = models.CharField(max_length=2, blank=True, null=True)
    graudado_universitario = models.CharField(max_length=3, blank=False, null=False)
    titulo_disertacion = models.CharField(max_length=200, blank=True, null=True)
    fecha_finalizacion = models.DateField(blank=False, null=False)
    numero_targeta_profesional = models.CharField(max_length=20, blank=True, null=True)
    pais_titulo = models.CharField(max_length=20, blank=True, null=True)
    departamento_titulo = models.CharField(max_length=20, blank=False, null=False)
    ciudad_titulo = models.CharField(max_length=50, blank=False, null=False)
    diploma_titulo = models.FileField(
        upload_to="files/docs/diplomas", blank=False, null=False
    )


class ExperienciasLaborale(models.Model):
    nombre_usuario = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE
    )
    tipo_empresa = models.CharField(max_length=80, blank=False, null=False)
    nombre_empresa = models.CharField(max_length=80, blank=False, null=False)
    cargo = models.CharField(max_length=80, blank=False, null=False)
    tipo_contrato = models.CharField(max_length=80, blank=True, null=True)
    departamento_contrato = models.CharField(max_length=20, blank=True, null=True)
    ciudad_contrato = models.CharField(max_length=50, blank=False, null=False)
    pais_contrato = models.CharField(max_length=20, blank=True, null=True)
    contacto_empresa = models.CharField(max_length=20, blank=True, null=True)
    correo_electronico_empresa = models.EmailField(
        max_length=50, blank=False, null=False
    )
    dependencia = models.CharField(max_length=80, blank=True, null=True)
    direccion_empresa = models.CharField(max_length=50, blank=False, null=False)
    fecha_inicio = models.DateField(blank=True, null=False)
    fecha_fin = models.DateField(blank=True, null=False)
    soportes_experincias_laborales = models.FileField(
        upload_to="files/docs/experiencia", blank=False, null=False
    )


class ProduccionAcademica(models.Model):
    nombre_usuario = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE
    )
    autores_trabajo = models.CharField(max_length=200, blank=False, null=False)
    nombre_trabajo = models.CharField(max_length=300, blank=False, null=False)
    pais_publicacion = models.CharField(max_length=50, blank=False, null=False)
    fecha_publicacion = models.DateField(blank=False, null=False)
    nombre_revista = models.CharField(max_length=100, blank=False, null=False)
    area_concentracion = models.CharField(max_length=150, blank=True, null=False)
    linea_pesquisa = models.CharField(max_length=150, blank=True, null=True)
    doi_link_publicacion = models.URLField(max_length=100, blank=False, null=False)


class ParticipacionCientifica(models.Model):
    nombre_usuario = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE
    )
    nombre_evento_cientifico = models.CharField(max_length=200, blank=False, null=False)
    tipo_evento = models.CharField(max_length=150, blank=False, null=False)
    institucion_evento = models.CharField(max_length=100, blank=False, null=False)
    ciudad_evento = models.CharField(max_length=50, blank=False, null=False)
    departamento_evento = models.CharField(max_length=50, blank=True, null=True)
    pais_evento = models.CharField(max_length=50, blank=False, null=False)
    fecha_inicio_evento = models.DateField(blank=False, null=False)
    fecha_fin_evento = models.DateField(blank=False, null=False)
    modalidad_evento = models.CharField(max_length=30, blank=False, null=False)
    soportes_eventos_cientificos = models.FileField(
        upload_to="files/docs/eventos", blank=False, null=False
    )


class IdiomaExtrangero(models.Model):
    nombre_usuario = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE
    )
    tipo_idioma = models.CharField(max_length=30, blank=False, null=False)
    domimio_conversacional = models.CharField(max_length=30, blank=False, null=False)
    dominio_lectura = models.CharField(max_length=30, blank=False, null=False)
    dominio_escritura = models.CharField(max_length=30, blank=False, null=False)
    nevel_certificado = models.CharField(max_length=5, blank=False, null=False)
    institucion_expedicion_certificado = models.CharField(
        max_length=80, blank=False, null=False
    )
    fecha_obtecion_certificado = models.DateField(blank=False, null=False)
    pais_obtencion_certificado = models.CharField(
        max_length=50, blank=False, null=False
    )
    departamento_obtencion_certificado = models.CharField(
        max_length=50, blank=False, null=False
    )
    ciudad_obtencion_certificado = models.CharField(
        max_length=50, blank=False, null=False
    )
    soporte_certificado_idioma = models.FileField(
        upload_to="files/docs/diploidiomas", blank=False, null=False
    )
