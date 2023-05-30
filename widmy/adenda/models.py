from django.db import models
from datetime import datetime
from widmy.historiaClinica.models import HistoriaClinica

# Create your models here.

class Adenda(models.Model):
    hClinica= models.IntegerField(null=False, default=None)
    fecha =  models.DateField(null=True,default =datetime.now, blank=True)
    diagnostico=models.CharField(null=True, blank=True,default=None, max_length=100)
    informacionAdicional = models.CharField(null=True, blank=True,default=None, max_length=100)
