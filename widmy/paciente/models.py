
from datetime import datetime
from django.db import models

#from historiaClinica.models import historiaClinica

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(null=True, blank=True,default=None, max_length=100)
    fechaNacimiento = models.DateField(null=True,default =datetime.now, blank=True)
    rH=models.CharField(null=True, blank=True,default=None, max_length=10)
    tipoDocumento = models.CharField(null=True, blank=True,default=None, max_length=10)
    documentoDeIdentidad = models.CharField(null=True, blank=True,default=None, max_length=50)
    eps =models.CharField(null=True, blank=True,default=None, max_length=50)
    ciudadResidencia=models.CharField(null=True, blank=True,default=None, max_length=100)   
    
    
    
    
    