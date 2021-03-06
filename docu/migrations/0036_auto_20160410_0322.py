# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-10 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docu', '0035_invitadoespecial_titulo_participacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='btn_actividades',
            field=models.ImageField(blank=True, null=True, upload_to='eventos'),
        ),
        migrations.AddField(
            model_name='evento',
            name='btn_proyecciones',
            field=models.ImageField(blank=True, null=True, upload_to='eventos'),
        ),
        migrations.AddField(
            model_name='evento',
            name='btn_seleccion_oficial',
            field=models.ImageField(blank=True, null=True, upload_to='eventos'),
        ),
        migrations.AddField(
            model_name='evento',
            name='header_actividades',
            field=models.ImageField(blank=True, null=True, upload_to='eventos'),
        ),
        migrations.AddField(
            model_name='evento',
            name='header_seleccion_oficial',
            field=models.ImageField(blank=True, null=True, upload_to='eventos'),
        ),
        migrations.AddField(
            model_name='evento',
            name='texto_introductorio_seleccion_oficial_internacional',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='evento',
            name='texto_introductorio_seleccion_oficial_nacional',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='evento',
            name='link_acreditaciones',
            field=models.CharField(max_length=2000, null=True, blank=True),
        ),
    ]
