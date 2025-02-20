import requests
import environ
import os
from pathlib import Path
from dotenv import load_dotenv
import urllib.parse

class helper:
    load_dotenv()

    def obtener_usuarios(id):
        #Obtenemos todos los usuarios
        profesor = os.getenv('TEACHER_USER')
        headers = {'Authorization': f'Bearer {profesor}'}
        response = requests.get('http://potito.pythonanywhere.com/api/v1/usuario/'+str(id), headers=headers)
        usuario = response.json()
        return usuario
    
    def obtener_tutorial(id):
        profesor = os.getenv('TEACHER_USER')
        headers = {'Authorization': f'Bearer {profesor}'}
        response = requests.get('http://potito.pythonanywhere.com/api/v1/tutorial/'+str(id), headers=headers)
        tutorial = response.json()
        return tutorial

    def obtener_etiqueta(id):
        profesor = os.getenv('TEACHER_USER')
        headers = {'Authorization': f'Bearer {profesor}'}
        response = requests.get('http://potito.pythonanywhere.com/api/v1/etiqueta/'+str(id), headers=headers)
        etiqueta = response.json()
        return etiqueta
    
    def obtener_curso(id):
        profesor = os.getenv('TEACHER_USER')
        headers = {'Authorization': f'Bearer {profesor}'}
        response = requests.get('http://potito.pythonanywhere.com/api/v1/curso/'+str(id), headers=headers)
        cursos = response.json()
        return cursos
    
    def obtener_usuario_selec():
        profesor = os.getenv('TEACHER_USER')
        headers = {'Authorization': f'Bearer {profesor}'}
        response = requests.get('http://potito.pythonanywhere.com/api/v1/usuario', headers=headers)
        usuarios = response.json()
        lista_usuarios = []
        for usuario in usuarios:
            lista_usuarios.append((usuario["id"], usuario["nombre"]))
        return lista_usuarios
    
    def obtener_tutorial_selec():
        profesor = os.getenv('TEACHER_USER')
        headers = {'Authorization': f'Bearer {profesor}'}
        response = requests.get('http://potito.pythonanywhere.com/api/v1/tutorial', headers=headers)
        tutoriales = response.json()
        lista_tutorial = []
        for tutorial in tutoriales:
            lista_tutorial.append((tutorial["id"], tutorial["titulo"]))
        return lista_tutorial

    