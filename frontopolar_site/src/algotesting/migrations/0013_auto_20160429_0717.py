# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algotesting', '0012_auto_20160429_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experimentresult',
            name='results_path',
            field=models.FilePathField(default=b''),
        ),
    ]
