from django.shortcuts import render
import requests
from django.core import serializers
from django.conf import settings
import os
from dotenv import load_dotenv

# Cargar el archivo .env
load_dotenv()

# Create your views here.
def inicio (request):
    return render(request, 'Padre.html')

def pagina_de_enlaces(request):
    return render(request, 'enlaces.html')  

def tutorial_lista_apiProfesor(request):
    # Le damos permiso de autorizacion
    profesor = os.getenv('TEACHER_USER')
    headers_Profesor = {'Authorization': f'Bearer {profesor}'}
    # Obtenemos todos los tutoriales de la api primero
    response = requests.get('http://127.0.0.1:8000/api/v1/tutorial', headers=headers_Profesor)
    # Transformamos la respuesta en JSON
    tutoriales = response.json()
    return render(request, 'Tutorial/lista_tutorial_api.html', {
        "tutoriales_mostrar": tutoriales
    })

def tutorial_lista_apiAdmin(request):
    admin = os.getenv("ADMIN_USER")
    headers_Admin = {'Authorization' : f'Bearer {admin}'}
    # Obtenemos todos los tutoriales de la api primero
    response = requests.get('http://127.0.0.1:8000/api/v1/tutorial', headers=headers_Admin)
    # Transformamos la respuesta en JSON
    tutoriales = response.json()
    return render(request, 'Tutorial/lista_tutorial_api.html', {
        "tutoriales_mostrar": tutoriales
    })
    
<<<<<<< HEAD
def usuario_lista_api (request):
    #Le damos el permiso de autorizacion
    headers = {'Authorization': 'Bearer G8S54YVURkTo8oS9fp7VF9fVnYQpnU'}
    #Obtenemos todos los usuarios de la api
    response = requests.get('http://127.0.0.1:8000/api/v1/usuario', headers= headers)
    #Transformamos las repuesta
=======
def tutorial_lista_apiEstudiante(request):
    # Le damos permiso de autorizacion
    estudiante = os.getenv('STUDENT_USER')
    headers_Estudiante = {'Authorization' : f'Bearer{estudiante}'}
    # Obtenemos todos los tutoriales de la api primero
    response = requests.get('http://127.0.0.1:8000/api/v1/tutorial', headers=headers_Estudiante)
    # Transformamos la respuesta en JSON
    tutoriales = response.json()
    return render(request, 'Tutorial/lista_tutorial_api.html', {
        "tutoriales_mostrar": tutoriales
    })

def usuario_lista_api(request):
    # Le damos el permiso de autorizacion
    profesor = os.getenv('TEACHER_USER')
    headers_Profesor = {'Authorization': f'Bearer {profesor}'}
    # Obtenemos todos los usuarios de la api
    response = requests.get('http://127.0.0.1:8000/api/v1/usuario', headers=headers_Profesor)
    # Transformamos la respuesta en JSON
>>>>>>> b2dd90b870ddde5bcb1237e04dd1d56f38a7986e
    usuarios = response.json()
    return render(request, 'Usuario/lista_usuario_api.html', {
        'usuarios_mostrar': usuarios
    })

def cursos_lista_api(request):
    profesor = os.getenv('TEACHER_USER')
    headers = {'Authorization': f'Bearer {profesor}'}
    response = requests.get('http://127.0.0.1:8000/api/v1/usuario', headers=headers)
    cursos = response.json()
    return render(request, 'Cursos/lista_cursos_api.html', {
        'cursos_mostrar', cursos
    })
    