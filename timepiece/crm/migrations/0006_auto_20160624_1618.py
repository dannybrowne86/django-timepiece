# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_auto_20160623_1047'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paidtimeoffrequest',
            options={'ordering': ('user_profile', '-pto_start_date'), 'permissions': (('approve_pto_request', 'Can approve PTO requests'), ('process_pto_request', 'Can payroll process PTO requests'))},
        ),
    ]
