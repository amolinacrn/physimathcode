import numpy as np
from django import forms
from .models import *
from .validator import MaxZiseFileValidator
from .validator import MaxZiseImageValidator
from django.contrib.auth.models import User
from .choises import *


class FotosPersonalesForm(forms.ModelForm):

    foto_perfil = forms.ImageField(
        label=" ",
        required=False,
        validators=[
            MaxZiseImageValidator(max_img_size=0.2),
        ],
    )

    class Meta:
        model = FotosPersonale
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        self.current_user = kwargs.pop("current_user", None)
        super().__init__(*args, **kwargs)
        self.fields["foto_perfil"].widget.attrs["class"] = "upload-img green"
        self.fields["nombre_usuario"].disabled = True
        self.fields["nombre_usuario"].initial = self.current_user


class DatosPersonalesForm(forms.ModelForm):

    class Meta:
        model = DatosPersonale
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        self.current_user = kwargs.pop("current_user", None)
        super().__init__(*args, **kwargs)

        # self.fields["fotocopia_documento"].widget.attrs["class"] = "fancy-file green"

        try:
            db_obj = DatosPersonale.objects.get(nombre_usuario_id=self.current_user)

            self.fields["documento_identificacion"].initial = (
                db_obj.documento_identificacion
            )

            self.fields["perfil_profesional"].initial = db_obj.perfil_profesional
            self.fields["cuenta_github"].initial = db_obj.cuenta_github
            self.fields["numero_identificacion"].initial = db_obj.numero_identificacion
            self.fields["fecha_expedicion_documento"].initial = (
                db_obj.fecha_expedicion_documento
            )
            self.fields["ciudad_expedicion_documento"].initial = (
                db_obj.ciudad_expedicion_documento
            )
            self.fields["primer_nombre"].initial = db_obj.primer_nombre
            self.fields["segundo_nombre"].initial = db_obj.segundo_nombre
            self.fields["primer_apellido"].initial = db_obj.primer_apellido
            self.fields["segundo_apellido"].initial = db_obj.segundo_apellido
            self.fields["genero_sexual"].initial = db_obj.genero_sexual
            self.fields["grupo_sanguineo"].initial = db_obj.grupo_sanguineo
            self.fields["estado_civil"].initial = db_obj.estado_civil
            self.fields["ciudad_nacimiento"].initial = db_obj.ciudad_nacimiento
            self.fields["fecha_nacimiento"].initial = db_obj.fecha_nacimiento
            self.fields["pais_origen"].initial = db_obj.pais_origen
            self.fields["nacionalidad"].initial = db_obj.nacionalidad
            self.fields["ciudad_residencia"].initial = db_obj.ciudad_residencia
            self.fields["departamento_origen"].initial = db_obj.departamento_origen
            self.fields["direccion_residencia"].initial = db_obj.direccion_residencia
            self.fields["telefono_celular"].initial = db_obj.telefono_celular
            self.fields["correo_electronico"].initial = db_obj.correo_electronico
            self.fields["libreta_militar"].initial = db_obj.libreta_militar
            self.fields["distrito_militar"].initial = db_obj.distrito_militar
            self.fields["fotocopia_documento"].initial = db_obj.fotocopia_documento
        except:
            self.fields["nombre_usuario"].disabled = True
            self.fields["nombre_usuario"].initial = self.current_user

    documento_identificacion = forms.CharField(
        max_length=50,
        label="<h7 style='color:red'>*</h7> Tipo Documento:",
        required=True,
        widget=forms.Select(choices=TIPO_DOCUMENTO),
    )

    numero_identificacion = forms.CharField(
        label="<h7 style='color:red'>*</h7> Número de documento:",
        required=True,
        widget=forms.NumberInput(),
    )

    fecha_expedicion_documento = forms.DateField(
        label="<h7 style='color:red'>*</h7> Fecha de expedicion:",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"],
    )

    ciudad_expedicion_documento = forms.CharField(
        max_length=20,
        label="<h7 style='color:red'>*</h7> Ciudad de expedición:",
        required=True,
    )

    primer_nombre = forms.CharField(
        max_length=20,
        label="<h7 style='color:red'>*</h7> Primer nombre:",
        required=True,
    )

    segundo_nombre = forms.CharField(
        max_length=20,
        label="<h7 style='color:red'>*</h7> Segundo nombre:",
        required=True,
    )

    primer_apellido = forms.CharField(
        max_length=20,
        label="<h7 style='color:red'>*</h7> Primer apellido:",
        required=True,
    )

    segundo_apellido = forms.CharField(
        max_length=20,
        label="<h7 style='color:red'>*</h7> Segundo apellido:",
        required=True,
    )

    genero_sexual = forms.CharField(
        max_length=15,
        label="<h7 style='color:red'>*</h7> Sexo biológico:",
        required=True,
        widget=forms.Select(choices=TIPO_SEXO),
    )

    grupo_sanguineo = forms.CharField(
        max_length=15,
        label="<h7 style='color:red'>*</h7> Grupo sanguineo:",
        required=True,
        widget=forms.Select(choices=TIPO_SANGRE),
    )

    estado_civil = forms.CharField(
        max_length=15,
        label="<h7 style='color:red'>*</h7> Estado civil:",
        required=True,
        widget=forms.Select(choices=ESTADO_CIVIL_TIPO),
    )

    ciudad_nacimiento = forms.CharField(
        max_length=20,
        label="<h7 style='color:red'>*</h7> Ciudad de nacimiento:",
        required=True,
    )

    fecha_nacimiento = forms.DateField(
        label="<h7 style='color:red'>*</h7> Fecha de nacimiento:",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"],
    )

    pais_origen = forms.CharField(
        max_length=20, label="<h7 style='color:red'>*</h7> País:", required=True
    )

    departamento_origen = forms.CharField(
        max_length=20, label="<h7 style='color:red'>*</h7> Departamento:", required=True
    )

    nacionalidad = forms.CharField(
        max_length=20,
        label="Nacionalidad:",
        required=True,
        widget=forms.Select(choices=NACIONALIDAD_CLASE),
    )

    ciudad_residencia = forms.CharField(
        max_length=20,
        label="<h7 style='color:red'>*</h7> Ciudad de residencia:",
        required=True,
    )

    direccion_residencia = forms.CharField(
        max_length=50, label="Dirección:", required=True
    )

    telefono_celular = forms.IntegerField(
        label="<h7 style='color:red'>*</h7> Celular:",
        required=True,
        widget=forms.NumberInput(),
    )

    correo_electronico = forms.EmailField(
        max_length=50,
        label="<h7 style='color:red'>*</h7> Correo electrónico:",
        required=True,
    )

    libreta_militar = forms.CharField(
        max_length=15,
        label="Libreta militar:",
        required=False,
        widget=forms.Select(choices=LIBRETA_MILITAR_CLASE),
    )

    distrito_militar = forms.CharField(
        max_length=5,
        label="Distrito militar:",
        required=True,
        widget=forms.NumberInput(),
    )

    cuenta_github = forms.URLField(
        max_length=50, label="Cuenta github:", required=False
    )

    fotocopia_documento = forms.FileField(
        label="<h7 style='color:red'>*</h7> Fotocopia Cédula (pdf):",
        required=True,
        widget=forms.FileInput(),
        validators=[MaxZiseFileValidator(max_file_size=0.2)],
    )

    perfil_profesional = forms.CharField(
        max_length=1500,
        label="Perfil profesional:",
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 10,
                "cols": 1,
            }
        ),
    )


class FormularioTitulosAcademicos(forms.ModelForm):

    class Meta:
        model = TitulosAcademico
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        self.current_user = kwargs.pop("current_user", None)
        super().__init__(*args, **kwargs)
        self.fields["nombre_usuario"].disabled = True
        self.fields["nombre_usuario"].initial = self.current_user

    grado_academico = forms.CharField(
        max_length=80,
        label="<h7 style='color:red'>*</h7> Titulación académica:",
        required=True,
        widget=forms.Select(choices=GRADO_ACADEMICO_PROFESIONAL),
    )
    titulo_obtenido = forms.CharField(
        max_length=100,
        label="<h7 style='color:red'>*</h7> Título obtenido:",
        required=True,
    )
    institucion_universitaria = forms.CharField(
        max_length=80,
        label="<h7 style='color:red'>*</h7> Institución universitaria:",
        required=True,
    )
    programa_academico = forms.CharField(
        max_length=100,
        label="<h7 style='color:red'>*</h7> Programa académico:",
        required=True,
    )
    periodos_aprobados = forms.CharField(
        max_length=2,
        label="Periodos aprobados:",
        required=False,
    )
    numero_semestres_programa = forms.CharField(
        max_length=2,
        label="Número de semestres:",
        required=False,
    )
    graudado_universitario = forms.CharField(
        max_length=80,
        label="<h7 style='color:red'>*</h7> Graduado:",
        required=True,
        widget=forms.Select(choices=ES_GRADUADO_UNIVERSITARIO),
    )
    titulo_disertacion = forms.CharField(
        max_length=200,
        label="Título trabajo de grado:",
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 2,
                "cols": 1,
            }
        ),
    )
    fecha_finalizacion = forms.DateField(
        label="<h7 style='color:red'>*</h7> Fecha de finalización:",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"],
    )
    numero_targeta_profesional = forms.CharField(
        max_length=20,
        label="Número tarjeta profesional:",
        required=False,
    )
    pais_titulo = forms.CharField(max_length=20, label="País:", required=False)
    departamento_titulo = forms.CharField(
        max_length=20, label="<h7 style='color:red'>*</h7> Departamento:", required=True
    )
    ciudad_titulo = forms.CharField(
        max_length=50, label="<h7 style='color:red'>*</h7> Ciudad:", required=True
    )
    diploma_titulo = forms.FileField(
        label="<h7 style='color:red'>*</h7> Soporte titulación  (<b>.pdf</b>):",
        required=True,
        widget=forms.FileInput(),
        validators=[
            MaxZiseFileValidator(max_file_size=0.5),
        ],
    )


class FormExperienciaLaboral(forms.ModelForm):

    class Meta:
        model = ExperienciasLaborale
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        self.current_user = kwargs.pop("current_user", None)
        super().__init__(*args, **kwargs)
        self.fields["nombre_usuario"].disabled = True
        self.fields["nombre_usuario"].initial = self.current_user

    tipo_empresa = forms.CharField(
        max_length=80,
        label="<h7 style='color:red'>*</h7>  Tipo Empresa:",
        required=True,
        widget=forms.Select(choices=TIPO_DE_EMPRESA_LABORAL),
    )
    nombre_empresa = forms.CharField(
        max_length=80,
        label="<h7 style='color:red'>*</h7> Nombre empresa:",
        required=True,
    )
    cargo = forms.CharField(
        max_length=80, label="<h7 style='color:red'>*</h7>  Cargo:", required=True
    )

    tipo_contrato = forms.CharField(
        max_length=50,
        label="<h7 style='color:red'>*</h7>  Tipo contrato:",
        required=True,
        widget=forms.Select(choices=TITPO_CONTRATO_EMPRESA_LABORAL),
    )
    departamento_contrato = forms.CharField(
        max_length=50,
        label="Departamento:",
        required=False,
    )
    ciudad_contrato = forms.CharField(
        max_length=50,
        label="<h7 style='color:red'>*</h7> Ciudad:",
        required=True,
    )
    pais_contrato = forms.CharField(
        max_length=50,
        label="País:",
        required=False,
    )

    # jornada_laboral = forms.CharField(
    #     max_length=50,
    #     label="Jornada:",
    #     required=True,
    # )

    contacto_empresa = forms.CharField(
        max_length=20,
        label="<h7 style='color:red'>*</h7> Telefono empresa:",
        required=True,
    )

    correo_electronico_empresa = forms.EmailField(
        max_length=50,
        label="<h7 style='color:red'>*</h7> Email empresa:",
        required=True,
    )
    dependencia = forms.CharField(
        max_length=80,
        label="Dependencia:",
        required=False,
    )

    direccion_empresa = forms.CharField(
        max_length=50,
        label="<h7 style='color:red'>*</h7> Dirección empresa:",
        required=True,
    )
    fecha_inicio = forms.DateField(
        label="<h7 style='color:red'>*</h7> Fecha inicio:",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"],
    )

    fecha_fin = forms.DateField(
        label="<h7 style='color:red'>*</h7> Fecha finalización:",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"],
    )
    soportes_experincias_laborales = forms.FileField(
        label="<h7 style='color:red'>*</h7> Soporte experiencia laboral (<b>.pdf</b>):",
        required=True,
        widget=forms.FileInput(),
        validators=[
            MaxZiseFileValidator(max_file_size=0.5),
        ],
    )


class FormularioProduccionAcademica(forms.ModelForm):

    class Meta:
        model = ProduccionAcademica
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        self.current_user = kwargs.pop("current_user", None)
        super().__init__(*args, **kwargs)
        self.fields["nombre_usuario"].disabled = True
        self.fields["nombre_usuario"].initial = self.current_user

    autores_trabajo = forms.CharField(
        max_length=200,
        label="<h7 style='color:red'>*</h7>  Nombres de los autores:",
        required=True,
    )
    nombre_trabajo = forms.CharField(
        max_length=300,
        label="<h7 style='color:red'>*</h7> Nombre publicación:",
        required=True,
    )
    pais_publicacion = forms.CharField(
        max_length=50,
        label="<h7 style='color:red'>*</h7>  País:",
        required=True,
    )

    fecha_publicacion = forms.DateField(
        label="<h7 style='color:red'>*</h7>  Fecha publicaciòn:",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"],
    )
    nombre_revista = forms.CharField(
        max_length=100,
        label="<h7 style='color:red'>*</h7> Nombre revista:",
        required=True,
    )
    area_concentracion = forms.CharField(
        max_length=150,
        label="Area de concentración:",
        required=False,
    )
    linea_pesquisa = forms.CharField(
        max_length=150,
        label="Linea de investigación:",
        required=False,
    )

    doi_link_publicacion = forms.URLField(
        max_length=100,
        label="<h7 style='color:red'>*</h7> Link o DOI:",
        required=True,
    )


class FormularioParticipacionCientifica(forms.ModelForm):

    class Meta:
        model = ParticipacionCientifica
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        self.current_user = kwargs.pop("current_user", None)
        super().__init__(*args, **kwargs)
        self.fields["nombre_usuario"].disabled = True
        self.fields["nombre_usuario"].initial = self.current_user

    nombre_evento_cientifico = forms.CharField(
        max_length=200,
        label="<h7 style='color:red'>*</h7>  Nombre del evento:",
        required=True,
    )
    tipo_evento = forms.CharField(
        max_length=150,
        label="<h7 style='color:red'>*</h7> Tipo de evento:",
        required=True,
        widget=forms.Select(choices=TIPO_EVENTO_CIENTIFICO),
    )
    institucion_evento = forms.CharField(
        max_length=100,
        label="<h7 style='color:red'>*</h7>  Institución del evento:",
        required=True,
    )

    ciudad_evento = forms.CharField(
        max_length=50,
        label="<h7 style='color:red'>*</h7>  Ciudad del evento:",
        required=True,
    )
    departamento_evento = forms.CharField(
        max_length=50,
        label="Departamento del evento:",
        required=False,
    )
    pais_evento = forms.CharField(
        max_length=50,
        label="<h7 style='color:red'>*</h7> Pais del evento:",
        required=True,
    )
    fecha_inicio_evento = forms.DateField(
        label="<h7 style='color:red'>*</h7> Fecha inicio:",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"],
    )
    fecha_fin_evento = forms.DateField(
        label="<h7 style='color:red'>*</h7> Fecha fin:",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"],
    )

    modalidad_evento = forms.CharField(
        max_length=80,
        label="<h7 style='color:red'>*</h7> Rol en el evento:",
        required=True,
        widget=forms.Select(choices=MODALIDAD_EVENTO_CIENTIFICO),
    )

    soportes_eventos_cientificos = forms.FileField(
        label="<h7 style='color:red'>*</h7> soporte del evento (<b>.pdf</b>):",
        required=True,
        widget=forms.FileInput(),
        validators=[
            MaxZiseFileValidator(max_file_size=0.5),
        ],
    )


class FormularioIdiomaExtrangero(forms.ModelForm):

    class Meta:
        model = IdiomaExtrangero
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        self.current_user = kwargs.pop("current_user", None)
        super().__init__(*args, **kwargs)
        self.fields["nombre_usuario"].disabled = True
        self.fields["nombre_usuario"].initial = self.current_user

    tipo_idioma = forms.CharField(
        max_length=30,
        label="<h7 style='color:red'>*</h7>  Idioma:",
        required=True,
    )
    domimio_conversacional = forms.CharField(
        max_length=30,
        label="<h7 style='color:red'>*</h7> Dominio conversacional:",
        required=True,
        widget=forms.Select(choices=NIVEL_SUFICIENCIA_INGLES),
    )
    dominio_lectura = forms.CharField(
        max_length=30,
        label="<h7 style='color:red'>*</h7>  Dominio de la lectura:",
        required=True,
        widget=forms.Select(choices=NIVEL_SUFICIENCIA_INGLES),
    )

    dominio_escritura = forms.CharField(
        max_length=30,
        label="<h7 style='color:red'>*</h7> Dominio de la escritura:",
        required=True,
        widget=forms.Select(choices=NIVEL_SUFICIENCIA_INGLES),
    )
    nevel_certificado = forms.CharField(
        max_length=5,
        label="<h7 style='color:red'>*</h7> Pais del evento:",
        required=True,
        widget=forms.Select(choices=NIVEL_INGLES_CERTIFICADO),
    )
    institucion_expedicion_certificado = forms.CharField(
        max_length=80,
        label="<h7 style='color:red'>*</h7> Institución expedición del certificado:",
        required=True,
    )
    fecha_obtecion_certificado = forms.DateField(
        label="<h7 style='color:red'>*</h7> Fecha del certificado:",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"],
    )

    pais_obtencion_certificado = forms.CharField(
        max_length=50,
        label="<h7 style='color:red'>*</h7> País:",
        required=True,
    )

    departamento_obtencion_certificado = forms.CharField(
        max_length=50,
        label="<h7 style='color:red'>*</h7> Departamento:",
        required=True,
    )

    ciudad_obtencion_certificado = forms.CharField(
        max_length=50,
        label="<h7 style='color:red'>*</h7> Ciudad:",
        required=True,
    )

    soporte_certificado_idioma = forms.FileField(
        label="<h7 style='color:red'>*</h7> Soporte certificado de idioma (<b>.pdf</b>):",
        required=True,
        widget=forms.FileInput(),
        validators=[
            MaxZiseFileValidator(max_file_size=0.5),
        ],
    )
