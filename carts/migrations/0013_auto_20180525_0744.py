# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-25 04:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0012_auto_20180524_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
