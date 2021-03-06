# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-03 09:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workplan', '0002_auto_20170302_0720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='category',
        ),
        migrations.RemoveField(
            model_name='event',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
        migrations.RemoveField(
            model_name='event',
            name='rule',
        ),
        migrations.RemoveField(
            model_name='eventcategory',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='eventrelation',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='eventrelation',
            name='event',
        ),
        migrations.RemoveField(
            model_name='occurrence',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='occurrence',
            name='event',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='EventCategory',
        ),
        migrations.DeleteModel(
            name='EventRelation',
        ),
        migrations.DeleteModel(
            name='Occurrence',
        ),
        migrations.DeleteModel(
            name='Rule',
        ),
    ]
