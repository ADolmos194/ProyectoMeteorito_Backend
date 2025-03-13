from django.db import models
from django.contrib.auth.hashers import make_password
from app.models import Estado

# Create your models here.
class Loginusuarios(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    password = models.CharField(max_length=255)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "loginusuarios"
    
    def __str__(self):
        return '%s - %s'% (self.username, self.password)

    def save(self, *args, **kwargs):
        # Cifra la contraseña antes de guardar si no está ya cifrada
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super(Loginusuarios, self).save(*args, **kwargs)
        
        
