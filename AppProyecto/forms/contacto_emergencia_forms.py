from django import forms
from AppProyecto.models import ContactoEmergencia

class ContactoEmergenciaForm(forms.ModelForm):
    class Meta:
        model = ContactoEmergencia
        fields = ['trabajador', 'nombre', 'relacion', 'telefono']
