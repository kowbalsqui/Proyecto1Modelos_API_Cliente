# Proyecto1Modelos_API_Cliente
TOKEN DE ADMIN
curl -X POST "http://localhost:8000/oauth2/token/" -d "grant_type=password&username=administrator@gmail.com&password=admin33&client_id=mi_aplicacion&client_secret=mi_clave_secreta"

TOKEN DE PROFE
curl -X POST "http://localhost:8000/oauth2/token/" -d "grant_type=password&username=<YOUR_USERNAME>&password=<YOUR_PASSWORD>&client_id=mi_aplicacion&client_secret=mi_clave_secreta"

TOKEN DE ESTUDIANTE
curl -X POST "http://localhost:8000/oauth2/token/" -d "grant_type=password&username=<YOUR_USERNAME>&password=<YOUR_PASSWORD>&client_id=mi_aplicacion&client_secret=mi_clave_secreta"
