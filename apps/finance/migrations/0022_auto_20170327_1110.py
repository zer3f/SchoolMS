# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_auto_20170325_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='id',
        ),
        migrations.AddField(
            model_name='class',
            name='acadYear',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
