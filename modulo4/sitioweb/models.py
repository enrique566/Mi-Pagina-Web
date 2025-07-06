from django.db import models

class Libro(models.Model):
    CATEGORIAS = [
        ('CLASICOS', 'Clásicos'),
        ('TERROR', 'Terror'),
        ('FANTASIA', 'Fantasía'),
        ('HISTORIA', 'Historia'),
        ('POESIA', 'Poesía'),
        ('MUSICA', 'Música'),
    ]
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)

    def __str__(self):
        return self.titulo

class SesionComputadora(models.Model):
    tiempo_uso_minutos = models.IntegerField()
    sitios_web_visitados = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sesión de {self.tiempo_uso_minutos} minutos el {self.fecha}"

class RegistroTrabajo(models.Model):
    nombre_empleado = models.CharField(max_length=100)
    horas_trabajadas = models.DecimalField(max_digits=4, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return f"Registro de {self.nombre_empleado} - {self.fecha}"
