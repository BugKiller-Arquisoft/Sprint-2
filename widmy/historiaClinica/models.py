from django.db import models

from paciente.models import Paciente


# Create your models here.

class HistoriaClinica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, default=None)
    prioridad = models.CharField(null=True, blank=True,default=None, max_length=100)
    activa= models.BooleanField(null=True)
    diagnosticoPrincipal=models.CharField(null=True, blank=True,default=None, max_length=100)
    otrosDiagnosticos=models.CharField(null=True, blank=True,default=None, max_length=100)
    operaciones=models.CharField(null=True, blank=True,default=None, max_length=100)
    informacionAdicional = models.CharField(null=True, blank=True,default=None, max_length=100)
    
    
