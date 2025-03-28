from django.db import models

# Create your models here.
from django.db import models
from app.models import  Estado, Estadopagos, Tipodocumento

class Clientes(models.Model):
    
    """
    El modelo Clientes representa a un cliente dentro del sistema. Cada cliente tiene un tipo de documento, 
    un número de documento, nombre completo, correo electrónico, número de celular y estado asociado.
    Este modelo también incluye las fechas de creación y modificación automáticas.
    """
    
    # Relación con el modelo Tipodocumento, que indica el tipo de documento del cliente (por ejemplo, DNI, pasaporte, etc.)
    tipodocumento = models.ForeignKey(Tipodocumento, on_delete=models.CASCADE)
    
    # Número de documento del cliente (por ejemplo, el número de su DNI o pasaporte)
    nro_documento = models.CharField(max_length=15, null=True, blank=True)
    
    # Nombre completo del cliente
    nombre_completo = models.CharField(max_length=100, null=True, blank=True)
    
    # Correo electrónico del cliente
    correo_electronico = models.CharField(max_length=255, null=True, blank=True)
    
    # Número de celular del cliente
    nro_celular = models.CharField(max_length=25, null=True, blank=True)
    
    # Relación con el modelo Estado, que indica el estado actual del cliente (activo, inactivo, etc.)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    
    # Fecha de creación automática del registro del cliente    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Fecha de última modificación automática del registro del cliente
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        # Define el nombre de la tabla en la base de datos
        db_table = "clientes"
        
    def __str__(self):
        """
        Método que devuelve una representación en cadena del modelo.
        En este caso, devuelve el nombre completo del cliente.
        """
        return '%s' % (self.nombre_completo)


#Se aplica lo mismo para el resto
class Tesis(models.Model):
    
    clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    nombre_tesis = models.CharField(max_length=255, null=True, blank=True)
    universidad = models.CharField(max_length=100, null=True, blank=True)
    usuario_plataforma = models.CharField(max_length=25, null=True, blank=True)
    clave_plataforma = models.CharField(max_length=25, null=True, blank=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        
        db_table = "tesis"
        
    def __str__(self):
        
        return "%s - %s" % (self.clientes, self.universidad)


class Pagosclientes(models.Model):
    
    tesis = models.ForeignKey(Tesis, on_delete=models.CASCADE)
    monto_tesis = models.FloatField(null=True, blank=True)
    cuotas = models.CharField(max_length=25, null=True, blank=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        
        db_table = "pagosclientes"
        
    def __str__(self):
        
        return "%s - %s"  % (self.tesis, self.monto_tesis)
    
class Detallespagoclientes(models.Model):
    
    pagosclientes = models.ForeignKey(Pagosclientes, on_delete=models.CASCADE)
    cuotaspagadas = models.CharField(max_length=25, null=True, blank=True)
    monto_cuotas = models.FloatField(null=True, blank=True)
    fechapago = models.DateField(null=True, blank=True)
    estado_pago = models.ForeignKey(Estadopagos, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        
        db_table = "detallespagoclientes"
        
    def __str__(self):
        
        return "%s - %s" % (self.pagosclientes, self.cuotaspagadas)
    
    
