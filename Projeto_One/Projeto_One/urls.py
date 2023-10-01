# from django.contrib import admin

from django.urls import path
from App_One import views

urlpatterns = [
    #rota,viwer resposnsavel, rota de referencia
    #usuario.com
    path('',views.home,name='home'),
    #
    path('usuarios/',views.usuarios,name='lista_de_usuarios'),
]
