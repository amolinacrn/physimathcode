# Generated by Django 4.2.14 on 2024-08-14 02:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TitulosAcademico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado_academico', models.CharField(max_length=80)),
                ('titulo_obtenido', models.CharField(max_length=80)),
                ('institucion_universitaria', models.CharField(max_length=80)),
                ('programa_academico', models.CharField(max_length=80)),
                ('periodos_aprobados', models.CharField(blank=True, max_length=2, null=True)),
                ('numero_semestres_programa', models.CharField(blank=True, max_length=2, null=True)),
                ('graudado_universitario', models.CharField(max_length=3)),
                ('titulo_disertacion', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha_finalizacion', models.DateField()),
                ('numero_targeta_profesional', models.CharField(blank=True, max_length=20, null=True)),
                ('pais_titulo', models.CharField(blank=True, max_length=20, null=True)),
                ('departamento_titulo', models.CharField(max_length=20)),
                ('ciudad_titulo', models.CharField(max_length=50)),
                ('diploma_titulo', models.FileField(upload_to='files/docs/diplomas')),
                ('nombre_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProduccionAcademica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autores_trabajo', models.CharField(max_length=200)),
                ('nombre_trabajo', models.CharField(max_length=300)),
                ('pais_publicacion', models.CharField(max_length=50)),
                ('fecha_publicacion', models.DateField()),
                ('nombre_revista', models.CharField(max_length=100)),
                ('area_concentracion', models.CharField(max_length=150)),
                ('linea_pesquisa', models.CharField(max_length=150)),
                ('doi_link_publicacion', models.URLField(max_length=20)),
                ('nombre_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ParticipacionCientifica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_evento_cientifico', models.CharField(max_length=200)),
                ('tipo_evento', models.CharField(max_length=150)),
                ('institucion_evento', models.CharField(max_length=100)),
                ('ciudad_evento', models.CharField(max_length=50)),
                ('pais_evento', models.CharField(max_length=50)),
                ('fecha_inicio_evento', models.DateField()),
                ('fecha_fin_evento', models.DateField()),
                ('modalidad_evento', models.CharField(max_length=30)),
                ('soportes_eventos_cientificos', models.FileField(upload_to='files/docs/eventos')),
                ('nombre_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IdiomaExtrangero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_idioma', models.CharField(max_length=30)),
                ('domimio_conversacional', models.CharField(max_length=30)),
                ('dominio_lectura', models.CharField(max_length=30)),
                ('dominio_escritura', models.CharField(max_length=30)),
                ('nevel_certificado', models.CharField(max_length=5)),
                ('institucion_expedicion_certificado', models.CharField(max_length=80)),
                ('fecha_obtecion_certificado', models.DateField()),
                ('pais_obtencion_certificado', models.CharField(max_length=50)),
                ('departamento_obtencion_certificado', models.CharField(max_length=50)),
                ('ciudad_obtencion_certificado', models.CharField(max_length=50)),
                ('soporte_certificado_idioma', models.FileField(upload_to='files/docs/diploidiomas')),
                ('nombre_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FotosPersonale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='files/img/foto')),
                ('nombre_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExperienciasLaborale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_empresa', models.CharField(max_length=80)),
                ('nombre_empresa', models.CharField(max_length=80)),
                ('cargo', models.CharField(max_length=80)),
                ('tipo_contrato', models.CharField(blank=True, max_length=80, null=True)),
                ('departamento_contrato', models.CharField(blank=True, max_length=20, null=True)),
                ('ciudad_contrato', models.CharField(max_length=50)),
                ('pais_contrato', models.CharField(blank=True, max_length=20, null=True)),
                ('contacto_empresa', models.CharField(blank=True, max_length=20, null=True)),
                ('correo_electronico_empresa', models.EmailField(max_length=50)),
                ('dependencia', models.CharField(blank=True, max_length=80, null=True)),
                ('direccion_empresa', models.CharField(max_length=50)),
                ('fecha_inicio', models.DateField(blank=True)),
                ('fecha_fin', models.DateField(blank=True)),
                ('soportes_experincias_laborales', models.FileField(upload_to='files/docs/experiencia')),
                ('nombre_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DatosPersonale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento_identificacion', models.CharField(max_length=50)),
                ('numero_identificacion', models.CharField(max_length=20)),
                ('fecha_expedicion_documento', models.DateField()),
                ('ciudad_expedicion_documento', models.CharField(max_length=20)),
                ('primer_nombre', models.CharField(max_length=20)),
                ('segundo_nombre', models.CharField(max_length=20)),
                ('primer_apellido', models.CharField(max_length=20)),
                ('segundo_apellido', models.CharField(max_length=20)),
                ('genero_sexual', models.CharField(max_length=15)),
                ('grupo_sanguineo', models.CharField(max_length=15)),
                ('estado_civil', models.CharField(max_length=15)),
                ('pais_origen', models.CharField(max_length=15)),
                ('departamento_origen', models.CharField(max_length=20)),
                ('ciudad_nacimiento', models.CharField(max_length=20)),
                ('nacionalidad', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_nacimiento', models.DateField()),
                ('ciudad_residencia', models.CharField(max_length=20)),
                ('direccion_residencia', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono_celular', models.CharField(max_length=10)),
                ('correo_electronico', models.EmailField(max_length=50)),
                ('libreta_militar', models.CharField(blank=True, max_length=15, null=True)),
                ('distrito_militar', models.CharField(blank=True, max_length=5, null=True)),
                ('cuenta_github', models.URLField(blank=True, null=True)),
                ('fotocopia_documento', models.FileField(upload_to='files/docs/documentid')),
                ('perfil_profesional', models.TextField(blank=True, max_length=1500, null=True)),
                ('nombre_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
