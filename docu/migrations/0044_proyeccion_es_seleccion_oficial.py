# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-12 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docu', '0043_pelicula_proyeccion_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyeccion',
            name='es_seleccion_oficial',
            field=models.BooleanField(default=False),
        ),
    ]
