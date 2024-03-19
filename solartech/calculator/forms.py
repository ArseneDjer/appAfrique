# calculator/forms.py
from django import forms
from .models import SolarSystem

class SolarSystemForm(forms.ModelForm):
    class Meta:
        model = SolarSystem
        fields = ['location', 'daily_energy_consumption', 'sunlight_hours', 'panel_efficiency', 'inverter_efficiency', 'battery_capacity', 'electronic_devices', 'number_of_bulbs']
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'daily_energy_consumption': forms.NumberInput(attrs={'class': 'form-control'}),
            'sunlight_hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'panel_efficiency': forms.NumberInput(attrs={'class': 'form-control'}),
            'inverter_efficiency': forms.NumberInput(attrs={'class': 'form-control'}),
            'battery_capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'electronic_devices': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'number_of_bulbs': forms.NumberInput(attrs={'class': 'form-control'}),
        }
