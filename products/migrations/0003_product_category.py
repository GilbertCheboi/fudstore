# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-10 09:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.Category'),
        ),
    ]
