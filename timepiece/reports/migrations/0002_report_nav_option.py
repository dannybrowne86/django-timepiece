# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='nav_option',
            field=models.BooleanField(default=True, help_text=b'Should this report be listed in the Nav Bar?'),
        ),
    ]
