"""ProyectoReservacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from App import views

""" Para utilizar cada pagina del app, debemos colocar un nombre que no sea igual a los de las apps, para llamar al app por independiente"""
"""Ejemplo el url Biblioteca/inicio o biblioteca/reservacion """
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Biblioteca/', include('App.urls'))
]
