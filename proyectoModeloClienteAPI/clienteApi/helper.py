import requests
import environ
import os
from pathlib import Path
from dotenv import load_dotenv
import urllib.parse
import requests
import json
import os
from dotenv import load_dotenv
from requests.exceptions import HTTPError
from django.http import JsonResponse
class helper:
    load_dotenv()

    def obtener_usuarios(id, request):
        token = request.session.get("token")  # 🔥 Obtener el token del usuario logueado
        
        if not token:
            return JsonResponse({"error": "No estás autenticado"}, status=401)
        #Obtenemos todos los usuarios
        profesor = os.getenv('TEACHER_USER')
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get('http://127.0.0.1:8092/api/v1/usuarios/'+str(id), headers=headers)
        usuario = response.json()
        return usuario
    
    def obtener_tutorial(id, request):
        token = request.session.get("token")  # 🔥 Obtener el token del usuario logueado
        
        if not token:
            return JsonResponse({"error": "No estás autenticado"}, status=401)
        profesor = os.getenv('TEACHER_USER')
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get('http://127.0.0.1:8092/api/v1/tutorial/'+str(id), headers=headers)
        tutorial = response.json()
        return tutorial

    def obtener_etiqueta(id, request):
        token = request.session.get("token")  # 🔥 Obtener el token del usuario logueado
        
        if not token:
            return JsonResponse({"error": "No estás autenticado"}, status=401)
        profesor = os.getenv('TEACHER_USER')
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get('http://127.0.0.1:8092/api/v1/etiqueta/'+str(id), headers=headers)
        etiqueta = response.json()
        return etiqueta
    
    def obtener_curso(id, request):
        token = request.session.get("token")  # 🔥 Obtener el token del usuario logueado
        
        if not token:
            return JsonResponse({"error": "No estás autenticado"}, status=401)
        profesor = os.getenv('TEACHER_USER')
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get('http://127.0.0.1:8092/api/v1/curso/'+str(id), headers=headers)
        cursos = response.json()
        return cursos
    
    def obtener_usuario_selec(request):
        token = request.session.get("token")  # 🔥 Obtener el token del usuario logueado
        
        if not token:
            return JsonResponse({"error": "No estás autenticado"}, status=401)
        profesor = os.getenv('TEACHER_USER')
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get('http://127.0.0.1:8092/api/v1/usuario', headers=headers)
        usuarios = response.json()
        lista_usuarios = []
        for usuario in usuarios:
            lista_usuarios.append((usuario["id"], usuario["nombre"]))
        return lista_usuarios
    
    def obtener_tutorial_selec(request):
        token = request.session.get("token")  # 🔥 Obtener el token del usuario logueado
        
        if not token:
            return JsonResponse({"error": "No estás autenticado"}, status=401)
        profesor = os.getenv('TEACHER_USER')
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get('http://127.0.0.1:8092/api/v1/tutorial', headers=headers)
        tutoriales = response.json()
        lista_tutorial = []
        for tutorial in tutoriales:
            lista_tutorial.append((tutorial["id"], tutorial["titulo"]))
        return lista_tutorial
    
    def obtener_token_session(usuario, password):
        token_url = 'http://127.0.0.1:8092/oauth2/token/'
        data = {
            'grant_type': 'password',
            'username': usuario,
            'password': password,
            'client_id': 'mi_aplicacion',
            'client_secret': 'mi_clave_secreta',
        }
        response = requests.post(token_url, data=data)
        respuesta = response.json()
        if response.status_code == 200:
            return respuesta.get('access_token')
        else:
            raise Exception(respuesta.get("error_description"))

    