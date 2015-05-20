# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formsmodels', '0007_auto_20150520_0457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loadmodels',
            old_name='pd',
            new_name='PDs',
        ),
        migrations.AlterField(
            model_name='loadmodels',
            name='types',
            field=models.CharField(default=b'Line Haul', max_length=50, choices=[(b'25lbs Sacks', b'25lbs Stack'), (b'40lbs Cartons', b'40lbs Cartons'), (b'50lbs Sacks', b'50lbs Sacks'), (b'Air Freight', b'Air Freight'), (b'Barrels', b'Barrels'), (b'Bushels', b'Bushels'), (b'Cubic Yard', b'Cubic Yard'), (b'CWT/100lbs', b'CWT/100lbs'), (b'CWT/1lbs', b'CWT/1lbs'), (b'CWT/1Ton', b'CWT/1Ton'), (b'Delivery', b'Delivery'), (b'Direct', b'Direct'), (b'Drop', b'Drop'), (b'Equip. Rental-Daily', b'Equip. Rental-Daily'), (b'Equip. Rental-Monthly', b'Equip. Rental-Monthly'), (b'Equip. Rental-Weekly', b'Equip. Rental-Weekly'), (b'Feet', b'Feet'), (b'FlatBed', b'FlatBed'), (b'Full Truck Load', b'Full Truck Load'), (b'Hot Shot', b'Hot Shot'), (b'Hourly', b'Hourly'), (b'Labour', b'Labour'), (b'Line Haul', b'Line Haul'), (b'LBS', b'LBS'), (b'LTL', b'LTL'), (b'Metric Ton', b'Metric Ton'), (b'Ocean', b'Ocean'), (b'Other', b'Other'), (b'Pallets', b'Pallets'), (b'Pickup', b'Pickup'), (b'Piece', b'Piece'), (b'Profit Share', b'Profit Share'), (b'Rail', b'Rail'), (b'RPM', b'RPM'), (b'RPM(fsc)', b'RPM(fsc)'), (b'Tons', b'Tons'), (b'Truck Ordered Not Used', b'Truck Ordered Not Used')]),
        ),
    ]
