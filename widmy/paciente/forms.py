from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'nombre',
            'fechaNacimiento',
            'rH',
            'tipoDocumento',
            'documentoDeIdentidad',
            'eps','ciudadResidencia'
            #'dateTime',
        ]

        labels = {
            'nombre' : 'Nombre',
            'fechaNacimiento' : 'FechaNacimiento',
            'rH':'Rh',
            'tipoDocumento':'TipoDocumento',
            'documentoDeIdentidad':'DocumentoDeIdentidad',
            'eps' : 'Eps',
            #'dateTime' : 'Date Time',
        }