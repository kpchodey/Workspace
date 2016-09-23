# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160919_1338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='set_top_box',
            old_name='VMS_01',
            new_name='Device_Type',
        ),
        migrations.RenameField(
            model_name='set_top_box',
            old_name='VMS_02',
            new_name='IP_Adress',
        ),
        migrations.RenameField(
            model_name='set_top_box',
            old_name='VMS_JENKINS_01',
            new_name='Model_Name',
        ),
        migrations.RenameField(
            model_name='set_top_box',
            old_name='VMS_JENKINS_02',
            new_name='Serial_Number',
        ),
    ]
