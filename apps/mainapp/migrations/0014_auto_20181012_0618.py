# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-12 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_auto_20181011_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity_sold',
            field=models.IntegerField(default=0),
        ),
    ]