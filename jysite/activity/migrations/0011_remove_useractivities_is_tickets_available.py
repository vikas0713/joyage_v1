# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0010_auto_20150706_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useractivities',
            name='is_tickets_available',
        ),
    ]
