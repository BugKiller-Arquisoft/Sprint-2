from django.core import serializers
from . import models

class PacienteSerializer(serializers.Serializer):
    
    class Meta:
        fields = ('id', 'nombre', 'edad', 'eps', 'prioridad',)
        model = models.Measurement