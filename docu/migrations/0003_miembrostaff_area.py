# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 03:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docu', '0002_auto_20160319_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='miembrostaff',
            name='area',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='docu.Area'),
            preserve_default=False,
        ),
    ]