from django import forms
from AppProyecto.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre_usuario', 'contrasena', 'rol', 'trabajador']
        widgets = {
            'contrasena': forms.PasswordInput(render_value=True),
        }
