# Generated by Django 4.2.10 on 2024-07-15 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AjusteDeCurva_fisilab2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('programa', models.CharField(max_length=100)),
                ('grupo', models.CharField(max_length=2)),
                ('calendario', models.DateField()),
                ('mensurando_1', models.FloatField()),
                ('error_1', models.FloatField()),
                ('sustentacion_1', models.CharField(max_length=500)),
                ('mensurando_2', models.FloatField()),
                ('error_2', models.FloatField()),
                ('sustentacion_2', models.CharField(max_length=500)),
                ('mensurando_3', models.FloatField()),
                ('sustentacion_3', models.CharField(max_length=500)),
                ('mensurando_4', models.FloatField()),
                ('error_4', models.FloatField()),
                ('sustentacion_4', models.CharField(max_length=500)),
                ('mensurando_5', models.FloatField()),
                ('error_5', models.FloatField()),
                ('sustentacion_5', models.CharField(max_length=500)),
                ('mensurando_6', models.FloatField()),
                ('sustentacion_6', models.CharField(max_length=500)),
                ('mensurando_7', models.FloatField()),
                ('error_7', models.FloatField()),
                ('sustentacion_7', models.CharField(max_length=500)),
                ('soporte', models.FileField(upload_to='files/ajuste_de_curvas')),
            ],
        ),
        migrations.CreateModel(
            name='ErroresEnMediciones_fisilab2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('programa', models.CharField(max_length=100)),
                ('grupo', models.CharField(max_length=2)),
                ('calendario', models.DateField()),
                ('mensurando_1', models.FloatField()),
                ('error_1', models.FloatField()),
                ('sustentacion_1', models.CharField(max_length=500)),
                ('mensurando_2', models.FloatField()),
                ('error_2', models.FloatField()),
                ('sustentacion_2', models.CharField(max_length=500)),
                ('mensurando_3', models.FloatField()),
                ('sustentacion_3', models.CharField(max_length=500)),
                ('mensurando_4', models.FloatField()),
                ('error_4', models.FloatField()),
                ('sustentacion_4', models.CharField(max_length=500)),
                ('mensurando_5', models.FloatField()),
                ('error_5', models.FloatField()),
                ('sustentacion_5', models.CharField(max_length=500)),
                ('mensurando_6', models.FloatField()),
                ('sustentacion_6', models.CharField(max_length=500)),
                ('mensurando_7', models.FloatField()),
                ('error_7', models.FloatField()),
                ('sustentacion_7', models.CharField(max_length=500)),
                ('soporte', models.FileField(upload_to='files/errores_en_mediciones')),
            ],
        ),
    ]