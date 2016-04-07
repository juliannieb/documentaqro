# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docu', '0033_pelicula_origen'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='texto_introductorio_invitados_especiales',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='evento',
            name='texto_introductorio_jurado',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='evento',
            name='texto_introductorio_talleristas',
            field=models.TextField(blank=True, null=True),
        ),
    ]
