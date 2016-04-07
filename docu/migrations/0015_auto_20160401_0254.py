# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 02:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docu', '0014_highlights_posicion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conferencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=2000)),
                ('nombre_conferencista', models.CharField(max_length=200)),
                ('fecha_y_hora', models.DateTimeField(verbose_name='Fecha y hora')),
                ('fecha_y_hora_final', models.DateTimeField(verbose_name='Fecha y hora final')),
                ('imagen', models.ImageField(default='static/default.jpg', upload_to='Conferencia')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docu.Evento')),
                ('sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docu.Sede')),
            ],
        ),
        migrations.CreateModel(
            name='Taller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=2000)),
                ('fecha_y_hora', models.DateTimeField(verbose_name='Fecha y hora')),
                ('fecha_y_hora_final', models.DateTimeField(verbose_name='Fecha y hora final')),
                ('imagen', models.ImageField(default='static/default.jpg', upload_to='talleres')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docu.Evento')),
                ('sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docu.Sede')),
            ],
        ),
        migrations.RenameField(
            model_name='pelicula',
            old_name='imagen',
            new_name='poster',
        ),
        migrations.AddField(
            model_name='pelicula',
            name='still',
            field=models.ImageField(default='static/default.jpg', upload_to='peliculas'),
        ),
    ]
