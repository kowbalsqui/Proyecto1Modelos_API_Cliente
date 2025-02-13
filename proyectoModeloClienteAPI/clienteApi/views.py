from django.shortcuts import render,redirect
import requests
from django.http import HttpResponseRedirect
from django.core import serializers
from django.conf import settings
import os
from requests.exceptions import HTTPError
from dotenv import load_dotenv
from .forms import *
import json

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
    profesor = os.getenv('TEACHER_USER')
    # Le damos el permiso de autorizacion
    headers_Profesor = {'Authorization': f'Bearer {profesor}'}
    # Obtenemos todos los usuarios de la api
    response = requests.get('http://127.0.0.1:8092/api/v1/usuario', headers=headers_Profesor)
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

import xml.etree.ElementTree as ET

def parse_response(response):
    """Parsea la respuesta según el tipo de contenido."""
    content_type = response.headers.get("Content-Type", "")

    if "application/json" in content_type:
        return response.json()
    elif "application/xml" in content_type or "text/xml" in content_type:
        return ET.fromstring(response.text)  # Convierte XML en un árbol de elementos
    else:
        return response.text  # Devuelve texto sin procesar si no se reconoce el formato

def etiquetas_lista_api(request):
    profesor = os.getenv('TEACHER_USER')
    headers = {'Authorization': f'Bearer {profesor}'}
    
    response = requests.get('http://potito.pythonanywhere.com/api/v1/etiqueta', headers=headers)
    
    etiquetas = parse_response(response)  # Usa la función dentro de la vista

    return render(request, 'Etiquetas/lista_etiquetas_api.html', {
        'etiquetas_mostrar': etiquetas
    })

# Vista de los formularios de busqueda basicos

def crear_cabezera():
    return {'Authorization': 'Bearer FZ6oExxJOhtg5cHiiTrbRFPOuL3jh8'}

def busqueda_usuario_simple_api(request):
    profesor = os.getenv('TEACHER_USER')
    if len(request.GET) > 0:
        print("Datos recibidos en request.GET:", request.GET)  # Depuración
        formulario = BusquedaUsuarioForm(request.GET)

        if formulario.is_valid():
            headers = {'Authorization': f'Bearer {profesor}'}
            response = requests.get('http://potito.pythonanywhere.com/api/v1/usuario', 
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

import os
import requests
from requests.exceptions import HTTPError
from django.shortcuts import render
from .forms import BusquedaUsuarioAvanzadoForm

def busqueda_usuario_avanzado_api(request):
    url = os.getenv('URLANYWHERE')
    profesor = os.getenv('TEACHER_USER')
    errores = None  # Inicializamos errores como None

    if len(request.GET) > 0:
        print("Datos recibidos en request.GET:", request.GET)  # Depuración
        formulario = BusquedaUsuarioAvanzadoForm(request.GET)
        
        if formulario.is_valid():
            try:
                headers = {'Authorization': f'Bearer {profesor}'}
                print("Datos enviados en params:", formulario.cleaned_data)  # Depuración
                
                response = requests.get(
                    f'{url}usuario/busqueda_avanzada_usuario', 
                    headers=headers,
                    params=formulario.cleaned_data
                )

                if response.status_code == 200:
                    usuarios = response.json()
                    return render(request, 'Usuario/busqueda_usuario_avanzada_api.html', {
                        "usuarios_mostrar": usuarios,
                        "formulario": formulario,
                        "errores": errores
                    })
                else:
                    errores = response.json()  # Capturar errores devueltos por la API
                    print("Errores recibidos del servidor:", errores)
            
            except HTTPError as http_err:
                print(f'Hubo un error en la petición: {http_err}')
                errores = {"error": "Error en la comunicación con el servidor."}

            except Exception as err:
                print(f'Ocurrió un error inesperado: {err}')
                errores = {"error": "Ocurrió un error inesperado. Inténtalo más tarde."}

        else:
            errores = formulario.errors
            print("Errores del formulario en el cliente:", errores)  # Depuración

    else:
        formulario = BusquedaUsuarioAvanzadoForm(None)

    return render(request, 'Usuario/busqueda_usuario_avanzada_api.html', {
        "formulario": formulario,
        "errores": errores
    })


import logging

logger = logging.getLogger(__name__)  # Configurar logs

def busqueda_tutorial_avanzado_api(request):
    profesor = os.getenv('TEACHER_USER')
    errores = None  # Inicializar errores

    if len(request.GET) > 0:
        logger.info("Datos recibidos en request.GET: %s", request.GET)  # Log de depuración
        formulario = BusquedaTutorialAvanzadoForm(request.GET)

        if formulario.is_valid():
            try:
                headers = {'Authorization': f'Bearer {profesor}'}
                logger.info("Datos enviados en params: %s", formulario.cleaned_data)  # Log de depuración
                
                response = requests.get(
                    'http://potito.pythonanywhere.com/api/v1/tutorial/busqueda_avanzada_tutorial', 
                    headers=headers,
                    params=formulario.cleaned_data
                )

                if response.status_code == requests.codes.ok:
                    tutoriales = response.json()
                    return render(request, 'Tutorial/busqueda_tutorial_avanzada_api.html', {
                        "tutorial_mostrar": tutoriales,
                        "formulario": formulario,
                        "errores": errores
                    })
                else:
                    errores = response.json()  # Capturar errores devueltos por la API
                    logger.warning("Errores recibidos del servidor: %s", errores)

            except HTTPError as http_err:
                logger.error("Error HTTP en la petición: %s", http_err)
                errores = {"error": f"Error en la comunicación con el servidor: {http_err}"}

            except Exception as err:
                logger.error("Ocurrió un error inesperado: %s", err)
                errores = {"error": "Ocurrió un error inesperado. Inténtalo más tarde."}

        else:
            errores = formulario.errors
            logger.warning("Errores del formulario en el cliente: %s", errores)  # Log de depuración
    else:
        formulario = BusquedaTutorialAvanzadoForm(None)

    return render(request, 'Tutorial/busqueda_tutorial_avanzada_api.html', {
        "formulario": formulario,
        "errores": errores
    })

def busqueda_perfil_avanzado_api(request):
    profesor = os.getenv('TEACHER_USER')
    errores = None  # Inicializar errores

    if len(request.GET) > 0:
        logger.info("Datos recibidos en request.GET: %s", request.GET)  # Log de depuración
        formulario = BusquedaPerfilAvanzadoForm(request.GET)

        if formulario.is_valid():
            try:
                headers = {'Authorization': f'Bearer {profesor}'}
                logger.info("Datos enviados en params: %s", formulario.cleaned_data)  # Log de depuración
                
                response = requests.get(
                    'http://potito.pythonanywhere.com/api/v1/perfil/busqueda_avanzda_perfil', 
                    headers=headers,
                    params=formulario.cleaned_data
                )

                if response.status_code == requests.codes.ok:
                    perfil = response.json()
                    return render(request, 'Perfil/busqueda_perfil_avanzada_api.html', {
                        "perfil_mostrar": perfil,
                        "formulario": formulario,
                        "errores": errores
                    })
                else:
                    errores = response.json()  # Capturar errores devueltos por la API
                    logger.warning("Errores recibidos del servidor: %s", errores)

            except HTTPError as http_err:
                logger.error("Error HTTP en la petición: %s", http_err)
                errores = {"error": f"Error en la comunicación con el servidor: {http_err}"}

            except Exception as err:
                logger.error("Ocurrió un error inesperado: %s", err)
                errores = {"error": "Ocurrió un error inesperado. Inténtalo más tarde."}

        else:
            errores = formulario.errors
            logger.warning("Errores del formulario en el cliente: %s", errores)  # Log de depuración
    else:
        formulario = BusquedaPerfilAvanzadoForm(None)

    return render(request, 'Perfil/busqueda_perfil_avanzada_api.html', {
        "formulario": formulario,
        "errores": errores
    })

def busqueda_comentario_avanzado_api(request):
    profesor = os.getenv('TEACHER_USER')
    errores = None  # Variable para capturar errores

    if len(request.GET) > 0:
        print("Datos recibidos en request.GET:", request.GET)  # Depuración
        formulario = BusquedaComentarioAvanzadoForm(request.GET)
        
        if formulario.is_valid():
            try:
                headers = {'Authorization': f'Bearer {profesor}'}
                print("Datos enviados en params:", formulario.cleaned_data)  # Depuración
                
                response = requests.get(
                    'http://potito.pythonanywhere.com/api/v1/comentario/busqueda_avanzada_comentario', 
                    headers=headers,
                    params=formulario.cleaned_data
                )

                if response.status_code == requests.codes.ok:
                    comentarios = response.json()
                    return render(request, 'Comentario/busqueda_comentario_avanzada_api.html', {
                        "comentario_mostrar": comentarios,
                        "formulario": formulario,
                        "errores": errores
                    })
                else:
                    errores = response.json()  # Capturar errores devueltos por la API
                    print("Errores recibidos del servidor:", errores)

            except HTTPError as http_err:
                print(f'Error HTTP en la petición: {http_err}')
                errores = {"error": f"Error en la comunicación con el servidor: {http_err}"}

            except Exception as err:
                print(f'Ocurrió un error inesperado: {err}')
                errores = {"error": "Ocurrió un error inesperado. Inténtalo más tarde."}

        else:
            errores = formulario.errors
            print("Errores del formulario en el cliente:", errores)  # Depuración
    else:
        formulario = BusquedaComentarioAvanzadoForm(None)

    return render(request, 'Comentario/busqueda_comentario_avanzada_api.html', {
        "formulario": formulario,
        "errores": errores
    })


   #Errores
   
def mi_error_500(request,exception=None):
    return render(request, 'errores/500.html',None,None,500)

#Crear en la API

def crear_usuario_api (request):
    profesor = os.getenv('TEACHER_USER')
    if (request.method == 'POST'):
        try:
            formulario = Create_usuario(request.POST)
            headers = {
                'Authorization': f'Bearer {profesor}',
                'Content-Type': 'application/json'
            }
            datos = formulario.data.copy()
            datos["fecha_Registro"] = str(
                datetime.date(year= int(datos['fecha_Registro_year']),
                            month= int(datos['fecha_Registro_month']),
                            day= int(datos['fecha_Registro_day']))
            )
            response = request.post(
                'http://127.0.0.1:8092/api/v1/usuario/crear_usuario_api',
                headers= headers,
                data = json.dumps(datos)
            )
            if(response.status_code == requests.codes.ok):
                return redirect('listar_usuarios_api')
            else: 
                print(response.status_code)
                response.raise_for_status()
        except HTTPError as http_err:
            print(f'Hubo un error en la petición: {http_err}')
            if(response.status_code == 400):
                errores = response.json()
                for error in errores:
                    formulario.add_error(error,errores[error])
                return render(request, 
                            'Usuario/crear_usuario_api.html',
                            {"formulario":formulario})
            else:
                return mi_error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)
            
    else:
            formulario = Create_usuario(None)
    return render(request, 'Usuario/crear_usuario_api.html',{"formulario":formulario})