from django import forms
from AppProyecto.models import Trabajador, Genero

class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = ['rut', 'nombre', 'genero', 'direccion', 'telefono']
        widgets = {
            'rut': forms.TextInput(attrs={'placeholder': 'Ingrese RUT'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese Nombre'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Ingrese Dirección'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ingrese Teléfono'}),
        }

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese Nombre de Género'}),
        }
