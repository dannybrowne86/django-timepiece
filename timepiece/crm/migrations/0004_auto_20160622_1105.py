# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20160409_2035'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='limitedaccessuserprofile',
            options={'permissions': (('can_view_limited_profile', 'Can view limited user profile'),)},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('code', 'name', 'status', 'type'), 'permissions': (('view_project', 'Can view project'), ('email_project_report', 'Can email project report'), ('view_project_time_sheet', 'Can view project time sheet'), ('export_project_time_sheet', 'Can export project time sheet'), ('generate_project_invoice', 'Can generate project invoice'), ('view_throughput_report', 'Can view project throughput report'))},
        ),
    ]
