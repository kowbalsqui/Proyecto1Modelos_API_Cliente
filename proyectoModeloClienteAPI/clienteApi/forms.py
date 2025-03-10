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
from .helper import helper


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
    nombre = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: Nombre..'
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

class Create_usuario(forms.Form):
    nombre = forms.CharField(
        required= True,
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contenido...',
        })
    )
    
    email = forms.CharField(
        required= True,
        max_length=20,
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email' 
        })
    )
    puntuacion = forms.DecimalField(
        max_digits=3, 
        decimal_places=1, 
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 5.0'
        })
    )
    es_activo = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        })
    )
    fecha_Registro = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
        })
    )

class NombreUsuarioForm(forms.Form):
    nombre = forms.CharField(
        required= True,
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre...',
        })
    )

class TituloTutorialForm(forms.Form):
    titulo = forms.CharField(
        required= True,
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'titulo...',
        })
    )

class EtiquetaNombreForm(forms.Form):
    nombre = forms.CharField(
        required= True,
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre...',
        })
    )

class CursoNombreForm(forms.Form):
    nombre = forms.CharField(
        required= True,
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre...',
        })
    )

class Create_tutorial(forms.Form):
    titulo = forms.CharField(
        required= True,
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'titulo...',
        })
    )
    contenido = forms.CharField(
        required= True,
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contenido...',
        })
    )
    fecha_Creacion = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
        })
    )
    visitas = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 1'
        })
    )

    valoracion = forms.DecimalField(
        max_digits=3, 
        decimal_places=1, 
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 5.0'
        })
    )

    def __init__(self, *args, **kwargs):

        self.request = kwargs.pop('request', None)
        
        super(Create_tutorial, self).__init__(*args, **kwargs)

        usuarios_disponibles = helper.obtener_usuario_selec(self.request)
        self.fields['usuario'] = forms.ChoiceField(
            choices= usuarios_disponibles, 
            widget= forms.Select,
            required= True,
        )

class Create_etiqueta(forms.Form):
    nombre = forms.CharField(
        required=True,
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre de la etiqueta...',
        })
    )
    color = forms.CharField(
        required=True,
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Color de la etiqueta...',
        })
    )
    publica = forms.BooleanField(
         widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        })
    )
    descripcion = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Descripción...',
        })
    )

    def __init__(self, *args, **kwargs):

        self.request = kwargs.pop('request', None)
        
        super(Create_etiqueta, self).__init__(*args, **kwargs)

        tutoriales_disponibles = helper.obtener_tutorial_selec(self.request)
        self.fields['tutorial'] = forms.ChoiceField(
            choices= tutoriales_disponibles, 
            widget= forms.Select,
            required= True,
        )

class Create_cursos(forms.Form):
    nombre = forms.CharField(
        required=True,
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre del curso...',
        })
    )
    horas = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 10h'
        })
    )

    precio = forms.DecimalField(
        max_digits=5, 
        decimal_places=2,  # ⬅️ Permite 2 decimales sin validación extra.
        min_value=0,  # ⬅️ Solo evita valores negativos.
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio...'})
    )
    
    descripcion = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Descripción...',
        })
    )

    def __init__(self, *args, **kwargs):

        self.request = kwargs.pop('request', None)
        
        super(Create_cursos, self).__init__(*args, **kwargs)

        usuarios_disponibles = helper.obtener_usuario_selec(self.request)
        self.fields['usuario'] = forms.ChoiceField(
            choices= usuarios_disponibles, 
            widget= forms.Select,
            required= True,
        )

from django.contrib.auth import get_user_model
User = get_user_model()
        
class RegistroForm(UserCreationForm):
    roles= (
        (2, 'Profesor'),
        (3, 'Estudiante'),
    )
    
    nombre = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    rol = forms.ChoiceField(choices=roles, required=True, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['nombre', 'email', 'password1', 'password2', 'rol']

        
class LoginForm(forms.Form):
    usuario = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class CreateTutorialForm(forms.Form):
    titulo = forms.CharField(
        required= True,
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'titulo...',
        })
    )
    contenido = forms.CharField(
        required= True,
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contenido...',
        })
    )
    fecha_Creacion = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
        })
    )
    visitas = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 1'
        })
    )

    valoracion = forms.DecimalField(
        max_digits=3, 
        decimal_places=1, 
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 5.0'
        })
    )

class CreateCourseForm(forms.Form):
    nombre = forms.CharField(
        required=True,
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre del curso...',
        })
    )
    horas = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 10h'
        })
    )

    precio = forms.DecimalField(
        max_digits=5, 
        decimal_places=2,  # ⬅️ Permite 2 decimales sin validación extra.
        min_value=0,  # ⬅️ Solo evita valores negativos.
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio...'})
    )
    
    descripcion = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Descripción...',
        })
    )
