# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-21 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160316_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenes',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]