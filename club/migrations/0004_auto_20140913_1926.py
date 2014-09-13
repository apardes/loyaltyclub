# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0003_auto_20140913_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='verified',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='business',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 13, 19, 26, 17, 417602)),
        ),
        migrations.AlterField(
            model_name='credit',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 13, 19, 26, 17, 418028)),
        ),
        migrations.AlterField(
            model_name='member',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 13, 19, 26, 17, 417032)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 13, 19, 26, 17, 418628)),
        ),
    ]
