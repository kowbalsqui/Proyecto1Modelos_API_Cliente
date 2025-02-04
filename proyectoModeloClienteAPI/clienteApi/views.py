from django.shortcuts import render,redirect
import requests
from django.http import HttpResponseRedirect
from django.core import serializers
from django.conf import settings
import os
from requests.exceptions import HTTPError
from dotenv import load_dotenv
from .forms import *

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
    response = requests.get('http://potito.pythonanywhere.com/api/v1/tutorial', headers=headers_Profesor)
    # Transformamos la respuesta en JSON
    tutoriales = response.json()
    return render(request, 'Tutorial/lista_tutorial_api.html', {
        "tutoriales_mostrar": tutoriales
    })

def tutorial_lista_apiAdmin(request):
    admin = os.getenv("ADMIN_USER")
    headers_Admin = {'Authorization' : f'Bearer {admin}'}
    # Obtenemos todos los tutoriales de la api primero
    response = requests.get('http://potito.pythonanywhere.com/api/v1/tutorial', headers=headers_Admin)
    # Transformamos la respuesta en JSON
    tutoriales = response.json()
    return render(request, 'Tutorial/lista_tutorial_api.html', {
        "tutoriales_mostrar": tutoriales
    })
    
def usuario_lista_api (request):
    #Le damos el permiso de autorizacion
    headers = {'Authorization': 'Bearer G8S54YVURkTo8oS9fp7VF9fVnYQpnU'}
    #Obtenemos todos los usuarios de la api
    response = requests.get('http://potito.pythonanywhere.com/api/v1/usuario', headers= headers)
    #Transformamos las repuesta

def tutorial_lista_apiEstudiante(request):
    # Le damos permiso de autorizacion
    estudiante = os.getenv('STUDENT_USER')
    headers_Estudiante = {'Authorization' : f'Bearer {estudiante}'}
    # Obtenemos todos los tutoriales de la api primero
    response = requests.get('http://potito.pythonanywhere.com/api/v1/tutorial', headers=headers_Estudiante)
    # Transformamos la respuesta en JSON
    tutoriales = response.json()
    return render(request, 'Tutorial/lista_tutorial_api.html', {
        "tutoriales_mostrar": tutoriales
    })

def usuario_lista_api(request):
    # Le damos el permiso de autorizacion
    headers_Profesor = {'Authorization': 'Bearer OGIxoAZTgOaPKtk0zU3O5Kt929il3l'}
    # Obtenemos todos los usuarios de la api
    response = requests.get('http://127.0.0.1:8000/api/v1/usuario', headers=headers_Profesor)
    # Transformamos la respuesta en JSON
    usuarios = response.json()
    return render(request, 'Usuario/lista_usuario_api.html', {
        'usuarios_mostrar': usuarios
    })

def cursos_lista_api(request):
    profesor = os.getenv('TEACHER_USER')
    headers = {'Authorization': f'Bearer {profesor}'}
    response = requests.get('http://potito.pythonanywhere.com/api/v1/cursos', headers=headers)
    cursos = response.json()
    return render(request, 'Cursos/lista_cursos_api.html', {
        'cursos_mostrar': cursos
    })

def categoria_lista_api(request):
    profesor = os.getenv('TEACHER_USER')
    headers = {'Authorization': f'Bearer {profesor}'}
    response = requests.get('http://potito.pythonanywhere.com/api/v1/categoria', headers=headers)
    categorias = response.json()
    return render(request, 'Categorias/lista_categorias_api.html', {
        'categorias_mostrar': categorias
    })

def etiquetas_lista_api(request):
    profesor = os.getenv('TEACHER_USER')
    headers = {'Authorization': f'Bearer {profesor}'}
    response = requests.get('http://potito.pythonanywhere.com/api/v1/etiqueta', headers=headers)
    etiquetas = response.json()
    return render(request, 'Etiquetas/lista_etiquetas_api.html', {
        'etiquetas_mostrar': etiquetas
    })

# Vista de los formularios de busqueda basicos

def crear_cabezera():
    return {'Authorization': 'Bearer OGIxoAZTgOaPKtk0zU3O5Kt929il3l'}

def busqueda_usuario_simple_api(request):
    if len(request.GET) > 0:
        print("Datos recibidos en request.GET:", request.GET)  # Depuración
        formulario = BusquedaUsuarioForm(request.GET)

        if formulario.is_valid():
            headers = {'Authorization': 'Bearer OGIxoAZTgOaPKtk0zU3O5Kt929il3l'}
            response = requests.get('http://127.0.0.1:8000/api/v1/usuario', 
                                    headers=headers,
                                    params=formulario.cleaned_data)
            usuarios = response.json()
            return render(request, 'Usuario/busqueda_usuario_simple_api.html', {"usuarios_mostrar": usuarios})
        else:
            print("Errores del formulario:", formulario.errors)  # Depuración
            referer = request.META.get("HTTP_REFERER")
            if referer:
                return HttpResponseRedirect(referer)
            else:
                return redirect('inicio')
    else:
        formulario = BusquedaUsuarioForm(None)
        return render(request, 'Usuario/busqueda_usuario_simple_api.html', {"formulario": formulario})

# Vista de los formularios de busqueda avanzados

def busqueda_usuario_avanzado_api(request):
    if len(request.GET) > 0:
        print("Datos recibidos en request.GET:", request.GET)  # Depuración
        formulario = BusquedaUsuarioAvanzadoForm(request.GET)
        
        if formulario.is_valid():
            try:
                headers = {'Authorization': 'Bearer OGIxoAZTgOaPKtk0zU3O5Kt929il3l'}
                print("Datos enviados en params:", formulario.cleaned_data)  # Depuración
                
                response = requests.get(
                    'http://127.0.0.1:8000/api/v1/usuario', 
                    headers=headers,
                    params=formulario.cleaned_data
                )

                if (response.status_code == requests.codes.ok):
                    usuarios = response.json()
                    return render(request, 'Usuario/busqueda_usuario_avanzada_api.html', {"usuarios_mostrar": usuarios})
                else:
                    print("Error de estado:", response.status_code)
                    response.raise_for_status()

            except HTTPError as http_err:
                print(f'Hubo un error en la petición: {http_err}')
                if response.status_code == 400:
                    errores = response.json()
                    for error in errores:
                        formulario.add_error(error, errores[error])
                    return render(request, 'Usuario/busqueda_usuario_avanzada_api.html', {"formulario": formulario, "errores": errores})
                else:
                    return mi_error_500(request)
            except Exception as err:
                print(f'Ocurrió un error: {err}')
                return mi_error_500(request)
        else:
            print("Errores del formulario:", formulario.errors)  # Depuración
    else:
        formulario = BusquedaUsuarioAvanzadoForm(None)

    return render(request, 'Usuario/busqueda_usuario_avanzada_api.html', {"formulario": formulario})
   
   
   #Errores
   
def mi_error_500(request,exception=None):
    return render(request, 'errores/500.html',None,None,500)