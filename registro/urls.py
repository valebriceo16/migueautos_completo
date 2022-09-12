from django.urls import path    
from . import views

urlpatterns = [
    path ('vehiculo/', views.vehiculo, name='vehiculo'),
    path ('vehiculo/eliminar/<int:id>', views.vehiculoDelete, name='eliminarvehiculo'),
    path ('vehiculo/editar/<int:id>', views.editarVehiculo, name='editarVehiculo'),
    
    path ('usuario/', views.usuario, name='usuario'),
    path ('usuario/editar/<int:id>', views.editarUsuario, name='editarUsuario'),
    path ('usuario/eliminar/<int:id>', views.usuariodelete, name='eliminarusuario'),
 ]