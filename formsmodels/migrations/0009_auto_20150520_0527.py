# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formsmodels', '0008_auto_20150520_0511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loadmodels',
            name='usd',
            field=models.IntegerField(default=10),
        ),
    ]
