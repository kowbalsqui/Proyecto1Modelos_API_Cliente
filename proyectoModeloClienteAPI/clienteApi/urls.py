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
    path('Tutorial/busqueda_tutorial_avanzado_api', views.busqueda_tutorial_avanzado_api, name = 'busqueda_tutorial_avanzado_api'),
    path('Cursos/busqueda_perfil_avanzado_api', views.busqueda_perfil_avanzado_api, name = 'busqueda_perfil_avanzado_api'),
    path('Comentario/busqueda_comentario_avanzado_api', views.busqueda_comentario_avanzado_api, name = 'busqueda_comentario_avanzado_api'),
    #URL POST
    path('Usuario/crear_usuario_api', views.crear_usuario_api, name = 'crear_usuario_api'),
    path('Tutorial/crear_tutorial_api', views.crear_tutorial_api, name = 'crear_tutorial_api'),
    path('Etiqueta/crear_etiqueta_api', views.crear_etiqueta_api, name= 'crear_etiqueta_api'),
    path('Cursos/crear_curso_api', views.crear_cursos_api, name= 'crear_cursos_api'),
    #URL PUT
    path('Usuario/editar_usuario_api/<int:usuario_id>', views.editar_usuario_api, name = 'editar_usuario_api'),
    path('Usuario/mostrar/<int:usuario_id>', views.usuario_obtener, name='usuario_mostrar'),
    path('Tutorial/editar_tutorial_api/<int:tutorial_id>', views.editar_tutorial_api, name = 'editar_tutorial_api'),
    path('Tutorial/mostrar/<int:tutorial_id>', views.tutorial_obtener, name='tutorial_mostrar'),
    path('Etiqueta/editar_etiqueta_api/<int:etiqueta_id>', views.editar_etiqueta_api, name = 'editar_etiqueta_api'),
    path('Etiqueta/mostrar/<int:etiqueta_id>', views.etiqueta_obtener, name='etiqueta_mostrar'),
    #URL PATCH
    path('Usuario/editar/nombre/<int:usuario_id>', views.actualizar_nombre_usuario_api, name = 'actualizar_nombre_usuario_api'),
    path('Tutorial/editar/titulo/<int:tutorial_id>', views.actualizar_titulo_tutorial_api, name= 'actualizar_titulo_tutorial_api'),
    path('Etiqueta/editar/nombre/<int:etiqueta_id>', views.actualizar_nombre_etiqueta_api, name= 'actualizar_nombre_etiqueta_api'),
    #URL DELETE
    path('Usuario/eliminar/<int:usuario_id>',views.eliminar_usuario_api,name='usuario_eliminar'),
    path('Tutorial/eliminar/<int:tutorial_id>', views.eliminar_tutorial_api, name = 'tutorial_eliminar'),
    path('Etiqueta/eliminar/<int:etiqueta_id>', views.eliminar_etiqueta_api, name = 'etiqueta_eliminar'),
]