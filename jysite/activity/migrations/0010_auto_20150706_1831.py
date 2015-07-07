# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0009_auto_20150706_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='is_availabe',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='useractivities',
            name='is_started',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useractivities',
            name='is_tickets_available',
            field=models.BooleanField(default=True),
        ),
    ]
