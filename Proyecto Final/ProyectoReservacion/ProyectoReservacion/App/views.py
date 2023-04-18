from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.template.loader import get_template
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import PaginaInicio, Libros, solicitudes, carritos
from django.http import Http404
from django.core.mail import send_mail


libros_carrito = ["Libro prueba 1"]

libros = []

# Pagina de incio
def inicio(request):

    objetodb = PaginaInicio.objects.all()[0]

    datos = {
        'quienessomos': objetodb.quienesSomos,
        'mision': objetodb.mision,
        'vision': objetodb.vision 
    }

    return render(request, "inicio.html", {'datos' : datos})

def reservacion(request):
    libros = Libros.objects.all()

    return render(request, "Reservacion.html", {'libros' : libros})


def carrito(request):


    return render(request, "carrito.html")

def contactenos(request):

    if request.method == "POST":
        subject = request.POST["name"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        texto = request.POST["texto"]

        send_mail('subject', 'texto', 'zamorajc16199@gmail.com', ['zamorajc16199@gmail.com'], fail_silently=False)

        return HttpResponse("Contactenos2.html")
    
    return render(request, "Contactenos.html")

def contactenos2(request):
    return render(request, "Contactenos2.html")