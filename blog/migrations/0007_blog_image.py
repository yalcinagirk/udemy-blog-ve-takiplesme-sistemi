# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-25 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180826_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Resim'),
        ),
    ]
