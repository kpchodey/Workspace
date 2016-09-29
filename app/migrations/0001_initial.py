# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appium',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('details', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Appium',
            },
        ),
        migrations.CreateModel(
            name='Revo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idTestResult', models.CharField(max_length=30)),
                ('date', models.DateTimeField()),
                ('suite_name', models.CharField(max_length=30)),
                ('project_name', models.CharField(max_length=30)),
                ('testcase_id', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('tester', models.CharField(max_length=30)),
                ('box_type', models.CharField(max_length=30)),
                ('box_unit_adress', models.CharField(max_length=30)),
                ('box_ip', models.CharField(max_length=30)),
                ('total_actions', models.CharField(max_length=30)),
                ('toatl_conditions', models.CharField(max_length=30)),
                ('pass_numbers', models.CharField(max_length=30)),
                ('fail_numbers', models.CharField(max_length=30)),
                ('result', models.CharField(max_length=30)),
                ('execution_time', models.CharField(max_length=30)),
                ('test_job_name', models.CharField(max_length=30)),
                ('test_job_executionid', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Revo',
            },
        ),
        migrations.CreateModel(
            name='Storm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('details', models.TextField(blank=True)),
                ('date', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Storm',
            },
        ),
    ]
