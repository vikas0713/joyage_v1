# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0007_auto_20150705_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='useractivities',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
