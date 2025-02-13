import requests
import environ
import os
from pathlib import Path
from dotenv import load_dotenv
class helper:
    load_dotenv()

    def obtener_usuarios(id):
        #Obtenemos todos los usuarios
        profesor = os.getenv('TEACHER_USER')
        headers = {'Authorization': f'Bearer {profesor}'}
        response = requests.get('http://127.0.0.1:8092/api/v1/usuario/'+str(id), headers=headers)
        usuario = response.json()
        return usuario

    