from django import forms
from .models import Ubicaciones, Dispositivos, Traslados

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicaciones
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Oficina Central'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción de la ubicación'}),
        }

class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivos
        fields = ['nombre', 'tipo', 'marca', 'modelo', 'n_serie', 'estado', 'id_ubi']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: PC Oficina 1'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Dell, HP'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Optiplex 7070'}),
            'n_serie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de serie'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'id_ubi': forms.Select(attrs={'class': 'form-control'}),
        }

class TrasladoForm(forms.ModelForm):
    class Meta:
        model = Traslados
        fields = ['id_dis', 'id_ubi', 'responsable']
        widgets = {
            'id_dis': forms.Select(attrs={'class': 'form-control'}),
            'id_ubi': forms.Select(attrs={'class': 'form-control'}),
            'responsable': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Persona responsable del traslado'}),
        }
