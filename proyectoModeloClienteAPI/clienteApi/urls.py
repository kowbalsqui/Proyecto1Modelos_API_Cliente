from django.urls import path, re_path
from .import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('Tutorial/lista_tutorial_api.html', views.tutorial_lista_api, name = 'listar_tutoriales_api'),
    path('enlaces/', views.pagina_de_enlaces, name='pagina_de_enlaces'),
]