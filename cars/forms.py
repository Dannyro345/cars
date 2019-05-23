from django.forms import ModelForm, TextInput, Select
from .models import Vehicle, Manufacturer, Fuel


class VehicleForm(ModelForm):
    class Meta:    
        model = Vehicle
        fields = '__all__'
        widgets = {
            'model': TextInput(attrs={'class':'form-control'}),
            'color': TextInput(attrs={'class':'form-control'}),
            'board': TextInput(attrs={'class':'form-control'}),
            'chassis': TextInput(attrs={'class':'form-control'}),
            'year': TextInput(attrs={'class':'form-control'}),
            'manufacturer': Select(attrs={'class': 'form-control'}),
            'fuel': Select(attrs={'class': 'form-control'})
        }

class ManufacturerForm(ModelForm):
    class Meta:    
        model = Manufacturer
        fields = '__all__'
        widgets = {
            'brand': TextInput(attrs={'class':'form-control'}),
            'country': TextInput(attrs={'class':'form-control'}),

        }

class FuelForm(ModelForm):
    class Meta:    
        model = Fuel
        fields = '__all__'
        widgets = {
            'type_fuel': TextInput(attrs={'class':'form-control'})
        }