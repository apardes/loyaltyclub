# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 13, 18, 48, 1, 115809)),
        ),
        migrations.AlterField(
            model_name='credit',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 13, 18, 48, 1, 116378)),
        ),
        migrations.AlterField(
            model_name='member',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 13, 18, 48, 1, 115151)),
        ),
    ]
