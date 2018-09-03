# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-27 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=225)),
                ('unit_price', models.FloatField()),
                ('status', models.IntegerField()),
                ('image', models.ImageField(upload_to='product_image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
