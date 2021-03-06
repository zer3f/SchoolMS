# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20170322_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AddField(
            model_name='feestruct',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='hasVan',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='feestruct',
            name='acadYear',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentID',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
