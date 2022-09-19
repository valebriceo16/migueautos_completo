from django.forms import ModelForm
from miproyecto.models import Backup
 

class BackupForm(ModelForm):
    class Meta:
        model= Backup
        fields= ['nombre','archivo']
