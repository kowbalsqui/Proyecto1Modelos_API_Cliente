from django.shortcuts import render,redirect
import requests
from django.http import HttpResponseRedirect
from django.core import serializers
from django.conf import settings
from django.http import JsonResponse

import os
from requests.exceptions import HTTPError
from dotenv import load_dotenv
from .forms import *
import json
from .helper import helper
from .cliente_api import cliente_api
import urllib.parse
from django.contrib import messages


# Cargar el archivo .env
load_dotenv()

# Create your views here.
def inicio (request):
    return render(request, 'Padre.html')

def pagina_de_enlaces(request):
    return render(request, 'enlaces.html')  

def tutorial_lista_apiProfesor(request):
    token = request.session.get("token")  # 🔥 Obtener el token del usuario logueado
    
    if not token:
        return JsonResponse({"error": "No estás autenticado"}, status=401)
    # Le damos permiso de autorizacio
    headers_Profesor = {'Authorization': f'Bearer {token}'}
    # Obtenemos todos los tutoriales de la api primero
    response = requests.get('http://127.0.0.1:8092/api/v1/tutorial', headers=headers_Profesor)
    # Transformamos la respuesta en JSON
    tutoriales = response.json()
    print("✅ Datos recibidos de la API:", tutoriales) 
    return render(request, 'Tutorial/lista_tutorial_api.html', {
        "tutoriales_mostrar": tutoriales
    })

def tutorial_lista_apiAdmin(request):
    token = request.session.get("token")  # 🔥 Obtener el token del usuario logueado
    
    if not token:
        return JsonResponse({"error": "No estás autenticado"}, status=401)
    headers_Admin = {'Authorization' : f'Bearer {token}'}
    # Obtenemos todos los tutoriales de la api primero
    response = requests.get('http://127.0.0.1:8092/api/v1/tutorial', headers=headers_Admin)
    # Transformamos la respuesta en JSON
    tutoriales = response.json()
    return render(request, 'Tutorial/lista_tutorial_api.html', {
        "tutoriales_mostrar": tutoriales
    })
    
def usuario_lista_api (request):
    token = request.session.get("token")  # 🔥 Obtener el token del usuario logueado
    
    if not token:
        return JsonResponse({"error": "No estás autenticado"}, status=401)

    #Le damos el permiso de autorizacion
    headers = {'Authorization': 'Bearer {token}'}
    #Obtenemos todos los usuarios de la api
    response = requests.get("http://127.0.0.1:8092/api/v1/usuarios/", headers= headers)
    #Transformamos las repuesta

def tutorial_lista_apiEstudiante(request):
    token = request.session.get("token")  # 🔥 Obtener el token del usuario logueado
    
    if not token:
        return JsonResponse({"error": "No estás autenticado"}, status=401)
    # Le damos permiso de autorizacion
    estudiante = os.getenv('STUDENT_USER')
    headers_Estudiante = {'Authorization' : f'Bearer {token}'}
    # Obtenemos todos los tutoriales de la api primero
    response = requests.get('http://127.0.0.1:8092/api/v1/tutorial', headers=headers_Estudiante)
    # Transformamos la respuesta en JSON
    tutoriales = response.json()
    return render(request, 'Tutorial/lista_tutorial_api.html', {
        "tutoriales_mostrar": tutoriales
    })

def usuario_lista_api(request):
    token = request.session.get("token")  # 🔥 Obtener el token del usuario logueado
    
    if not token:
        return JsonResponse({"error": "No estás autenticado"}, status=401)
    # Le damos el permiso de autorizacion
    headers_Profesor = {'Authorization': f'Bearer {token}'}
    # Obtenemos todos los usuarios de la api
    response = requests.get('http://127.0.0.1:8092/api/v1/usuarios/', headers=headers_Profesor)
    # Transformamos la respuesta en JSON
    usuarios = response.json()
    return render(request, 'Usuario/lista_usuario_api.html', {
        'usuarios_mostrar': usuarios
    })

def cursos_lista_api(request):
    token = request.session.get("token")  # 🔥 Obtener el token del usuario logueado
    
    if not token:
        return JsonResponse({"error": "No estás autenticado"}, status=401)
    profesor = os.getenv('TEACHER_USER')
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get('http://127.0.0.1:8092/api/v1/cursos', headers=headers)
    cursos = response.json()
    return render(request, 'Cursos/lista_cursos_api.html', {
        'cursos_mostrar': cursos
    })

def categoria_lista_api(request):
    token = request.session.get("token")  # 🔥 Obtener el token del usuario logueado
    
    if not token:
        return JsonResponse({"error": "No estás autenticado"}, status=401)
    profesor = os.getenv('TEACHER_USER')
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get('http://127.0.0.1:8092/api/v1/categoria', headers=headers)
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
    token = request.session.get("token")  # 🔥 Obtener el token del usuario logueado
    
    if not token:
        return JsonResponse({"error": "No estás autenticado"}, status=401)
    profesor = os.getenv('TEACHER_USER')
    headers = {'Authorization': f'Bearer {token}'}
    
    response = requests.get('http://127.0.0.1:8092/api/v1/etiqueta', headers=headers)
    
    etiquetas = parse_response(response)  # Usa la función dentro de la vista

    return render(request, 'Etiquetas/lista_etiquetas_api.html', {
        'etiquetas_mostrar': etiquetas
    })

# Vista de los formularios de busqueda basicos

def crear_cabezera(request):
    token = request.session.get("token")  # 🔥 Obtener el token del usuario logueado
    
    if not token:
        return JsonResponse({"error": "No estás autenticado"}, status=401)
    profesor = os.getenv('TEACHER_USER')
    return {'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'}

def busqueda_usuario_simple_api(request):
    token = request.session.get("token")  # 🔥 Obtener el token del usuario logueado
    
    if not token:
        return JsonResponse({"error": "No estás autenticado"}, status=401)
    profesor = os.getenv('TEACHER_USER')
    if len(request.GET) > 0:
        print("Datos recibidos en request.GET:", request.GET)  # Depuración
        formulario = BusquedaUsuarioForm(request.GET)

        if formulario.is_valid():
            headers = {'Authorization': f'Bearer {token}'}
            response = requests.get('http://127.0.0.1:8092/api/v1/usuario', 
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
    token = request.session.get("token")  # 🔥 Obtener el token del usuario logueado
    
    if not token:
        return JsonResponse({"error": "No estás autenticado"}, status=401)
    url = os.getenv('URL')
    profesor = os.getenv('TEACHER_USER')
    errores = None  # Inicializamos errores como None

    if len(request.GET) > 0:
        print("Datos recibidos en request.GET:", request.GET)  # Depuración
        formulario = BusquedaUsuarioAvanzadoForm(request.GET)
        
        if formulario.is_valid():
            try:
                headers = {'Authorization': f'Bearer {token}'}
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
    token = request.session.get("token")  # 🔥 Obtener el token del usuario logueado
    
    if not token:
        return JsonResponse({"error": "No estás autenticado"}, status=401)
    
    profesor = os.getenv('TEACHER_USER')
    errores = None  # Inicializar errores

    if len(request.GET) > 0:
        logger.info("Datos recibidos en request.GET: %s", request.GET)  # Log de depuración
        formulario = BusquedaTutorialAvanzadoForm(request.GET)

        if formulario.is_valid():
            try:
                headers = {'Authorization': f'Bearer {token}'}
                logger.info("Datos enviados en params: %s", formulario.cleaned_data)  # Log de depuración
                
                response = requests.get(
                    'http://127.0.0.1:8092/api/v1/tutorial/busqueda_avanzada_tutorial', 
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

    token = request.session.get("token")  # 🔥 Obtener el token del usuario logueado
    
    if not token:
        return JsonResponse({"error": "No estás autenticado"}, status=401)
    profesor = os.getenv('TEACHER_USER')
    errores = None  # Inicializar errores

    if len(request.GET) > 0:
        logger.info("Datos recibidos en request.GET: %s", request.GET)  # Log de depuración
        formulario = BusquedaPerfilAvanzadoForm(request.GET)

        if formulario.is_valid():
            try:
                headers = {'Authorization': f'Bearer {token}'}
                logger.info("Datos enviados en params: %s", formulario.cleaned_data)  # Log de depuración
                
                response = requests.get(
                    'http://127.0.0.1:8092/api/v1/perfil/busqueda_avanzda_perfil', 
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

    token = request.session.get("token")  # 🔥 Obtener el token del usuario logueado
    
    if not token:
        return JsonResponse({"error": "No estás autenticado"}, status=401)
    
    profesor = os.getenv('TEACHER_USER')
    errores = None  # Variable para capturar errores

    if len(request.GET) > 0:
        print("Datos recibidos en request.GET:", request.GET)  # Depuración
        formulario = BusquedaComentarioAvanzadoForm(request.GET)
        
        if formulario.is_valid():
            try:
                headers = {'Authorization': f'Bearer {token}'}
                print("Datos enviados en params:", formulario.cleaned_data)  # Depuración
                
                response = requests.get(
                    'http://127.0.0.1:8092/api/v1/comentario/busqueda_avanzada_comentario', 
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

#GETS

from django.shortcuts import render, redirect
import requests

def perfil_usuario(request):
    token = request.session.get("token")
    if not token:
        return redirect('login')  # Redirige si no está logueado

    # Cabecera con el token
    headers = {"Authorization": f"Bearer {token}"}

    # Endpoints de la API del servidor
    user_api_url = "http://127.0.0.1:8092/api/v1/usuarios/me/"
    all_tutorials_api_url = "http://127.0.0.1:8092/api/v1/tutorial"

    user_data = {}
    tutorial_data = []

    try:
        # 1) Obtener datos del usuario logueado
        user_resp = requests.get(user_api_url, headers=headers)
        user_resp.raise_for_status()
        user_data = user_resp.json()  # { "id": 38, "nombre": "raby", ... }

        # 2) Obtener todos los tutoriales (sin filtrar)
        tutorial_resp = requests.get(all_tutorials_api_url, headers=headers)
        tutorial_resp.raise_for_status()
        all_tutorials = tutorial_resp.json()  # Lista con todos los tutoriales

        # 3) Filtrar en el cliente: solo los tutoriales del usuario logueado
        usuario_id = user_data.get("id")
        tutorial_data = [
            t for t in all_tutorials
            if t["usuario"]["id"] == usuario_id
        ]

    except requests.RequestException as e:
        print(f"Error al hacer la petición: {e}")
        # Manejo de errores: podrías poner tutorial_data = []

    # Pasamos el usuario y los tutoriales filtrados al template
    context = {
        "user": user_data,
        "tutoriales": tutorial_data
    }
    return render(request, "Usuario/perfil.html", context)



   #Errores
   
def mi_error_500(request,exception=None):
    return render(request, 'errores/500.html',None,None,500)

#Crear en la API

def crear_tutorial_cliente(request):
    if request.method == 'POST':
        token = request.session.get("token")
        if not token:
            return redirect('login')

        data = {
            "titulo": request.POST.get("titulo"),
            "contenido": request.POST.get("contenido"),
            "fecha_Creacion": request.POST.get("fecha_Creacion"),
            "visitas": request.POST.get("visitas"),
            "valoracion": request.POST.get("valoracion"),
        }

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        api_url = "http://127.0.0.1:8092/api/v1/tutorial/crear_tutorial_api_user/"
        try:
            response = requests.post(api_url, json=data, headers=headers)
            if response.status_code == 201:
                messages.success(request, "Tutorial creado con éxito.")
            elif response.status_code == 400:
                errors = response.json()
                messages.error(request, f"Errores de validación: {errors}")
            else:
                messages.error(request, f"Error {response.status_code}: {response.text}")
        except Exception as e:
            messages.error(request, f"Ocurrió un error: {e}")

        return redirect('listar_tutoriales_api')
    else:
        # Si es GET, mostramos el formulario
        formulario = CreateTutorialForm()
        return render(request, 'Tutorial/formularioTutorial.html', {
            'formulario': formulario
        })

from django.shortcuts import render, redirect
from django.contrib import messages
import requests

def crear_curso_cliente(request):
    if request.method == 'POST':
        token = request.session.get("token")
        if not token:
            messages.error(request, "No estás autenticado.")
            return redirect('login')

        # Recolectamos los datos del formulario (sin usuario)
        data = {
            "nombre": request.POST.get("nombre"),
            "horas": request.POST.get("horas"),
            "precio": request.POST.get("precio"),
            "descripcion": request.POST.get("descripcion"),
        }

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        # Endpoint de la API en el servidor para crear un curso
        api_url = "http://127.0.0.1:8092/api/v1/curso/crear_cursos_api_user/"
        
        try:
            response = requests.post(api_url, json=data, headers=headers)
            if response.status_code in [200, 201]:
                messages.success(request, "Curso creado con éxito.")
            elif response.status_code == 400:
                errores = response.json()
                messages.error(request, f"Errores de validación: {errores}")
            else:
                messages.error(request, f"Error {response.status_code}: {response.text}")
        except requests.RequestException as e:
            messages.error(request, f"Ocurrió un error: {e}")

        # Redirige a la vista que lista los cursos o a donde prefieras
        return redirect('lista_cursos_api')

    else:
        # Si es GET, instanciamos el formulario y lo enviamos al template
        formulario = CreateCourseForm()
        return render(request, 'Cursos/formularioCurso.html', {
            'formulario': formulario
        })


def crear_usuario_api (request):
    token = request.session.get("token")  # 🔥 Obtener el token del usuario logueado
    
    if not token:
        return JsonResponse({"error": "No estás autenticado"}, status=401)
    profesor = os.getenv('TEACHER_USER')
    if (request.method == 'POST'):
        try:
            formulario = Create_usuario(request.POST)
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            datos = formulario.data.copy()
            response = requests .post(
                "http://127.0.0.1:8092/api/v1/usuarios/",
                headers= headers,
                data = json.dumps(datos)
            )
            if response.status_code in [requests.codes.ok, 201]:
                print("Usuario Creado")
                messages.success(request,"Usuario Creado")
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

def crear_tutorial_api(request):

    token = request.session.get("token")  # 🔥 Obtener el token del usuario logueado
    
    if not token:
        return JsonResponse({"error": "No estás autenticado"}, status=401)
    
    profesor = os.getenv('TEACHER_USER')
    print(request.method)
    if (request.method == 'POST'):
        try:
            formulario = Create_tutorial(request.POST, request=request)
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            datos = formulario.data.copy()
            datos['usuarios'] = request.POST.getlist('usuarios')
            response = requests .post(
                'http://127.0.0.1:8092/api/v1/tutorial/crear_tutorial_api',
                headers= headers,
                data = json.dumps(datos)
            )
            if(response.status_code == requests.codes.ok):
                print("Tutoriales creado")
                messages.success(request,"Tutorial Creado")
                return redirect('listar_tutoriales_api')
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
                            'Tutorial/crear_tutorial_api.html',
                            {"formulario":formulario})
            else:
                return mi_error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)
            
    else:
            formulario = Create_tutorial(None, request=request)
    return render(request, 'Tutorial/crear_tutorial_api.html',{"formulario":formulario})

def crear_etiqueta_api(request):

    token = request.session.get("token")  # 🔥 Obtener el token del usuario logueado
    
    if not token:
        return JsonResponse({"error": "No estás autenticado"}, status=401)
    
    profesor = os.getenv('TEACHER_USER')
    print(request.method)
    if (request.method == 'POST'):
        try:
            formulario = Create_etiqueta(request.POST, request = request)
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            datos = formulario.data.copy()
            datos['tutorial'] = request.POST.getlist('tutorial')
            response = requests .post(
                'http://127.0.0.1:8092/api/v1/etiqueta/crear_etiqueta_api',
                headers= headers,
                data = json.dumps(datos)
            )
            if(response.status_code == requests.codes.ok or 201):
                print("Etiqueta creada")
                messages.success(request,"Etiqueta Creada")
                return redirect('lista_etiquetas_api')
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
                            'Etiquetas/crear_etiqueta_api.html',
                            {"formulario":formulario})
            else:
                return mi_error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)
            
    else:
            formulario = Create_etiqueta(None, request = request)
    return render(request, 'Etiquetas/crear_etiqueta_api.html',{"formulario":formulario})

def crear_cursos_api(request):

    token = request.session.get("token")  # 🔥 Obtener el token del usuario logueado
    
    if not token:
        return JsonResponse({"error": "No estás autenticado"}, status=401)
    
    profesor = os.getenv('TEACHER_USER')
    print(request.method)
    if (request.method == 'POST'):
        try:
            formulario = Create_cursos(request.POST, request = request)
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            datos = formulario.data.copy()
            datos['usuario'] = request.POST.getlist('usuario')
            response = requests .post(
                'http://127.0.0.1:8092/api/v1/curso/crear_cursos_api',
                headers= headers,
                data = json.dumps(datos)
            )
            if response.status_code == requests.codes.ok or response.status_code == 201:
                print("Curso creado")
                messages.success(request,"Curso creado")
                return redirect('lista_cursos_api')

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
                            'Cursos/crear_cursos_api.html',
                            {"formulario":formulario})
            else:
                return mi_error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)
            
    else:
            formulario = Create_cursos(None, request = request)
    return render(request, 'Cursos/crear_cursos_api.html',{"formulario":formulario})


# PUT en la API

def usuario_obtener(request, usuario_id):
    
    usuario = helper.obtener_usuarios(usuario_id, request)
    return render(request, 'Usuario/usuario_obtener.html', {'usuario': usuario})

def editar_usuario_api(request, usuario_id):
    datosFormulario = None
    
    if request.method == "POST":
        datosFormulario = request.POST
    
    usuario = helper.obtener_usuarios(usuario_id, request)
    formulario = Create_usuario(datosFormulario,
                                initial={
                                    'nombre': usuario['nombre'],
                                    'email': usuario['email'],
                                    'es_activo': usuario['es_activo'],
                                    'puntuacion': usuario['puntuacion'],
                                    'fecha_Registro': usuario['fecha_Registro'],
                                }
    )
    if(request.method == "POST"):
        formulario = Create_usuario(request.POST)
        datos = request.POST.copy()
        api_cliente = cliente_api("PUT", f"usuarios/{usuario_id}/", datos)
        api_cliente.realizar_peticion_api(request)
        if(api_cliente.es_respuesta_correcta()):
            print("Usuario modificado")
            messages.success(request,"Usuario modificado")
            return redirect("usuario_mostrar",usuario_id=usuario_id)
        else:
            if(api_cliente.es_error_validacion_datos()):
                api_cliente.incluir_errores_formulario(formulario)
            else:
                return tratar_errores(request,api_cliente.codigoRespuesta)
    return render(request, 'Usuario/actualizar.html',{"formulario":formulario,"usuario":usuario, "usuario_id":usuario_id})


def tutorial_obtener(request, tutorial_id):
    tutorial = helper.obtener_tutorial(tutorial_id, request)
    return render(request, 'Tutorial/tutorial_obtener.html', {'tutorial': tutorial})

def editar_tutorial_api(request, tutorial_id):
    datosFormulario = None
    
    if request.method == "POST":
        datosFormulario = request.POST
    
    tutorial = helper.obtener_tutorial(tutorial_id, request)
    formulario = Create_tutorial(datosFormulario,
                                initial={
                                    'titulo': tutorial['titulo'],
                                    'contenido': tutorial['contenido'],
                                    'fecha_Creacion': tutorial['fecha_Creacion'],
                                    'visitas': tutorial['visitas'],
                                    'valoracion': tutorial['valoracion'],
                                    'usuario': [usuario['id'] for usuario in tutorial.get('usuarios', [])],  # 🔹 Cambiado aquí,
                                }, request = request
    )
    if(request.method == "POST"):
        formulario = Create_tutorial(request.POST, request=request)
        datos = request.POST.copy()
        datos['usuarios'] = request.POST.getlist('usuarios')
        api_cliente = cliente_api("PUT", f"tutorial/editar/{tutorial_id}", datos)
        api_cliente.realizar_peticion_api(request)
        if(api_cliente.es_respuesta_correcta()):
            print("Tutorial modificado")
            messages.success(request,"Tutorial modificado")
            return redirect("tutorial_mostrar", tutorial_id=tutorial_id)
        else:
            if(api_cliente.es_error_validacion_datos()):
                api_cliente.incluir_errores_formulario(formulario)
            else:
                return tratar_errores(request,api_cliente.codigoRespuesta)
    return render(request, 'Tutorial/actualizar.html',{"formulario":formulario,"tutorial":tutorial, "tutorial_id":tutorial_id})


def etiqueta_obtener(request, etiqueta_id):
    etiqueta = helper.obtener_etiqueta(etiqueta_id, request)
    return render(request, 'Etiquetas/etiqueta_obtener.html', {'etiqueta': etiqueta})

def editar_etiqueta_api(request, etiqueta_id):
    datosFormulario = None
    
    if request.method == "POST":
        datosFormulario = request.POST
    
    etiqueta = helper.obtener_etiqueta(etiqueta_id, request)
    formulario = Create_etiqueta(datosFormulario,
                                initial={
                                    'nombre': etiqueta['nombre'],
                                    'color': etiqueta['color'],
                                    'publica': etiqueta['publica'],
                                    'descripcion': etiqueta['descripcion'],
                                    'tutorial': [tutorial['id'] for tutorial in etiqueta.get('tutoriales', [])],  # 🔹 Cambiado aquí,
                                }, request = request
    )
    if(request.method == "POST"):
        formulario = Create_etiqueta(request.POST, request = request)
        datos = request.POST.copy()
        datos['tutoriales'] = request.POST.getlist('tutoriales')
        api_cliente = cliente_api("PUT", f"etiqueta/editar/{etiqueta_id}", datos)
        api_cliente.realizar_peticion_api(request)
        if(api_cliente.es_respuesta_correcta()):
            print("Etiqueta modificado")
            messages.success(request,"Etiqueta modificado")
            return redirect("etiqueta_mostrar", etiqueta_id=etiqueta_id)
        else:
            if(api_cliente.es_error_validacion_datos()):
                api_cliente.incluir_errores_formulario(formulario)
            else:
                return tratar_errores(request,api_cliente.codigoRespuesta)
    return render(request, 'Etiquetas/actualizar.html',{"formulario":formulario,"etiqueta":etiqueta, "etiqueta_id":etiqueta_id})

def curso_obtener(request, curso_id):
    curso = helper.obtener_curso(curso_id, request)
    return render(request, 'Cursos/curso_obtener.html', {'curso': curso})

def editar_curso_api(request, curso_id):
    datosFormulario = None
    
    if request.method == "POST":
        datosFormulario = request.POST
    
    curso = helper.obtener_curso(curso_id, request)
    formulario = Create_cursos(datosFormulario,
                                initial={
                                    'nombre': curso['nombre'],
                                    'descripcion': curso['descripcion'],
                                    'horas': curso['horas'],
                                    'precio': curso['precio'],
                                    'usuario': [usuario['id'] for usuario in curso.get('usuarios', [])],
                                }, request = request
    )
    if(request.method == "POST"):
        formulario = Create_cursos(request.POST, request = request)
        datos = request.POST.copy()
        datos['usuario'] = request.POST.getlist('usuario')
        api_cliente = cliente_api("PUT", f"curso/editar/{curso_id}", datos)
        api_cliente.realizar_peticion_api(request)
        if(api_cliente.es_respuesta_correcta()):
            print("Curso modificado")
            messages.success(request,"Curso modificado")
            return redirect("curso_mostrar",curso_id=curso_id)
        else:
            if(api_cliente.es_error_validacion_datos()):
                api_cliente.incluir_errores_formulario(formulario)
            else:
                return tratar_errores(request,api_cliente.codigoRespuesta)
    return render(request, 'Cursos/actualizar.html',{"formulario":formulario,"curso":curso, "curso_id":curso_id})

# PATCH en la API

def actualizar_nombre_usuario_api(request, usuario_id):
    datosFormulario = None

    if request.method == "POST":
        datosFormulario = request.POST

    usuario = helper.obtener_usuarios(usuario_id, request)
    formulario = NombreUsuarioForm(datosFormulario,
                                   initial={
                                       'nombre': usuario['nombre']
                                   })
    if (request.method == 'POST'):
        try:
            formulario = NombreUsuarioForm(request.POST)
            headers = crear_cabezera(request)
            datos = request.POST.copy()
            response = requests.patch(
                'http://127.0.0.1:8092/api/v1/usuarios/'+str(usuario_id)+"/",
                headers=headers,
                data=json.dumps(datos)
            )
            if (response.status_code == requests.codes.ok):
                print("Usuario modificado")
                messages.success(request,"Usuario modificado")
                return redirect('usuario_mostrar', usuario_id=usuario_id)
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
                            'Usuario/actualizaNombre.html',
                            {"formulario":formulario,"usuario":usuario})
            else:
                return mi_error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)
    return render(request, 'Usuario/actualizaNombre.html',{"formulario":formulario,"usuario":usuario, 'usuario_id': usuario_id})


def actualizar_titulo_tutorial_api (request, tutorial_id):
    datosFormulario = None

    if request.method == "POST":
        datosFormulario = request.POST

    tutorial = helper.obtener_tutorial(tutorial_id, request)
    formulario = TituloTutorialForm(datosFormulario,
                                   initial={
                                       'titulo': tutorial['titulo']
                                   })
    if (request.method == 'POST'):
        try:
            formulario = TituloTutorialForm(request.POST)
            headers = crear_cabezera(request)
            datos = request.POST.copy()
            response = requests.patch(
                'http://127.0.0.1:8092/api/v1/tutorial/actualizar/titulo/'+str(tutorial_id),
                headers=headers,
                data=json.dumps(datos)
            )
            if (response.status_code == requests.codes.ok):
                print("Tutorial modificado")
                messages.success(request,"Tutorial modificado")
                return redirect('tutorial_mostrar', tutorial_id=tutorial_id)
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
                            'Tutorial/actualizaTitulo.html',
                            {"formulario":formulario,"tutorial":tutorial})
            else:
                return mi_error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)
    return render(request, 'Tutorial/actualizaTitulo.html',{"formulario":formulario,"tutorial":tutorial, 'tutorial_id': tutorial_id})

def actualizar_nombre_etiqueta_api (request, etiqueta_id):
    datosFormulario = None

    if request.method == "POST":
        datosFormulario = request.POST

    etiqueta = helper.obtener_etiqueta(etiqueta_id, request)
    formulario = EtiquetaNombreForm(datosFormulario,
                                   initial={
                                       'nombre': etiqueta['nombre']
                                   })
    if (request.method == 'POST'):
        try:
            formulario = EtiquetaNombreForm(request.POST)
            headers = crear_cabezera(request)
            datos = request.POST.copy()
            response = requests.patch(
                'http://127.0.0.1:8092/api/v1/etiqueta/actualizar/nombre/'+str(etiqueta_id),
                headers=headers,
                data=json.dumps(datos)
            )
            if (response.status_code == requests.codes.ok):
                print("Etiqueta modificado")
                messages.success(request,"Etiqueta modificado")
                return redirect('etiqueta_mostrar', etiqueta_id=etiqueta_id)
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
                            'Etiquetas/actualizaNombre.html',
                            {"formulario":formulario,"etiqueta":etiqueta})
            else:
                return mi_error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)
    return render(request, 'Etiquetas/actualizaNombre.html',{"formulario":formulario,"etiqueta":etiqueta, 'etiqueta_id': etiqueta_id})

def actualizar_nombre_curso_api (request, curso_id):
    datosFormulario = None

    if request.method == "POST":
        datosFormulario = request.POST

    curso = helper.obtener_curso(curso_id, request)
    formulario = CursoNombreForm(datosFormulario,
                                   initial={
                                       'nombre': curso['nombre']
                                   })
    if (request.method == 'POST'):
        try:
            formulario = CursoNombreForm(request.POST)
            headers = crear_cabezera(request)
            datos = request.POST.copy()
            response = requests.patch(
                'http://127.0.0.1:8092/api/v1/curso/actualizar/nombre/'+str(curso_id),
                headers=headers,
                data=json.dumps(datos)
            )
            if (response.status_code == requests.codes.ok):
                print("Curso modificado")
                messages.success(request,"Curso modificado")
                return redirect('curso_mostrar', curso_id=curso_id)
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
                            'Cursos/actualizaNombre.html',
                            {"formulario":formulario,"curso":curso})
            else:
                return mi_error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)
    return render(request, 'Cursos/actualizaNombre.html',{"formulario":formulario,"curso":curso, 'curso_id': curso_id})

# DELETED en la API

def eliminar_usuario_api(request, usuario_id):
    try:
        headers = crear_cabezera(request)
        response = requests.delete(
            f'http://127.0.0.1:8092/api/v1/usuarios/{usuario_id}/',  # 🔹 Usa f-string para mejorar legibilidad
            headers=headers
        )
        
        # ✅ DRF devuelve 204 para DELETE exitoso, así que revisamos ambos (200 y 204)
        if response.status_code in [requests.codes.ok, 204]:  
            print("Usuario eliminado")
            messages.success(request,"Usuario elimindo")
            return redirect('listar_usuarios_api')
        else:
            print(f"Error {response.status_code}: {response.text}")  # 🔹 Más detalles del error
            response.raise_for_status()
    
    except requests.RequestException as err:
        print(f'Ocurrió un error en la solicitud: {err}')
        return mi_error_500(request)
    
    return redirect('listar_usuarios_api')


def eliminar_tutorial_api(request, tutorial_id):
    try:
        headers = crear_cabezera(request)
        response = requests.delete(
            'http://127.0.0.1:8092/api/v1/tutorial/eliminar/'+str(tutorial_id),
            headers = headers
        )
        if (response.status_code == requests.codes.ok):
            print("Tutorial eliminado")
            messages.success(request,"Tutorial eliminado")
            return redirect('listar_tutoriales_api')
        else:
            print(response.status_code)
            response.raise_for_status()
    except Exception as err:
        print(f'Ocurrió un error: {err}')
        return mi_error_500(request)
    return redirect('listar_tutoriales_api')

def eliminar_etiqueta_api(request, etiqueta_id):
    try:
        headers = crear_cabezera(request)
        response = requests.delete(
            'http://127.0.0.1:8092/api/v1/etiqueta/eliminar/'+str(etiqueta_id),
            headers = headers
        )
        if (response.status_code == requests.codes.ok):
            print("Etiqueta eliminado")
            messages.success(request,"Etiqueta eliminada")
            return redirect('lista_etiquetas_api')
        else:
            print(response.status_code)
            response.raise_for_status()
    except Exception as err:
        print(f'Ocurrió un error: {err}')
        return mi_error_500(request)
    return redirect('lista_etiquetas_api')

def eliminar_curso_api(request, curso_id):
    try:
        headers = crear_cabezera(request)
        response = requests.delete(
            'http://127.0.0.1:8092/api/v1/curso/eliminar/'+str(curso_id),
            headers = headers
        )
        if (response.status_code == requests.codes.ok):
            print("Curso Eliminado")
            messages.success(request, "Curso eliminado")
            return redirect('lista_cursos_api')
        else:
            print(response.status_code)
            response.raise_for_status()
    except Exception as err:
        print(f'Ocurrió un error: {err}')
        return mi_error_500(request)
    return redirect('lista_etiquetas_api')


def tratar_errores(request,codigo):
    if codigo == 404:
        return mi_error_404(request)
    else:
        return mi_error_500(request)
        
#Páginas de Error
def mi_error_404(request,exception=None):
    return render(request, 'errores/404.html',None,None,404)

#REGISTRAR

def registrar_usuario(request):
    if request.method == "POST":
        try:
            formulario = RegistroForm(request.POST)
            if formulario.is_valid():
                headers = {
                    "Content-Type": "application/json"
                }
                response = requests.post(
                    'http://127.0.0.1:8092/api/v1/usuario/registro',
                    headers=headers,
                    data=json.dumps(formulario.cleaned_data)
                )

                if response.status_code in [200, 201]:
                    usuario = response.json()
                    token_acceso = helper.obtener_token_session(
                            formulario.cleaned_data.get("email"),
                            formulario.cleaned_data.get("password1")
                            )
                    request.session["usuario"]=usuario
                    request.session["token"] = token_acceso
                    return redirect("inicio")
                else:
                    messages.error(request, f"Error {response.status_code}: {response.text}")
                    response.raise_for_status()
        except requests.HTTPError as http_err:
            messages.error(request, f'Error en la petición: {http_err}')
            if response.status_code == 400:
                errores = response.json()
                for error in errores:
                    formulario.add_error(error, errores[error])
                return render(request, "Registration/registrar.html", {"formulario": formulario})
        except Exception as err:
            messages.error(request, f'Ocurrió un error inesperado: {err}')
            return render(request, "Registration/registrar.html", {"formulario": formulario})

    else:
        formulario = RegistroForm()
    
    return render(request, "Registration/registrar.html", {"formulario": formulario})

def login(request):
    if request.method == "POST":
        formulario = LoginForm(request.POST)
        
        if formulario.is_valid():  # ✅ Verifica que los datos sean válidos
            try:
                # ✅ Obtener token correctamente
                token_acceso = helper.obtener_token_session(
                    formulario.cleaned_data["usuario"],
                    formulario.cleaned_data["password"]
                )
                
                # ✅ Guardar token en la sesión
                request.session["token"] = token_acceso
                
                # ✅ Usar token en los headers, NO en la URL
                headers = {'Authorization': f'Bearer {token_acceso}'}
                response = requests.get('http://127.0.0.1:8092/api/v1/usuarios/me/', headers=headers)

                if response.status_code == 200:
                    request.session["usuario"] = response.json()
                    print("✅ Datos recibidos de la API en el login:", json.dumps(request.session["usuario"], indent=4))  # 🔍 Depuración
                    return redirect("inicio")  # ✅ "inicio" estaba mal escrito en tu código
                
                else:
                    print(f"Error obteniendo usuario: {response.json()}")
                    formulario.add_error(None, "No se pudo obtener el usuario.")
                    
            except Exception as excepcion:
                print(f'Hubo un error en la petición: {excepcion}')
                formulario.add_error(None, str(excepcion))

        return render(request, 'Registration/login.html', {"form": formulario})

    else:
        formulario = LoginForm()

    return render(request, 'Registration/login.html', {'form': formulario})

def logout(request):
    request.session.pop("token", None)  # Evita el error si el token no existe
    request.session.pop("usuario", None)  # Borra la info del usuario logueado
    request.session.flush()  # Elimina toda la sesión
    return redirect("login")  # Redirige a la página de login