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
    response = requests.get("http://potito.pythonanywhere.com/api/v1/usuarios/", headers= headers)
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
    response = requests.get('http://potito.pythonanywhere.com/api/v1/usuarios/', headers=headers_Profesor)
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
    profesor = os.getenv('TEACHER_USER')
    return {'Authorization': f'Bearer {profesor}',
            'Content-Type': 'application/json'}

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
            response = requests .post(
                "http://potito.pythonanywhere.com/api/v1/usuarios/",
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
    profesor = os.getenv('TEACHER_USER')
    print(request.method)
    if (request.method == 'POST'):
        try:
            formulario = Create_tutorial(request.POST)
            headers = {
                'Authorization': f'Bearer {profesor}',
                'Content-Type': 'application/json'
            }
            datos = formulario.data.copy()
            datos['usuarios'] = request.POST.getlist('usuarios')
            response = requests .post(
                'http://potito.pythonanywhere.com/api/v1/tutorial/crear_tutorial_api',
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
            formulario = Create_tutorial(None)
    return render(request, 'Tutorial/crear_tutorial_api.html',{"formulario":formulario})

def crear_etiqueta_api(request):
    profesor = os.getenv('TEACHER_USER')
    print(request.method)
    if (request.method == 'POST'):
        try:
            formulario = Create_etiqueta(request.POST)
            headers = {
                'Authorization': f'Bearer {profesor}',
                'Content-Type': 'application/json'
            }
            datos = formulario.data.copy()
            datos['tutorial'] = request.POST.getlist('tutorial')
            response = requests .post(
                'http://potito.pythonanywhere.com/api/v1/etiqueta/crear_etiqueta_api',
                headers= headers,
                data = json.dumps(datos)
            )
            if(response.status_code == requests.codes.ok):
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
            formulario = Create_etiqueta(None)
    return render(request, 'Etiquetas/crear_etiqueta_api.html',{"formulario":formulario})

def crear_cursos_api(request):
    profesor = os.getenv('TEACHER_USER')
    print(request.method)
    if (request.method == 'POST'):
        try:
            formulario = Create_cursos(request.POST)
            headers = {
                'Authorization': f'Bearer {profesor}',
                'Content-Type': 'application/json'
            }
            datos = formulario.data.copy()
            datos['usuario'] = request.POST.getlist('usuario')
            response = requests .post(
                'http://potito.pythonanywhere.com/api/v1/curso/crear_cursos_api',
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
            formulario = Create_cursos(None)
    return render(request, 'Cursos/crear_cursos_api.html',{"formulario":formulario})


# PUT en la API

def usuario_obtener(request, usuario_id):
    usuario = helper.obtener_usuarios(usuario_id)
    return render(request, 'Usuario/usuario_obtener.html', {'usuario': usuario})

def editar_usuario_api(request, usuario_id):
    datosFormulario = None
    
    if request.method == "POST":
        datosFormulario = request.POST
    
    usuario = helper.obtener_usuarios(usuario_id)
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
        api_cliente.realizar_peticion_api()
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
    tutorial = helper.obtener_tutorial(tutorial_id)
    return render(request, 'Tutorial/tutorial_obtener.html', {'tutorial': tutorial})

def editar_tutorial_api(request, tutorial_id):
    datosFormulario = None
    
    if request.method == "POST":
        datosFormulario = request.POST
    
    tutorial = helper.obtener_tutorial(tutorial_id)
    formulario = Create_tutorial(datosFormulario,
                                initial={
                                    'titulo': tutorial['titulo'],
                                    'contenido': tutorial['contenido'],
                                    'fecha_Creacion': tutorial['fecha_Creacion'],
                                    'visitas': tutorial['visitas'],
                                    'valoracion': tutorial['valoracion'],
                                    'usuario': [usuario['id'] for usuario in tutorial.get('usuarios', [])],  # 🔹 Cambiado aquí,
                                }
    )
    if(request.method == "POST"):
        formulario = Create_tutorial(request.POST)
        datos = request.POST.copy()
        datos['usuarios'] = request.POST.getlist('usuarios')
        api_cliente = cliente_api("PUT", f"tutorial/editar/{tutorial_id}", datos)
        api_cliente.realizar_peticion_api()
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
    etiqueta = helper.obtener_etiqueta(etiqueta_id)
    return render(request, 'Etiquetas/etiqueta_obtener.html', {'etiqueta': etiqueta})

def editar_etiqueta_api(request, etiqueta_id):
    datosFormulario = None
    
    if request.method == "POST":
        datosFormulario = request.POST
    
    etiqueta = helper.obtener_etiqueta(etiqueta_id)
    formulario = Create_etiqueta(datosFormulario,
                                initial={
                                    'nombre': etiqueta['nombre'],
                                    'color': etiqueta['color'],
                                    'publica': etiqueta['publica'],
                                    'descripcion': etiqueta['descripcion'],
                                    'tutorial': [tutorial['id'] for tutorial in etiqueta.get('tutoriales', [])],  # 🔹 Cambiado aquí,
                                }
    )
    if(request.method == "POST"):
        formulario = Create_etiqueta(request.POST)
        datos = request.POST.copy()
        datos['tutoriales'] = request.POST.getlist('tutoriales')
        api_cliente = cliente_api("PUT", f"etiqueta/editar/{etiqueta_id}", datos)
        api_cliente.realizar_peticion_api()
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
    curso = helper.obtener_curso(curso_id)
    return render(request, 'Cursos/curso_obtener.html', {'curso': curso})

def editar_curso_api(request, curso_id):
    datosFormulario = None
    
    if request.method == "POST":
        datosFormulario = request.POST
    
    curso = helper.obtener_curso(curso_id)
    formulario = Create_cursos(datosFormulario,
                                initial={
                                    'nombre': curso['nombre'],
                                    'descripcion': curso['descripcion'],
                                    'horas': curso['horas'],
                                    'precio': curso['precio'],
                                    'usuario': [usuario['id'] for usuario in curso.get('usuarios', [])],
                                }
    )
    if(request.method == "POST"):
        formulario = Create_cursos(request.POST)
        datos = request.POST.copy()
        datos['usuario'] = request.POST.getlist('usuario')
        api_cliente = cliente_api("PUT", f"curso/editar/{curso_id}", datos)
        api_cliente.realizar_peticion_api()
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

    usuario = helper.obtener_usuarios(usuario_id)
    formulario = NombreUsuarioForm(datosFormulario,
                                   initial={
                                       'nombre': usuario['nombre']
                                   })
    if (request.method == 'POST'):
        try:
            formulario = NombreUsuarioForm(request.POST)
            headers = crear_cabezera()
            datos = request.POST.copy()
            response = requests.patch(
                'http://potito.pythonanywhere.com/api/v1/usuarios/'+str(usuario_id)+"/",
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

    tutorial = helper.obtener_tutorial(tutorial_id)
    formulario = TituloTutorialForm(datosFormulario,
                                   initial={
                                       'titulo': tutorial['titulo']
                                   })
    if (request.method == 'POST'):
        try:
            formulario = TituloTutorialForm(request.POST)
            headers = crear_cabezera()
            datos = request.POST.copy()
            response = requests.patch(
                'http://potito.pythonanywhere.com/api/v1/tutorial/actualizar/titulo/'+str(tutorial_id),
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

    etiqueta = helper.obtener_etiqueta(etiqueta_id)
    formulario = EtiquetaNombreForm(datosFormulario,
                                   initial={
                                       'nombre': etiqueta['nombre']
                                   })
    if (request.method == 'POST'):
        try:
            formulario = EtiquetaNombreForm(request.POST)
            headers = crear_cabezera()
            datos = request.POST.copy()
            response = requests.patch(
                'http://potito.pythonanywhere.com/api/v1/etiqueta/actualizar/nombre/'+str(etiqueta_id),
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

    curso = helper.obtener_curso(curso_id)
    formulario = CursoNombreForm(datosFormulario,
                                   initial={
                                       'nombre': curso['nombre']
                                   })
    if (request.method == 'POST'):
        try:
            formulario = CursoNombreForm(request.POST)
            headers = crear_cabezera()
            datos = request.POST.copy()
            response = requests.patch(
                'http://potito.pythonanywhere.com/api/v1/curso/actualizar/nombre/'+str(curso_id),
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
        headers = crear_cabezera()
        response = requests.delete(
            f'http://potito.pythonanywhere.com/api/v1/usuarios/{usuario_id}/',  # 🔹 Usa f-string para mejorar legibilidad
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
        headers = crear_cabezera()
        response = requests.delete(
            'http://potito.pythonanywhere.com/api/v1/tutorial/eliminar/'+str(tutorial_id),
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
        headers = crear_cabezera()
        response = requests.delete(
            'http://potito.pythonanywhere.com/api/v1/etiqueta/eliminar/'+str(etiqueta_id),
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
        headers = crear_cabezera()
        response = requests.delete(
            'http://potito.pythonanywhere.com/api/v1/curso/eliminar/'+str(curso_id),
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
