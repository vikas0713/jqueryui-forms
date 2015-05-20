# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formsmodels', '0002_auto_20150513_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='loadmodels',
            name='carrier_fee',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='loadmodels',
            name='currency_type',
            field=models.CharField(default=b'USD', max_length=50),
        ),
        migrations.AddField(
            model_name='loadmodels',
            name='drivermiles',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='loadmodels',
            name='promiles',
            field=models.IntegerField(default=0),
        ),
    ]
