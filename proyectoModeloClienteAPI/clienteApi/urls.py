from django.urls import path, re_path
from .import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('Usuario/lista_usuario_api.html', views.usuario_lista_api, name = 'listar_usuarios_api'),
    path('Tutorial/lista_tutorial_api.html', views.tutorial_lista_apiProfesor, name = 'listar_tutoriales_api'),
    path('Tutorial/lista_tutorial_api.html', views.tutorial_lista_apiAdmin, name = 'listar_tutoriales_apiAdmin'),
    path('Tutorial/lista_tutorial_api.html', views.tutorial_lista_apiEstudiante, name = 'listar_tutoriales_apiEstudiante'),
    path('Usuario/lista_usuario_api_html', views.usuario_lista_api, name = 'listar_usuarios_api'),
    path('Categoria/lista_categoria_api_html', views.categoria_lista_api, name = 'listar_categoria_api'),
    path('Cursos/lista_cursos_api.html', views.cursos_lista_api, name = 'lista_cursos_api'),
    path('Etiquetas/lista_etiquetas_api.html', views.etiquetas_lista_api, name = 'lista_etiquetas_api'),
    path('enlaces/', views.pagina_de_enlaces, name='pagina_de_enlaces'),
    #URLS de los formularios de busqueda basicos
    path('Usuario/busqueda_usuario_simple_api', views.busqueda_usuario_simple_api, name = 'busqueda_usuario_simple_api'),
    #URLS de los formularios de busqueda avanzados
    path('Usuario/busqueda_usuario_avanzado_api', views.busqueda_usuario_avanzado_api, name = 'busqueda_usuario_avanzado_api'),
]