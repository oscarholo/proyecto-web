from django.db import models

class Ubicaciones(models.Model):
    id_ubi = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        db_table = 'Ubicaciones'
        verbose_name_plural = 'Ubicaciones'

class Dispositivos(models.Model):
    TIPO_CHOICES = [
        ('Ordenador', 'Ordenador'),
        ('Portátil', 'Portátil'),
        ('Teclado', 'Teclado'),
        ('Monitor', 'Monitor'),
        ('Otro', 'Otro'),
    ]
    
    ESTADO_CHOICES = [
        ('Funcional', 'Funcional'),
        ('Averiado', 'Averiado'),
        ('Obsoleto', 'Obsoleto'),
    ]
    
    id_dis = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    marca = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    n_serie = models.CharField(max_length=50, unique=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Funcional')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    id_ubi = models.ForeignKey(Ubicaciones, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.n_serie})"

    class Meta:
        db_table = 'Dispositivos'
        verbose_name_plural = 'Dispositivos'

class Traslados(models.Model):
    id_tras = models.AutoField(primary_key=True)
    id_dis = models.ForeignKey(Dispositivos, on_delete=models.CASCADE)
    id_ubi = models.ForeignKey(Ubicaciones, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_traslado = models.DateTimeField(auto_now_add=True)
    responsable = models.CharField(max_length=100)
    desde = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"Traslado {self.id_tras} - {self.id_dis.nombre}"

    class Meta:
        db_table = 'Traslados'
        verbose_name_plural = 'Traslados'