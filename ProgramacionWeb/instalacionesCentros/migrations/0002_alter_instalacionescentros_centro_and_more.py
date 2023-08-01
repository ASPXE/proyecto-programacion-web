# Generated by Django 4.2.3 on 2023-08-01 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('centros', '0004_alter_centros_codigopostal_alter_centros_colonia_and_more'),
        ('instalaciones', '0001_initial'),
        ('instalacionesCentros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instalacionescentros',
            name='centro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='centros.centros'),
        ),
        migrations.AlterField(
            model_name='instalacionescentros',
            name='instalacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='instalaciones.instalaciones'),
        ),
    ]
