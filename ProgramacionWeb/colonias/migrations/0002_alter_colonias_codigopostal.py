# Generated by Django 4.2.3 on 2023-08-01 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codigoPostal', '0002_alter_codigopostal_municipio'),
        ('colonias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colonias',
            name='codigoPostal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='codigoPostal.codigopostal'),
        ),
    ]
