# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0012_auto_20150706_1848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='is_availabe',
            new_name='is_available',
        ),
    ]
