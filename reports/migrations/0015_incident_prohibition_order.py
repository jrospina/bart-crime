# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0014_auto_20170807_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='prohibition_order',
            field=models.BooleanField(default=False),
        ),
    ]
