# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-24 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0011_auto_20180524_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
