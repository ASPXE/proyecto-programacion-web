# Generated by Django 4.2.3 on 2023-07-25 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('municipios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodigoPostal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cp', models.CharField(max_length=5)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='municipios.municipios')),
            ],
        ),
    ]
