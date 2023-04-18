from django.urls import path

from App import views

urlpatterns = [
    path('inicio', views.inicio, name="inicio"),
    path('reservacion', views.reservacion, name="reservacion"),
    path('carrito', views.carrito, name="carrito"),
    path('contactenos', views.contactenos, name="contactenos"),
    path('contactenos2', views.contactenos2, name="contactenos2")
]