# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-10 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docu', '0037_evento_header_proyecciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='texto_introductorio_premios',
            field=models.TextField(blank=True, null=True),
        ),
    ]