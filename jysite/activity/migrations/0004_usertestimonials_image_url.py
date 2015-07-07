# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0003_usertestimonials'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertestimonials',
            name='image_url',
            field=models.CharField(default=datetime.datetime(2015, 7, 4, 15, 54, 15, 51698, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]
