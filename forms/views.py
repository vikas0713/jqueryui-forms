from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from formsmodels.models import *
from formsmodels.forms import *



def index(request):
    c={}
    c.update(csrf(request))
    c['form']=LoadForm
    c['driverform']=DriverForm
    c['shipperform']=CustomerForm
    c['truckform']=TruckForm
    c['trailerform']=TrailerForm
    c['data']=LoadModels.objects.all()
    return render_to_response('index1.html',c)

def submit(request):
    if request.POST:
        val1=request.POST.get('rate')
        val2=request.POST.get('PDs')
        d=request.POST.get('ship_date')
        form=LoadForm(request.POST)
        if form.is_valid():
            form.save()
            obj=LoadModels.objects.get(ship_date=d)
            obj.usd=int(val1)+int(val2)
            obj.save()
            return HttpResponseRedirect('/')
        else:
            form=LoadForm()
    return HttpResponseRedirect('/')

def changed_status(request,lid):
    if request.POST:
        val=request.POST.get('status')
        if 'Delete' in val:
            try:
                LoadModels.objects.get(load=lid).delete()
            except:
                a=None
        else:
            try:
                b=LoadModels.objects.get(load=lid)
                b.status=val
                b.save()
            except:
                b=None
    return HttpResponseRedirect('/')
def submit_info(request,status):
    c={}
    if request.POST:
        if 'driver' in status:
            a=DriverForm(request.POST)
        if 'customer' in status:
            a=CustomerForm(request.POST)
        if 'truck' in status:
            a=TruckForm(request.POST)
        if 'trailer' in status:
            a=TrailerForm(request.POST)
        form=a
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else :
            c['errors']='Invalid Data in some of the fields'
            return render_to_response('invalid.html',c)
    c['errors']='Invalid Request'
    return render_to_response('invalid.html',c)  
def get_status(request,status):
    try:
        a=LoadModels.objects.filter(status=status)
    except:
        a=None
    c={}
    c['data']=a
    return render_to_response('invalid.html',c)
    
    
        

