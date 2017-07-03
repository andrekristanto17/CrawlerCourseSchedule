# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-03 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0003_auto_20170703_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='from_course_code',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='from_index_code',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='index_code',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
