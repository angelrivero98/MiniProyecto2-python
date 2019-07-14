from django import forms
from tesis.models import Usuario, Autor, Tesis


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
            'rol': forms.Select(attrs={'class': 'form-control'})
        }


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ('nombre','apellido',)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
        }


class FormInicio(forms.Form):
    search = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Buscar tesis'})
    )

class TesisForm(forms.Form):
    class Meta:
        model = Tesis
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
            'rol': forms.Select(attrs={'class': 'form-control'})
        }
