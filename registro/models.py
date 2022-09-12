from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

    
class Usuario(models.Model):
    nombre = models.CharField(max_length=45, blank=False, unique= False, verbose_name=u"Nombre")
    apellido = models.CharField(max_length=45, blank=False, unique= False, verbose_name=u"Apellido")
    telefono = models.CharField(max_length=13, blank=True, unique=True, verbose_name="Numero de celular")

    def __str__(self) -> str:
        return '%s %s'%(self.nombre, self.apellido)

class Vehículo(models.Model):
    placa = models.CharField(max_length=7, unique=True,verbose_name="Placa")
    fecha = models.DateTimeField(auto_now_add=True)
    modelo = models.CharField(max_length=25)
    color= models.CharField(max_length=15, verbose_name="Color del vehículo")
    class Estado(models.TextChoices):
        EXCELENTE = 'E', _('Exelente (E)')
        REGULAR = 'R', _('Regular (R)')
        BIEN = 'B', _('Bien (B)')
        MAL = 'M', _('Mal (M)')
    estado = models.CharField(max_length=10,choices=Estado.choices, verbose_name=u"Estado")
    usuario=models.ForeignKey(Usuario,on_delete=models.SET_NULL, null=True,verbose_name=u"Usuario")
    
    def __str__(self) -> str:
        return '%s'%(self.placa)