from django import forms
from datetime import datetime
from django.forms import ModelForm
from .models import *
from django.utils.timezone import now
from datetime import date, timedelta
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BusquedaUsuarioForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico', max_length=100)
    
class BusquedaUsuarioAvanzadoForm(forms.Form):
    puntuacion = forms.DecimalField(
        max_digits=3, 
        decimal_places=1, 
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 5.0'
        })
    )
    es_activo = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        })
    )
    fecha_Registro = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
        })
    )
class BusquedaTutorialAvanzadoForm(forms.Form):
    visitas = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 1'
        })
    )
    valoracion = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 1'
        })
    )
    titulo = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: Python'
        })
    )

class BusquedaPerfilAvanzadoForm (forms.Form):
    fecha_Nacimiento = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
        })
    )

    REDES = [
        ("IG", "Instagram"),
        ("FB", "Facebook"),
        ("TW", "Twitter"),
        ("LI", "LinkedIn"),
    ]

    redes = forms.ChoiceField(
        choices=REDES,  
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    estudios = forms.CharField(
        max_length=100, 
        required=False, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: Estudios superiores',
        })
    )

class BusquedaComentarioAvanzadoForm(forms.Form):
    contenido = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contenido...',
        })
    )
    visible = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        })
    )
    puntuacion = forms.DecimalField(
        max_digits=3,
        decimal_places=1,
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 5.0',
        })
    )