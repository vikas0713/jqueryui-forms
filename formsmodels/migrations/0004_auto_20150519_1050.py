# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formsmodels', '0003_auto_20150513_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trailer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trailer_no', models.IntegerField(unique=True)),
                ('trailersss_type', models.CharField(default=b'none', max_length=100)),
                ('license_plate', models.CharField(default=b'none', max_length=100)),
                ('plate_expiry', models.DateTimeField(default=b'none')),
                ('inspection_expiry', models.DateTimeField(null=True)),
                ('internal_notes', models.CharField(default=b'none', max_length=200)),
                ('status', models.CharField(default=b'none', max_length=100)),
                ('ownership', models.CharField(default=b'none', max_length=100)),
                ('mileage', models.IntegerField(default=0)),
                ('start_date', models.DateTimeField(null=True)),
                ('axles', models.CharField(default=b'none', max_length=100)),
                ('fuel_type', models.CharField(default=b'none', max_length=100)),
                ('deactivation', models.DateTimeField(null=True)),
                ('registered_state', models.CharField(default=b'none', max_length=100)),
                ('insurance_no', models.CharField(default=b'none', max_length=100)),
                ('gross_weight', models.IntegerField(default=0)),
                ('vehicle_id', models.CharField(unique=True, max_length=100)),
                ('dot_expiry', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customers',
            name='advanced_internal',
            field=models.TextField(default=b'none'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='secondary_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='loadmodels',
            name='sales',
            field=models.CharField(default=b'Sales Repo 1', max_length=50),
        ),
    ]
