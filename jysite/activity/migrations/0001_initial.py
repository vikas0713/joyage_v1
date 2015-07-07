# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('deleted_date', models.DateTimeField(null=True, blank=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('city', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255, null=True, blank=True)),
                ('price_unit', models.CharField(max_length=255, null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('venue', models.CharField(max_length=255)),
                ('neighborhood', models.CharField(max_length=255, null=True, blank=True)),
                ('gmap_coordinates', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=255, null=True, blank=True)),
                ('more_info_link', models.CharField(max_length=255, null=True, blank=True)),
                ('book_ticket_link', models.CharField(max_length=255, null=True, blank=True)),
                ('book_ride_link', models.CharField(max_length=255, null=True, blank=True)),
                ('image_credit_link', models.CharField(max_length=255, null=True, blank=True)),
                ('image_url', models.CharField(max_length=255, blank=True)),
                ('date', models.CharField(max_length=255, null=True, blank=True)),
                ('start_time', models.TimeField(null=True, blank=True)),
                ('end_time', models.TimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'jy_activity',
            },
        ),
        migrations.CreateModel(
            name='ActivityTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('deleted_date', models.DateTimeField(null=True, blank=True)),
                ('tag', models.CharField(max_length=255)),
                ('activity', models.ForeignKey(to='activity.Activity')),
            ],
            options={
                'db_table': 'jy_activity_tag',
            },
        ),
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('deleted_date', models.DateTimeField(null=True, blank=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'jy_mood',
            },
        ),
        migrations.CreateModel(
            name='UserActivities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activity', models.ForeignKey(to='activity.Activity')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='mood',
            field=models.ForeignKey(blank=True, to='activity.Mood', null=True),
        ),
    ]
