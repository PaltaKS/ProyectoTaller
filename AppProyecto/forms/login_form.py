from django import forms

class LoginForm(forms.Form):
    nombre_usuario = forms.CharField(max_length=150)
    contrasena = forms.CharField(widget=forms.PasswordInput)


