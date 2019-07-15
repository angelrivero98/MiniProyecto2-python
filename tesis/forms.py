from django import forms
from tesis.models import Usuario, Autor, Tesis

#Los formularios asociados a la cracion de tesis, autor y usuario
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'required': False}),
            'rol': forms.Select(attrs={'class': 'form-control'})
        }


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
        }


class TesisForm(forms.ModelForm):
    class Meta:
        model = Tesis
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'resumen': forms.Textarea(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control datetimepicker-input', 'data-target': '#datetimepicker1', 'placeholder': 'Fecha', 'type': 'date'}),
            'calificacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'finalizada': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'escuela': forms.Select(attrs={'class': 'form-control'}),
            'palabrasclave': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'evaluadores': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'autores': forms.SelectMultiple(attrs={'class': 'form-control'})
        }
