# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-08 14:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0002_auto_20180422_0333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='county',
            new_name='Estate',
        ),
    ]
