# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 03:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docu', '0017_auto_20160401_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='proyeccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='docu.Proyeccion'),
        ),
    ]