# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0016_auto_20150707_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='useractivities',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]
