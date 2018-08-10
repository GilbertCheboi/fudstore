# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-27 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_total',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=100),
        ),
    ]
