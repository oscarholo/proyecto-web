from django.db import models

class Portatil(models.Model):
    nombre = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)

   
    sistema_operativo = models.CharField(max_length=100)
    procesador = models.CharField(max_length=100)
    ram = models.CharField(max_length=50)            
    almacenamiento = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} ({'Disponible' if self.disponible else 'Ocupado'})"


class Tablet(models.Model):
    nombre = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)

    sistema_operativo = models.CharField(max_length=100)
    procesador = models.CharField(max_length=100)
    ram = models.CharField(max_length=50)
    almacenamiento = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} ({'Disponible' if self.disponible else 'Ocupado'})"


class Reserva(models.Model):
    empleado = models.CharField(max_length=50)
    fecha_reserva = models.DateTimeField(auto_now_add=True)

    
    portatil = models.ForeignKey(
        Portatil, null=True, blank=True, on_delete=models.SET_NULL
    )
    tablet = models.ForeignKey(
        Tablet, null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        if self.portatil:
            return f"Reserva de {self.portatil.nombre} por {self.empleado}"
        if self.tablet:
            return f"Reserva de {self.tablet.nombre} por {self.empleado}"
        return f"Reserva sin dispositivo ({self.empleado})"

