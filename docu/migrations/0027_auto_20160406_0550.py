# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docu', '0026_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='video',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]