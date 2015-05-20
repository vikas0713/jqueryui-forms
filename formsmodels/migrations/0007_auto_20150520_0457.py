# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('formsmodels', '0006_auto_20150520_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loadmodels',
            name='dispatcher',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='loadmodels',
            name='ship_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
