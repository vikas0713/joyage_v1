# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0017_useractivities_is_done'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useractivities',
            name='is_done',
        ),
        migrations.RemoveField(
            model_name='useractivities',
            name='is_started',
        ),
    ]
