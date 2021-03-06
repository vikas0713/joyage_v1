# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useractivities',
            name='is_bookmarked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useractivities',
            name='is_going',
            field=models.BooleanField(default=False),
        ),
    ]
