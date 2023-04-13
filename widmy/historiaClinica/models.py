from django.db import models

from paciente.models import Paciente


# Create your models here.

class HistoriaClinica(models.Model):
    #id = models.IntegerField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, default=None)
    #paciente = models.OneToOneField(Paciente,on_delete=models.CASCADE,default= None)
    informacion = models.CharField(null=True, blank=True,default=None, max_length=100)
    
    
