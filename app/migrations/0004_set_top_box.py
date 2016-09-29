# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160823_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Set_Top_Box',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('VMS_01', models.CharField(max_length=30)),
                ('VMS_02', models.DateTimeField()),
                ('VMS_JENKINS_01', models.CharField(max_length=30)),
                ('VMS_JENKINS_02', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Set Top Box',
            },
        ),
    ]
