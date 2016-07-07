# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(help_text=b'The name of the report displayed to the user.', unique=True)),
                ('slug', models.SlugField(help_text=b'An abbreviated name for the report.  Currently unused.', unique=True)),
                ('url_name', models.CharField(help_text=b'The url name, when using the reverse function, will provide the path to execute the report.', unique=True, max_length=64)),
            ],
            options={
                'ordering': ('name',),
                'permissions': (('view_report', 'Can view report.'),),
            },
        ),
    ]
