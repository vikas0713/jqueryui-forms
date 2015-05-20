# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formsmodels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loadmodels',
            name='flat_rate',
            field=models.IntegerField(default=0),
        ),
    ]
