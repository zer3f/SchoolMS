# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-09 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0032_auto_20170409_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
