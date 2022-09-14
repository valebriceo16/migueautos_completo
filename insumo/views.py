from django.shortcuts import render,redirect
from insumo.forms import  InsumoForm, MarcaForm, ServicioForm
from .models import Insumo, Marca, Servicio
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.views.generic.edit import CreateView

class insumo(CreateView):
    model = Insumo
    fields = '__all__'
    template_name = 'insumo/insumo_form.html'
    
# Create your views here.
@login_required(login_url='/login/')
def servicio(request):
    servicio_db = Servicio.objects.all()
    servicio = ServicioForm(request.POST or None, request.FILES or None)

    if servicio.is_valid():
       servicio.save()
       return redirect('insumo')
   
    context = {
        'servicio_db': servicio_db,
        'servicio': servicio,
    }
    return render (request, 'servicios/servicio.html', context)
def editarServicio(request,id):
    edit_Servicio = Servicio.objects.get(id=id)
    servicio = ServicioForm(request.POST or None, request.FILES or None, instance=edit_Servicio)
    context = {
        'servicio': servicio,
    }
    if servicio.is_valid() and request.method == 'POST':
        servicio.save()
        return redirect('insumo')
    return render (request, 'servicios/servicio.html', context) 
     
def eliminarServicio(request,id):
    delete_Servicio = Servicio.objects.get(id=id)
    url_back = 'servicio'
    txt_action = 'Servicio'
    context = {
        'url_back': url_back,
        'txt_action': txt_action,
    }
    if request.method == 'POST':
        delete_Servicio.delete()
        return redirect ('servicio')  
    return render (request, 'servicios/deleteServicio.html',context)
# lOGICA DE insumo (EDITAR ELIMINAR Y OTRAS FUNCIONES)




@login_required(login_url='/login/')
def insumos(request):
    db_insumo = Insumo.objects.all()
    form = InsumoForm()
    if request.method == 'POST':
        form = InsumoForm(request.POST)
        print(form)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            marca = form.cleaned_data['marca']
            if Insumo.objects.filter(nombre=nombre,marca=marca).exists():
                messages.success(request,'El insumo %s es existente' %nombre)
            else:
                s = form.save()
                s.save()
                messages.success(request,'El insumo %s fue registrado correctamente' %nombre)
                return redirect('insumo')
              
    context = {
        'insumos' : db_insumo,
        'form': form,
    } 
    return render (request, 'insumo/insumo.html', context)

def editarInsumo(request,id):   
    edit_insumo = Insumo.objects.get(id=id)
    insumo_form = InsumoForm(request.POST or None, request.FILES or None, instance=edit_insumo)
    print(edit_insumo)
    if request.method == "POST":
        insumo_form = InsumoForm(request.POST)
        if insumo_form.is_valid():
            nombre = insumo_form.cleaned_data['nombre']
            marca = insumo_form.cleaned_data['marca']
            print('valido')
            if Insumo.objects.filter(nombre=nombre,marca=marca).exists():
                messages.error(request,'%s Ya es un insumo existente'%edit_insumo.nombre)
            
            else:
                insumo_form.save()
                messages.success(request, 'Insumo editado %s correctamente.' %edit_insumo.nombre)
                return redirect('insumo')
    context = {
         'insumo': insumo_form,
         'edit': edit_insumo,
    }
    return render (request, 'insumo/editar.html', context) 
    
def eliminarInsumo(request,id):
    delete_insumo = Insumo.objects.get(id=id)
    url_back = 'insumo'
    txt_action = 'insumo'
    context = {
        'url_back': url_back,
        'txt_action': txt_action,
    }
    if request.method == 'POST' and 'eliminar' in request.POST: # si el metodo es post y el formulario es
        delete_insumo.delete() # se elimina el vehiculo
        messages.success(request,'Vehiculo %s eliminado exitosamente' %delete_insumo.nombre) # se muestra un mensaje de exito
        return redirect ('insumo') # se redirecciona a la url
    if request.method == 'POST' and 'cancelar' in request.POST: # si el metodo es post y el formulario es form2
        #no se realiza ninguna accion por que el cliente decidio no eliminar el vehiculo
        return redirect ('insumo') 
    return render (request, 'insumo/eliminar/eliminar.html',context)

# LOGICA DE marca (EDITAR, ELIMINAR  Y OTRAS FUNCIONES)
@login_required(login_url='/login/')
def marca(request):
    db_insumo = Marca.objects.all()
    form = MarcaForm()
    if request.method == 'POST': 
        form = MarcaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            
            if Insumo.objects.filter(nombre=nombre).exists():
                messages.success(request,'La marca %s ya existe'%nombre)
                return redirect ('insumo')
            else:
                form = MarcaForm(request.POST)
                s = form.save()
                s.save()
                messages.success(request,'La marca %s fue registrada exitosamente'%nombre)
                return redirect('insumo')
    context = {
        'marcas' :db_insumo,
        'form': form,
    }
    return render (request,'insumo/marca.html', context)

def editarmarca(request,id):
    editar = Marca.objects.get(id=id)
    if request.method == "POST" and 'cancelar':
        form = MarcaForm(request.POST,instance=editar)
        if form.is_valid():
            editar.nombre = request.POST['nombre'] #nose que quieres editar solo es un ejemplo
            editar.save()
            messages.success(request,'La marca %s ah sido editada' %editar.nombre)
            return redirect ('insumo')
        else : 
            form = MarcaForm(instance=editar)
            context = {'formulario' : form}
        
    else:
        form = MarcaForm(instance=editar)    
    if request.method == 'post' and 'editar' in request.POST: # si el metodo es post y el formulario es form2
        #no se realiza ninguna accion por que el cliente decidio no eliminar el vehiculo
        return redirect ('insumo')
    context={
        'formulario': form,
        'marca': editar,
    }
    return render (request, 'insumo/editar/editarmarca.html', context)  

def eliminarMarca(request,id):
    vehiculo_d = Marca.objects.get(id=id) # se obtiene el vehiculo
    vehiculo_db = Marca.objects.all() # se carga la base de datos para ver los vehiculos
    txt_action = 'este marca' # se define el texto de la accion
    if request.method == 'POST' and 'eliminar' in request.POST: # si el metodo es post y el formulario es
        vehiculo_d.delete() # se elimina el vehiculo
        messages.success(request,'Marca %s eliminada exitosamente' %vehiculo_d.nombre) # se muestra un mensaje de exito
        return redirect ('insumo') # se redirecciona a la url
    if request.method == 'POST' and 'cancelar' in request.POST: # si el metodo es post y el formulario es form2
        #no se realiza ninguna accion por que el cliente decidio no eliminar el vehiculo
        return redirect ('insumo') # se redirecciona a la url
    context = {
        'vehiculo_db': vehiculo_db,
        'txt_action': txt_action,  
    }
    return render (request, 'insumo/eliminar/eliminar.html',context)

def testing(request):

    return render(request, 'insumo/editar.html')