# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 08:44
from __future__ import unicode_literals

from django.db import migrations
import izi.models.fields.slugfield


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0006_auto_20160111_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='line_reference',
            field=izi.models.fields.slugfield.SlugField(max_length=128, verbose_name='Line Reference'),
        ),
    ]
