# Generated by Django 5.1 on 2024-10-04 05:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobskill1', '0001_initial'),
        ('paginaEmpresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv', models.FileField(upload_to='Candidatos')),
                ('solicitudD', models.CharField(blank=True, max_length=100, null=True)),
                ('aprobado', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('postulante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobskill1.usuarios')),
                ('puesto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paginaEmpresa.puesto')),
            ],
        ),
    ]
