from django.db import models

class Doctor(models.Model):
    # Campo de texto para el nombre del doctor (máximo 100 caracteres)
    first_name = models.CharField(max_length=100)
    
    # Campo de texto para el apellido del doctor (máximo 100 caracteres)
    last_name = models.CharField(max_length=100)
    
    # Campo de fecha para la fecha de nacimiento del doctor
    birth_date = models.DateField()
    
    # Campo de texto para la dirección del doctor (máximo 255 caracteres)
    address = models.CharField(max_length=255)
    
    # Campo booleano para el estado activo/inactivo del doctor (por defecto True)
    is_active = models.BooleanField(default=True)

    # Clase Meta para definir opciones adicionales del modelo
    class Meta:
        # Nombre singular en la interfaz de administración
        verbose_name = "Doctor"
        
        # Nombre plural en la interfaz de administración
        verbose_name_plural = "Doctors"
        
        # Ordena los resultados por apellido y luego por nombre
        ordering = ['last_name', 'first_name']

    # Método para definir la representación en cadena del objeto
    def __str__(self):
        # Retorna el nombre completo del doctor (nombre + apellido)
        return f"{self.first_name} {self.last_name}"
