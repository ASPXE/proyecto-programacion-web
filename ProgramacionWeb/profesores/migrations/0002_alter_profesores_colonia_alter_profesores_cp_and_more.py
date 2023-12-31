# Generated by Django 4.2.3 on 2023-08-01 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colonias', '0002_alter_colonias_codigopostal'),
        ('codigoPostal', '0002_alter_codigopostal_municipio'),
        ('municipios', '0002_alter_municipios_estado'),
        ('gradoEstudios', '0001_initial'),
        ('estados', '0002_alter_estados_pais'),
        ('profesores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesores',
            name='colonia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='colonias.colonias'),
        ),
        migrations.AlterField(
            model_name='profesores',
            name='cp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='codigoPostal.codigopostal'),
        ),
        migrations.AlterField(
            model_name='profesores',
            name='estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='estados.estados'),
        ),
        migrations.AlterField(
            model_name='profesores',
            name='gradoEstudios',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gradoEstudios.gradoestudios'),
        ),
        migrations.AlterField(
            model_name='profesores',
            name='municipio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='municipios.municipios'),
        ),
    ]
