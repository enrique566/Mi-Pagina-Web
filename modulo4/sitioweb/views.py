from rest_framework import viewsets
from .models import Libro, SesionComputadora, RegistroTrabajo
from .serializers import LibroSerializer, SesionComputadoraSerializer, RegistroTrabajoSerializer
from django.shortcuts import render

def index(request):
    return render(request, 'sitioweb/index.html')

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class SesionComputadoraViewSet(viewsets.ModelViewSet):
    queryset = SesionComputadora.objects.all()
    serializer_class = SesionComputadoraSerializer

class RegistroTrabajoViewSet(viewsets.ModelViewSet):
    queryset = RegistroTrabajo.objects.all()
    serializer_class = RegistroTrabajoSerializer
