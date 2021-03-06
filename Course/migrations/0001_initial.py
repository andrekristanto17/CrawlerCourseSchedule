# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-03 09:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=250)),
                ('course_code', models.CharField(max_length=250)),
                ('course_au', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_code', models.CharField(max_length=250)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10, null=True)),
                ('group', models.CharField(max_length=10, null=True)),
                ('day', models.CharField(max_length=10, null=True)),
                ('time', models.CharField(max_length=10, null=True)),
                ('venue', models.CharField(max_length=10, null=True)),
                ('remark', models.CharField(max_length=50, null=True)),
                ('index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.Index')),
            ],
        ),
    ]
