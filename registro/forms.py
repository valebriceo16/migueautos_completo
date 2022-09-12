from tkinter.ttk import Widget
from django import forms
from .models import Usuario, Vehículo

class usuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        
class vehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehículo
        fields = ['placa','modelo','color','estado','usuario']
        # widgets = {
            #  'fecha':forms.DateInput(
                #  attrs = {
                #  'readonly':True,
                    # 'hidden': True,
                    # 'placeholder': 'hola',
                    # 'required': False
                #   }
                #  )},
             
            
    

    