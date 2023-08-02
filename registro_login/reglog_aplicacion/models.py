from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    # Otros campos y atributos del modelo

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
