# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_usertestimonials_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertestimonials',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 5, 4, 11, 52, 365434, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
