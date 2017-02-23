# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TODO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Name of todo', max_length=100)),
                ('description', models.CharField(help_text=b'description of todo', max_length=200)),
                ('priority', models.IntegerField(default=2, help_text=b'Priority', choices=[(1, b'High'), (2, b'Medium'), (3, b'Low')])),
                ('task_status', models.IntegerField(default=1, choices=[(1, b'Todo'), (2, b'Doing'), (3, b'Done')])),
                ('due_date', models.DateField()),
            ],
        ),
    ]
