# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 06:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docu', '0013_festival_nombre_corto'),
    ]

    operations = [
        migrations.AddField(
            model_name='highlights',
            name='posicion',
            field=models.IntegerField(choices=[(0, 'Centro'), (1, 'Izquierda'), (2, 'Derecha')], default=0),
        ),
    ]
