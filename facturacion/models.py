from django.db import models
from django.utils.translation import gettext_lazy as _
from registro.models import Usuario,Vehículo
from insumo.models import Insumo,Servicio
# Create your models here.
class Generar(models.Model):
    usuario = models.ForeignKey(Usuario, verbose_name="usuario",on_delete=models.SET_NULL, null=True)
    vehiculo = models.ForeignKey(Vehículo, verbose_name="vehiculo",on_delete=models.SET_NULL, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario}'
    
# class Agregarservicio(models.Model):
#     servicio = models.ForeignKey(Servicio)

class Carrodecompras(models.Model):
    insumo = models.ForeignKey(Insumo, verbose_name="insumo",on_delete=models.SET_NULL, null=True)

class Compras(models.Model):
    factura = models.ForeignKey(Generar, verbose_name="factura",on_delete=models.SET_NULL, null=True)
   
    class Estado (models.TextChoices):
        activa = 'Activo', _('Activo')
        Completa= 'Completa', _('Completa')
    estado = models.CharField(max_length=10, choices=Estado.choices,default=Estado.activa,verbose_name=u"Estado de factura")
    class Tipodeservicio (models.TextChoices):
        LATONERIA = 'Latoneria', _('Latoneria')
        PINTURA= 'Pintura', _('Pintura')
    tipodeservicio = models.CharField(max_length=10, choices=Tipodeservicio.choices, verbose_name=u"Seleccione el tipo de servicio")
    
    