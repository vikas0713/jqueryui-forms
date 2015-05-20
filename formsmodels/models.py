from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.

status=(
    ('Opened', 'Opened'),
    ('Dispatched', 'Dispatched'),
    ('Pending','Pending'),
    ('Complete','Complete'),
    ('Loaded','Loaded'),
    ('Unloaded','Unloaded'),
    ('Free','Free'),
    ('OnRoute','OnRoute'),
    ('InYard','InYard'),
    ('Delivered','Delivered'),
    ('Covered','Covered'),
)

Types=(
    ('25lbs Sacks','25lbs Stack'),
    ('40lbs Cartons','40lbs Cartons'),
    ('50lbs Sacks','50lbs Sacks'),
    ('Air Freight','Air Freight'),
    ('Barrels','Barrels'),
    ('Bushels','Bushels'),
    ('Cubic Yard','Cubic Yard'),
    ('CWT/100lbs','CWT/100lbs'),
    ('CWT/1lbs','CWT/1lbs'),
    ('CWT/1Ton','CWT/1Ton'),
    ('Delivery','Delivery'),
    ('Direct','Direct'),
    ('Drop','Drop'),
    ('Equip. Rental-Daily','Equip. Rental-Daily'),
    ('Equip. Rental-Monthly','Equip. Rental-Monthly'),
    ('Equip. Rental-Weekly','Equip. Rental-Weekly'),
    ('Feet','Feet'),
    ('FlatBed','FlatBed'),
    ('Full Truck Load','Full Truck Load'),
    ('Hot Shot','Hot Shot'),
    ('Hourly','Hourly'),
    ('Labour','Labour'),
    ('Line Haul','Line Haul'),
    ('LBS','LBS'),
    ('LTL','LTL'),
    ('Metric Ton','Metric Ton'),
    ('Ocean','Ocean'),
    ('Other','Other'),
    ('Pallets','Pallets'),
    ('Pickup','Pickup'),
    ('Piece','Piece'),
    ('Profit Share','Profit Share'),
    ('Rail','Rail'),
    ('RPM','RPM'),
    ('RPM(fsc)','RPM(fsc)'),
    ('Tons','Tons'),
    ('Truck Ordered Not Used','Truck Ordered Not Used'),
  )
owner=(
        ('Company Truck','Company Truck'),
        ('Other','Other')
      )

class Truck(models.Model):
    truck_no=models.IntegerField(unique=True)
    truck_type=models.CharField(max_length=100,default='none')
    license_plate=models.CharField(max_length=100,default='none')
    plate_expiry=models.DateTimeField(default='none')
    inspection_expiry=models.DateTimeField(null=True)
    internal_notes=models.CharField(max_length=200,default='none')
    status=models.CharField(max_length=100,default='none')
    ownership=models.CharField(choices=owner,max_length=100,default='Company Truck')
    mileage=models.IntegerField(default=0)
    start_date=models.DateTimeField(null=True)
    axles=models.CharField(default='none',max_length=100)
    fuel_type=models.CharField(default='none',max_length=100)
    deactivation=models.DateTimeField(null=True)
    registered_state=models.CharField(default='none',max_length=100)
    insurance_no=models.CharField(default='none',max_length=100)
    gross_weight=models.IntegerField(default=0)
    vehicle_id=models.CharField(unique=True,max_length=100)
    dot_expiry=models.DateTimeField(null=True)

class Trailer(models.Model):
    trailer_no=models.IntegerField(unique=True)
    trailer_type=models.CharField(max_length=100,default='none')
    license_plate=models.CharField(max_length=100,default='none')
    plate_expiry=models.DateTimeField(default='none')
    inspection_expiry=models.DateTimeField(null=True)
    internal_notes=models.CharField(max_length=200,default='none')
    status=models.CharField(max_length=100,default='none')
    ownership=models.CharField(max_length=100,default='none')
    mileage=models.IntegerField(default=0)
    start_date=models.DateTimeField(null=True)
    axles=models.CharField(default='none',max_length=100)
    fuel_type=models.CharField(default='none',max_length=100)
    deactivation=models.DateTimeField(null=True)
    registered_state=models.CharField(default='none',max_length=100)
    insurance_no=models.CharField(default='none',max_length=100)
    gross_weight=models.IntegerField(default=0)
    vehicle_id=models.CharField(unique=True,max_length=100)
    dot_expiry=models.DateTimeField(null=True)
    

class SingleDriver(models.Model):
    driver_name=models.CharField(max_length=100,default='none')
    telephone=models.IntegerField(default=0)
    cell_phone=models.IntegerField(default=0)
    pager=models.IntegerField(default=0)
    email=models.EmailField(null=True)
    address=models.CharField(default='none',max_length=100)
    country=models.CharField(default='none',max_length=100)
    state=models.CharField(default='none',max_length=100)
    city=models.CharField(default='none',max_length=100)
    zip_code=models.IntegerField(default=0)
    dob=models.DateTimeField(null=True)
    hire_date=models.DateTimeField(null=True)
    last_medical=models.DateTimeField(null=True)
    last_drug_test=models.DateTimeField(null=True)
    next_drug_test=models.DateTimeField(null=True)
    passport_expiry=models.DateTimeField(null=True)
    license_no=models.CharField(max_length=100,default='none')
    license_expiry=models.DateTimeField(null=True)
    fast_card_expiry=models.DateTimeField(null=True)
    hazmat_expiry=models.DateTimeField(null=True)
    internal_notes=models.CharField(max_length=200,default='none')
    pay=models.IntegerField(default=0)
    pay_type=models.CharField(default='none',max_length=100)
    currency=models.CharField(default='USD',max_length=100)
    pay_details=models.CharField(default='none',max_length=200)

class TeamDriver(models.Model):
    driver_name=models.CharField(max_length=100,default='none')
    telephone=models.IntegerField(default=0)
    cell_phone=models.IntegerField(default=0)
    pager=models.IntegerField(default=0)
    email=models.EmailField(null=True)
    address=models.CharField(default='none',max_length=100)
    country=models.CharField(default='none',max_length=100)
    state=models.CharField(default='none',max_length=100)
    city=models.CharField(default='none',max_length=100)
    zip_code=models.IntegerField(default=0)
    dob=models.DateTimeField(null=True)
    hire_date=models.DateTimeField(null=True)
    last_medical=models.DateTimeField(null=True)
    last_drug_test=models.DateTimeField(null=True)
    next_drug_test=models.DateTimeField(null=True)
    passport_expiry=models.DateTimeField(null=True)
    passport_expiry=models.DateTimeField(null=True)
    license_no=models.CharField(max_length=100,default='none')
    license_expiry=models.DateTimeField(null=True)
    fast_card_expiry=models.DateTimeField(null=True)
    hazmat_expiry=models.DateTimeField(null=True)
    internal_notes=models.CharField(max_length=200,default='none')
    pay=models.IntegerField(default=0)
    pay_type=models.CharField(default='none',max_length=100)
    currency=models.CharField(default='USD',max_length=100)
    pay_details=models.CharField(default='none',max_length=200)
    driver_name2=models.CharField(max_length=100,default='none')
    telephone2=models.IntegerField(default=0)
    cell_phone2=models.IntegerField(default=0)
    pager2=models.IntegerField(default=0)
    email2=models.EmailField(null=True)
    address2=models.CharField(default='none',max_length=100)
    country2=models.CharField(default='none',max_length=100)
    state2=models.CharField(default='none',max_length=100)
    city2=models.CharField(default='none',max_length=100)
    zip_code2=models.IntegerField(default=0)
    dob2=models.DateTimeField(null=True)
    hire_date2=models.DateTimeField(null=True)
    last_medical2=models.DateTimeField(null=True)
    last_drug_test2=models.DateTimeField(null=True)
    next_drug_test2=models.DateTimeField(null=True)
    passport_expiry2=models.DateTimeField(null=True)
    passport_expiry2=models.DateTimeField(null=True)
    license_no2=models.CharField(max_length=100,default='none')
    license_expiry2=models.DateTimeField(null=True)
    fast_card_expiry2=models.DateTimeField(null=True)
    hazmat_expiry2=models.DateTimeField(null=True)
    internal_notes2=models.CharField(max_length=200,default='none')
    pay2=models.IntegerField(default=0)
    pay_type2=models.CharField(default='none',max_length=100)
    currency2=models.CharField(default='USD',max_length=100)
    pay_details2=models.CharField(default='none',max_length=200)
    
class Customers(models.Model):
    name=models.CharField(max_length=100, default='none')
    customer_id=models.CharField(max_length=100, default='none')
    address1=models.CharField(max_length=100, default='none')
    address2=models.CharField(max_length=100, default='none')
    address3=models.CharField(max_length=100, default='none')
    country=models.CharField(max_length=100, default='none')
    state=models.CharField(max_length=100, default='none')
    city=models.CharField(max_length=100, default='none')
    bill_address1=models.CharField(max_length=100, default='none')
    bill_address2=models.CharField(max_length=100, default='none')
    bill_address3=models.CharField(max_length=100, default='none')
    bill_country=models.CharField(max_length=100, default='none')
    bill_state=models.CharField(max_length=100, default='none')
    bill_city=models.CharField(max_length=100, default='none')
    primary_contact=models.CharField(max_length=100, default='none')
    primary_contact=models.IntegerField( default=0)
    telephone=models.IntegerField( default=0)
    telephone_ext=models.IntegerField( default=0)
    email=models.EmailField( null=True)
    toll_free=models.IntegerField( default=0)
    secondary_contact=models.IntegerField( default=0)
    secondary_email=models.EmailField(null=True)
    billing_email=models.IntegerField( default=0)
    bill_telephone=models.IntegerField(default=0)
    bill_ext=models.IntegerField(default=0)
    advanced_internal=models.TextField(default='none')

class LoadModels(models.Model):
    load=models.AutoField(primary_key=True)
    bill_to=models.CharField(max_length=100, default='none')
    dispatcher=models.ForeignKey(User)
    sales=models.CharField(max_length=50, default='Sales Repo 1')
    status=models.CharField(choices=status, max_length=50,default='Opened')
    types=models.CharField(choices=Types,max_length=50, default='Line Haul')
    rate=models.IntegerField(default=0)
    PDs=models.IntegerField(default=0)
    usd=models.IntegerField(default=10)
    carrier=models.CharField(max_length=100, default='none')
    carrier_fee=models.IntegerField(default=0)
    currency_type=models.CharField(max_length=50,default='USD')
    driver=models.CharField(max_length=100, default='none')
    truck=models.CharField(max_length=100, default='none')
    trailer=models.CharField(max_length=100, default='none')
    flat_rate=models.IntegerField( default=0)
    shipper=models.CharField(max_length=200, default='none')
    location=models.CharField(max_length=200, default='none')
    ship_date=models.DateTimeField(default=now)
    description=models.CharField(max_length=200, default='none')
    ship_type=models.CharField(max_length=200, default='none')
    ship_qty=models.IntegerField(default=0)
    ship_weight=models.IntegerField(default=0)
    shipping_notes=models.CharField(max_length=200, default='none')
    ship_po=models.IntegerField(default=0)
    custom_broker=models.CharField(max_length=200,default='none')
    consignee=models.CharField(max_length=200, default='none')
    c_location=models.CharField(max_length=200, default='none')
    c_date=models.DateTimeField(null=True)
    c_description=models.CharField(max_length=200, default='none')
    c_type=models.CharField(max_length=200, default='none')
    c_qty=models.IntegerField(default=0)
    c_weight=models.IntegerField(default=0)
    delivery_notes=models.CharField(max_length=200, default='none')
    c_po=models.IntegerField(default=0)
    promiles=models.IntegerField(default=0)
    drivermiles=models.IntegerField(default=0)
    