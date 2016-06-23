# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_auto_20160622_1105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='limitedaccessuserprofile',
            options={'permissions': (('view_limited_profile', 'Can view limited user profile'),)},
        ),
        migrations.AlterModelOptions(
            name='paidtimeoffrequest',
            options={'ordering': ('user_profile', '-pto_start_date'), 'permissions': (('approve_pto_requests', 'Can approve PTO requests'), ('process_pto_requests', 'Can payroll process PTO requests'))},
        ),
    ]
