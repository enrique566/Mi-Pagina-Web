from rest_framework import serializers
from .models import Libro, SesionComputadora, RegistroTrabajo

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'

class SesionComputadoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = SesionComputadora
        fields = '__all__'

class RegistroTrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroTrabajo
        fields = '__all__'
