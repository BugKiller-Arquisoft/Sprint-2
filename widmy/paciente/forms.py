from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'nombre',
            'edad',
            'eps',
            'prioridad',
            #'dateTime',
        ]

        labels = {
            'nombre' : 'Nombre',
            'edad' : 'Edad',
            'eps' : 'Eps',
            'prioridad' : 'Prioridad',
            #'dateTime' : 'Date Time',
        }