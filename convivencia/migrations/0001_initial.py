# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-10-20 07:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('centro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amonestaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField()),
                ('Hora', models.CharField(choices=[('1', 'Primera'), ('2', 'Segunda'), ('3', 'Tercera'), ('4', 'Recreo'), ('5', 'Cuarta'), ('6', 'Quinta'), ('7', 'Sexta')], default='1', max_length=1)),
                ('Comentario', models.TextField(blank=True)),
                ('IdAlumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centro.Alumnos')),
                ('Profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centro.Profesores')),
            ],
            options={
                'verbose_name': 'Amonestaci\xf3n',
                'verbose_name_plural': 'Amonestaciones',
            },
        ),
        migrations.CreateModel(
            name='Sanciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField()),
                ('Fecha_fin', models.DateField(verbose_name='Fecha finalizaci\xf3n')),
                ('Sancion', models.CharField(blank=True, max_length=100)),
                ('Comentario', models.TextField(blank=True)),
                ('IdAlumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centro.Alumnos')),
            ],
            options={
                'verbose_name': 'Sanci\xf3n',
                'verbose_name_plural': 'Sanciones',
            },
        ),
        migrations.CreateModel(
            name='TiposAmonestaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TipoAmonestacion', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Tipo Amonestaci\xf3n',
                'verbose_name_plural': 'Tipos de Amonestaciones',
            },
        ),
        migrations.AddField(
            model_name='amonestaciones',
            name='Tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Tipo_de', to='convivencia.TiposAmonestaciones'),
        ),
    ]
