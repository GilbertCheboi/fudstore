# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-21 03:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20180422_0333'),
        ('carts', '0007_auto_20180520_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='product',
        ),
        migrations.AddField(
            model_name='entry',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]
