# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-11 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_hw_malfunction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset_printer',
            name='cartridge_number',
            field=models.CharField(blank=True, max_length=120, verbose_name='رقم عبوة الحبر '),
        ),
    ]
