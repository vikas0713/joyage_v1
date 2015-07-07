# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0015_auto_20150706_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useractivities',
            name='is_completed',
        ),
        migrations.AddField(
            model_name='activity',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
