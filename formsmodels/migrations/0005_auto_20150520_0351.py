# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formsmodels', '0004_auto_20150519_1050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trailer',
            old_name='trailersss_type',
            new_name='trailer_type',
        ),
        migrations.AlterField(
            model_name='loadmodels',
            name='bill_to',
            field=models.CharField(default=b'none', max_length=100),
        ),
        migrations.AlterField(
            model_name='loadmodels',
            name='c_description',
            field=models.CharField(default=b'none', max_length=200),
        ),
        migrations.AlterField(
            model_name='loadmodels',
            name='c_location',
            field=models.CharField(default=b'none', max_length=200),
        ),
        migrations.AlterField(
            model_name='loadmodels',
            name='c_type',
            field=models.CharField(default=b'none', max_length=200),
        ),
        migrations.AlterField(
            model_name='loadmodels',
            name='carrier',
            field=models.CharField(default=b'none', max_length=100),
        ),
        migrations.AlterField(
            model_name='loadmodels',
            name='consignee',
            field=models.CharField(default=b'none', max_length=200),
        ),
        migrations.AlterField(
            model_name='loadmodels',
            name='custom_broker',
            field=models.CharField(default=b'none', max_length=200),
        ),
        migrations.AlterField(
            model_name='loadmodels',
            name='delivery_notes',
            field=models.CharField(default=b'none', max_length=200),
        ),
        migrations.AlterField(
            model_name='loadmodels',
            name='description',
            field=models.CharField(default=b'none', max_length=200),
        ),
        migrations.AlterField(
            model_name='loadmodels',
            name='dispatcher',
            field=models.CharField(default=b'none', max_length=100),
        ),
        migrations.AlterField(
            model_name='loadmodels',
            name='driver',
            field=models.CharField(default=b'none', max_length=100),
        ),
        migrations.AlterField(
            model_name='loadmodels',
            name='location',
            field=models.CharField(default=b'none', max_length=200),
        ),
        migrations.AlterField(
            model_name='loadmodels',
            name='ship_type',
            field=models.CharField(default=b'none', max_length=200),
        ),
        migrations.AlterField(
            model_name='loadmodels',
            name='shipper',
            field=models.CharField(default=b'none', max_length=200),
        ),
        migrations.AlterField(
            model_name='loadmodels',
            name='shipping_notes',
            field=models.CharField(default=b'none', max_length=200),
        ),
        migrations.AlterField(
            model_name='loadmodels',
            name='status',
            field=models.CharField(default=b'none', max_length=50),
        ),
        migrations.AlterField(
            model_name='loadmodels',
            name='trailer',
            field=models.CharField(default=b'none', max_length=100),
        ),
        migrations.AlterField(
            model_name='loadmodels',
            name='truck',
            field=models.CharField(default=b'none', max_length=100),
        ),
        migrations.AlterField(
            model_name='loadmodels',
            name='types',
            field=models.CharField(default=b'none', max_length=50),
        ),
    ]
