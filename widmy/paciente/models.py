from django.db import models

#from historiaClinica.models import historiaClinica

# Create your models here.

class Paciente(models.Model):
    #id = models.IntegerField()
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    eps = models.CharField(max_length=50)
    prioridad= models.CharField(max_length=50)
    #historiaclinica = models.OneToOneField(historiaClinica,default= None)
    
    
    