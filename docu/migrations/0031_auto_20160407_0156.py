# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docu', '0030_auto_20160407_0154'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitadoespecial',
            name='foto',
            field=models.ImageField(default='static/default.jpg', upload_to='jurado'),
        ),
        migrations.AddField(
            model_name='tallerista',
            name='foto',
            field=models.ImageField(default='static/default.jpg', upload_to='jurado'),
        ),
    ]
