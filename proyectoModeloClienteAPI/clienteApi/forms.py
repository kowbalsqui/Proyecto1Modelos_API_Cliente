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
    nombre = forms.CharField(label='Nombre', max_length=100, required=False)
    activo = forms.BooleanField(label='Activo', required=False)
    puntuacion = forms.DecimalField(label='Puntuación', max_digits=3, decimal_places=1, required=False)

    