from django.shortcuts import render
import requests
from django.core import serializers

# Create your views here.
def inicio (request):
    return render(request, 'Padre.html')

def pagina_de_enlaces(request):
    return render(request, 'enlaces.html')  

def tutorial_lista_api (request):
    #Obtenemos todos los tutoriales de la api primero
    response = requests.get('http://127.0.0.1:8000/api/v1/tutorial')
    #Transformamos la repsuesta en JSON
    tutoriales = response.json()
    return render(request, 'Tutorial/lista_tutorial_api.html', {
        "tutoriales_mostrar": tutoriales
    })