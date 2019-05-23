from django.shortcuts import render, redirect
from  .models import Vehicle, Manufacturer, Fuel
from .forms import VehicleForm, ManufacturerForm, FuelForm

# Create your views here.

def home(request):
    return render (request, 'home.html', {})

def vehicle_list(request):
    if (request.method == 'POST'):
        form = request.POST.get('select')
        vehicles = Vehicle.objects.all().order_by(form)
        return render(request, 'cars/list.html', {'vehicles':vehicles})
    else:
        vehicles = Vehicle.objects.all()
        return render(request, 'cars/list.html', {'vehicles':vehicles})       
def vehicle_show(request, vehicle_id):
    vehicle = Vehicle.objects.get(pk = vehicle_id)
    return render(request, 'cars/show.html', {'vehicle': vehicle})
def vehicle_form (request):
    
    if(request.method == 'POST'):
        form = VehicleForm(request.POST)
        form.save()
        return redirect('/cars/cars/')

    else:    
        form = VehicleForm()
        return render (request, 'cars/form.html',{'form':form})
def vehicle_edit (request, vehicle_id):
    if (request.method == 'POST'):
        vehicle = Vehicle.objects.get(pk=vehicle_id)
        form = VehicleForm(request.POST, instance = vehicle)
        if (form.is_valid):
            form.save()
            return redirect ('/cars/cars/')
        else:
            return render(request, 'cars/edit.html', {'form':form, 'vehicle_id': vehicle_id})
    else:
        vehicle = Vehicle.objects.get(pk=vehicle_id)
        form = VehicleForm(instance = vehicle)
        return render (request, 'cars/edit.html',{'form':form, 'vehicle_id': vehicle_id})
def vehicle_delete (request, vehicle_id):
    vehicle = Vehicle.objects.get(pk= vehicle_id)
    vehicle.delete()
    return redirect('/cars/cars/')


def manufacturer_list(request):
    manufacturer = Manufacturer.objects.all()
    return render(request, 'manufacturer/list.html', {'manufacturer': manufacturer})
def manufacturer_show(request, manufacturer_id):
    manufacturer = Manufacturer.objects.get(pk = manufacturer_id)
    return render(request, 'manufacturer/show.html', {'manufacturer': manufacturer})
def manufacturer_form (request):
    if(request.method == 'POST'):
        form = ManufacturerForm(request.POST)
        form.save()
        return redirect('/cars/manufacturer/')
    else:    
        form = ManufacturerForm()
        return render (request, 'manufacturer/form.html',{'form':form})
def manufacturer_edit (request, manufacturer_id):
    if (request.method == 'POST'):
        manufacturer = Manufacturer.objects.get(pk=manufacturer_id)
        form = ManufacturerForm(request.POST, instance = Manufacturer)
        if (form.is_valid):
            form.save()
            return redirect ('/cars/manufacturer/')
        else:
            return render(request, 'manufacturer/edit.html', {'form':form, 'manufacturer_id': manufacturer_id})
    else:
        manufacturer = Manufacturer.objects.get(pk=manufacturer_id)
        form = ManufacturerForm(instance = manufacturer)
        return render (request, 'manufacturer/edit.html',{'form':form, 'manufacturer_id': manufacturer_id})
def manufacturer_delete (request, manufacturer_id):
    manufacturer = Manufacturer.objects.get(pk= manufacturer_id)
    manufacturer.delete()
    return redirect('/cars/manufacturer/')


def fuel_list(request):
    fuel = Fuel.objects.all()
    return render(request, 'fuel/list.html', {'fuel': fuel})
def fuel_show(request, manufacturer_id):
    fuel = Fuel.objects.get(pk = fuel_id)
    return render(request, 'fuel/show.html', {'fuel': fuel })
def fuel_form (request):
    if(request.method == 'POST'):
        form = FuelForm(request.POST)
        form.save()
        return redirect('/cars/fuel/')
    else:    
        form = FuelForm()
        return render (request, 'fuel/form.html',{'form':form})
def fuel_edit (request, fuel_id):
    if (request.method == 'POST'):
        fuel = Fuel.objects.get(pk=fuel_id)
        form = FuelForm(request.POST, instance = Fuel)
        if (form.is_valid):
            form.save()
            return redirect ('/cars/fuel/')
        else:
            return render(request, 'fuel/edit.html', {'form':form, 'fuel_id': fuel_id})
    else:
        fuel = Fuel.objects.get(pk=fuel_id)
        form = FuelForm(instance = fuel)
        return render (request, 'fuel/edit.html',{'form':form, 'fuel_id': fuel_id})
def fuel_delete (request, fuel_id):
    fuel = Fuel.objects.get(pk= fuel_id)
    fuel.delete()
    return redirect('/cars/fuel/')