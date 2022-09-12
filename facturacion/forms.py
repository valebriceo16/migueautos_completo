from django import forms

from facturacion.models import *

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Generar
        fields = ['usuario','vehiculo']