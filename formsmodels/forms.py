from django import forms
from models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, ButtonHolder
from crispy_forms.bootstrap import FormActions




class LoadForm(forms.ModelForm):
    
    helper=FormHelper()
    helper.layout = Layout(
        Div(
        Div(
            Div('bill_to',css_class='col-md-4'),
            Div('dispatcher',css_class='col-md-4'),
            Div('sales',css_class='col-md-4'),
            Div('status',css_class='col-md-3'),
            Div('types',css_class='col-md-3'),
            Div('rate',css_class='col-md-3'),
            Div('PDs', css_class='col-md-3'),
            css_class='row-fluid'),
        Div(
            Div('currency_type',css_class='col-md-4'),
            Div('carrier',css_class='col-md-4'),
            Div('carrier_fee',css_class='col-md-4'),
            Div('flat_rate',css_class='col-md-4'),
            css_class='row-fluid carrier'
            ),
        Div(
            Div('driver',css_class='col-md-4'),
            Div('truck',css_class='col-md-4'),
            Div('trailer',css_class='col-md-4'),
            css_class='row-fluid driver'
            ),
            css_class='container-fluid first'),
            
        Div(
            Div(
            Div('shipper',css_class='col-md-3'),
            Div('location',css_class='col-md-3'),
            Div('ship_date',css_class='col-md-3'),
            Div('description',css_class='col-md-3'),
            Div('ship_type',css_class='col-md-3'),
            Div('ship_qty',css_class='col-md-3'),
            Div('ship_weight',css_class='col-md-3'),
            Div('ship_po',css_class='col-md-3'),
            Div('shipping_notes',css_class='col-md-3'),
            Div('custom_broker',css_class='col-md-3'),
            css_class='row-fluid'
            ),
            css_class='container-fluid first'),
            
            
        Div(
            Div(
            Div('consignee',css_class='col-md-3'),
            Div('c_location',css_class='col-md-3'),
            Div('c_date',css_class='col-md-3'),
            Div('c_description',css_class='col-md-3'),
            Div('c_type',css_class='col-md-3'),
            Div('c_qty',css_class='col-md-3'),
            Div('c_weight',css_class='col-md-3'),
            Div('c_po',css_class='col-md-3'),
            Div('delivery_notes',css_class='col-md-3'),
            css_class='row-fluid'
            ),
        css_class="container-fluid first"),
           
    Div(
            Div(
            Div('promiles',css_class='col-md-4'),
            Div('drivermiles',css_class='col-md-4'),
            css_class='row-fluid'
            ),
        css_class="container-fluid first"),
           
        )
    
    class Meta:
        model=LoadModels
        exclude=['usd']
        
    def __init__(self , *args, **kwargs):
        super(LoadForm, self).__init__(*args, **kwargs)
        self.fields['ship_date'].widget.attrs.update({'id':'datepicker20'})
        self.fields['c_date'].widget.attrs.update({'id':'datepicker19'})
        
class DriverForm(forms.ModelForm):
    

    
    class Meta:
        model= SingleDriver
        exclude=[]
        
    def __init__(self , *args, **kwargs):
        super(DriverForm, self).__init__(*args, **kwargs)
        self.fields['dob'].widget.attrs.update({'id':'datepicker'})
        self.fields['hire_date'].widget.attrs.update({'id':'datepicker1'})
        self.fields['last_medical'].widget.attrs.update({'id':'datepicker2'})
        self.fields['last_drug_test'].widget.attrs.update({'id':'datepicker3'})
        self.fields['next_drug_test'].widget.attrs.update({'id':'datepicker4'})
        self.fields['passport_expiry'].widget.attrs.update({'id':'datepicker5'})
        self.fields['license_expiry'].widget.attrs.update({'id':'datepicker6'})
        self.fields['fast_card_expiry'].widget.attrs.update({'id':'datepicker7'})
        self.fields['hazmat_expiry'].widget.attrs.update({'id':'datepicker8'})
        
class CustomerForm(forms.ModelForm):
    helper=FormHelper()
    helper.layout = Layout(
        Div(
        Div(
            Div('name',css_class='col-md-4'),
            Div('customer_id',css_class='col-md-4'),
            Div('address1',css_class='col-md-4'),
            Div('address2', css_class='col-md-3'),
            Div('address3', css_class='col-md-3'),
            Div('country', css_class='col-md-3'),
            Div('state', css_class='col-md-3'),
            Div('city', css_class='col-md-3'),
            Div('bill_address1', css_class='col-md-3'),
            Div('bill_address2', css_class='col-md-3'),
            Div('bill_address3', css_class='col-md-3'),
            Div('bill_country', css_class='col-md-3'),
            Div('bill_state', css_class='col-md-3'),
            Div('bill_city', css_class='col-md-3'),
            Div('primary_contact', css_class='col-md-3'),
            Div('telephone', css_class='col-md-3'),
            Div('telephone_ext',css_class='col-md-3'),
            Div('email',css_class='col-md-3'),  
            Div('toll_free', css_class='col-md-3'),
            Div('secondary_contact', css_class='col-md-3'),
            Div('secondary_email', css_class='col-md-3'),
            Div('billing_email', css_class='col-md-3'),
            Div('bill_telephone', css_class='col-md-3'),
            Div('bill_ext',css_class='col-md-4'),
            css_class='row-fluid'),
            Div(
             Div('advanced_internal',css_class='col-md-12')
                ,css_class='row-fluid'
            ),
            css_class='container-fluid first'),
        )
    class Meta:
        model= Customers
        exclude=[]
        
    def __init__(self , *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['advanced_internal'].widget.attrs.update({'id':'advance'})
        
class TruckForm(forms.ModelForm):
    helper=FormHelper()
    helper.layout = Layout(
        Div(
        Div(
            Div('truck_no',css_class='col-md-4'),
            Div('truck_type',css_class='col-md-4'),
            Div('license_plate',css_class='col-md-4'),
            Div('registered_state', css_class='col-md-3'),
            Div('insurance_no', css_class='col-md-3'),
            Div('gross_weight', css_class='col-md-3'),
            Div('vehicle_id', css_class='col-md-3'),
            Div('status', css_class='col-md-3'),
            Div('mileage', css_class='col-md-3'),
            Div('ownership', css_class='col-md-3'),
            Div('axles', css_class='col-md-3'),
            Div('fuel_type', css_class='col-md-3'),
            Div('plate_expiry',css_class='col-md-3'),
            Div('inspection_expiry',css_class='col-md-3'),  
            Div('deactivation', css_class='col-md-3'),
            Div('dot_expiry', css_class='col-md-3'),
            Div('internal_notes',css_class='col-md-4'),
            css_class='row-fluid'),
            css_class='container-fluid first'),
        )

    
    class Meta:
        model=Truck
        exclude=[]
        
    def __init__(self , *args, **kwargs):
        super(TruckForm, self).__init__(*args, **kwargs)
        self.fields['dot_expiry'].widget.attrs.update({'id':'datepicker9'})
        self.fields['start_date'].widget.attrs.update({'id':'datepicker10'})
        self.fields['plate_expiry'].widget.attrs.update({'id':'datepicker13'})
        self.fields['inspection_expiry'].widget.attrs.update({'id':'datepicker14'})
        self.fields['deactivation'].widget.attrs.update({'id':'datepicker15'})

class TrailerForm(forms.ModelForm):
    helper=FormHelper()
    helper.layout = Layout(
        Div(
        Div(
            Div('trailer_no',css_class='col-md-4'),
            Div('trailer_type',css_class='col-md-4'),
            Div('license_plate',css_class='col-md-4'),
            Div('registered_state', css_class='col-md-3'),
            Div('insurance_no', css_class='col-md-3'),
            Div('gross_weight', css_class='col-md-3'),
            Div('vehicle_id', css_class='col-md-3'),
            Div('status', css_class='col-md-3'),
            Div('mileage', css_class='col-md-3'),
            Div('ownership', css_class='col-md-3'),
            Div('axles', css_class='col-md-3'),
            Div('fuel_type', css_class='col-md-3'),
            Div('plate_expiry',css_class='col-md-3'),
            Div('inspection_expiry',css_class='col-md-3'),  
            Div('deactivation', css_class='col-md-3'),
            Div('dot_expiry', css_class='col-md-3'),
            Div('internal_notes',css_class='col-md-4'),
            css_class='row-fluid'),
            css_class='container-fluid first'),
        )
    
    class Meta:
        model=Trailer
        exclude=[]
    def __init__(self , *args, **kwargs):
        super(TrailerForm, self).__init__(*args, **kwargs)
        self.fields['dot_expiry'].widget.attrs.update({'id':'datepicker11'})
        self.fields['start_date'].widget.attrs.update({'id':'datepicker12'})
        self.fields['plate_expiry'].widget.attrs.update({'id':'datepicker16'})
        self.fields['inspection_expiry'].widget.attrs.update({'id':'datepicker17'})
        self.fields['deactivation'].widget.attrs.update({'id':'datepicker18'})
        