# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_auto_20140913_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=20, decimal_places=2)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2014, 9, 13, 19, 25, 13, 184447))),
                ('business', models.ForeignKey(to='club.Business')),
                ('member', models.ForeignKey(to='club.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='business',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 13, 19, 25, 13, 183338)),
        ),
        migrations.AlterField(
            model_name='credit',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 13, 19, 25, 13, 183837)),
        ),
        migrations.AlterField(
            model_name='member',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 13, 19, 25, 13, 182837)),
        ),
    ]
