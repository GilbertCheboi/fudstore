# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-24 11:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]
