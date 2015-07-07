# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0018_auto_20150707_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='useractivities',
            name='is_attended',
            field=models.BooleanField(default=False),
        ),
    ]
