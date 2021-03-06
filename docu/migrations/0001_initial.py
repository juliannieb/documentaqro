# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 02:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('contenido', models.TextField(default='')),
                ('video', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=30)),
                ('mensaje', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=7)),
                ('fecha_inicio', models.DateTimeField(verbose_name='Fecha inicio')),
                ('fecha_fin', models.DateTimeField(verbose_name='Fecha fin')),
                ('texto_introductorio_jurado', models.TextField(null=True, blank=True)),
                ('texto_introductorio_invitados_especiales', models.TextField(null=True, blank=True)),
                ('texto_introductorio_talleristas', models.TextField(null=True, blank=True)),
                ('link_acreditaciones', models.CharField(max_length=2000, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Jurado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docu.Evento')),
            ],
        ),
        migrations.CreateModel(
            name='MiembroEquipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docu.Area')),
            ],
        ),
        migrations.CreateModel(
            name='MiembroStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('sinopsis', models.CharField(max_length=500)),
                ('trailer', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Proyeccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_y_hora', models.DateTimeField(verbose_name='Fecha y hora')),
                ('descripcion', models.CharField(max_length=500)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docu.Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Subscriptor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='proyeccion',
            name='sede',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docu.Sede'),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='proyeccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docu.Proyeccion'),
        ),
        migrations.AddField(
            model_name='evento',
            name='festival',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docu.Festival'),
        ),
    ]
