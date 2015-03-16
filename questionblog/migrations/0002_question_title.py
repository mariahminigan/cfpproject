# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('questionblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(default=datetime.datetime(2015, 3, 16, 15, 35, 49, 263613), max_length=200),
            preserve_default=False,
        ),
    ]
