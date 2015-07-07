# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0005_usertestimonials_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertestimonials',
            name='activity',
            field=models.IntegerField(),
        ),
    ]
