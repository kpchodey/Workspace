# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_revo_idtestresult'),
    ]

    operations = [
        migrations.RenameField(
            model_name='revo',
            old_name='testcase_id',
            new_name='id_test_result',
        ),
        migrations.AddField(
            model_name='revo',
            name='test_case_id',
            field=models.CharField(default=datetime.datetime(2016, 8, 23, 23, 41, 45, 951913, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='revo',
            name='execution_time',
            field=models.DateTimeField(),
        ),
    ]
