from django import forms
from .models import OfertaLaboral
from .models import Campania

class OfertaLaboralForm(forms.ModelForm):
    class Meta:
        model = OfertaLaboral
        fields = ['cargo', 'salario', 'ubicacion', 'critica']
        widgets = {
            'cargo': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. Desarrollador Backend'}),
            'salario': forms.NumberInput(attrs={'class': 'form-input'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-input'}),
            'critica': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }
        
# forms.py
class CampaniaForm(forms.ModelForm):
    class Meta:
        model = Campania
        fields = ['nombre', 'contenido', 'presupuesto', 'fecha_inicio', 'plataformas', 'OfertaLaboral']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'presupuesto': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'plataformas': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'OfertaLaboral': forms.Select(attrs={'class': 'form-select'}),
        }


