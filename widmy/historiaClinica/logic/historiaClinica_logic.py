from webbrowser import get
import historiaClinica
import paciente
from ..models import HistoriaClinica
from paciente.models import Paciente
from paciente.logic import pacientes_logic as pl
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json

def get_historiasclinicas():
    historiasclinicas = HistoriaClinica.objects.all()
    return historiasclinicas

def get_historiaclinica(hcl_pk):
    historiaclinica = HistoriaClinica.objects.get(pk=hcl_pk)
    return historiaclinica

def create_historiaclinica(hcl):
    if check_paciente(hcl) == True:
        historiaclinica= HistoriaClinica(paciente= hcl["paciente"],prioridad= hcl["prioridad"],
                                         activa= hcl["activa"],diagnosticoPrincipal=hcl["diagnosticoPrincipal"],
                                         otrosDiagnosticos= hcl["otrosDiagnosticos"],operaciones= hcl["operaciones"],
                                         informacionAdicional= hcl["informacionAdicional"],)
        historiaclinica.save()
        return historiaclinica
    else:
        return HttpResponse("unsuccessfully created adenda. Historia Clinica does not exist")

def delete_historiaclinica(hcl_pk):
    historiaclinica = get_historiaclinica(hcl_pk)
    historiaclinica.delete()
    return historiaclinica

def get_activas():
    
    contador=0
    hclinicas = get_historiasclinicas()
    for hclinica in hclinicas:
        if hclinica.activa == True:
            contador+=1
    return contador

def get_alta_prioridad():
    contador = 0
    hclinicas = get_historiasclinicas()
    for historiaclinica in hclinicas:
        if historiaclinica.prioridad == 'Alta':
            contador+=1
    return contador
def check_paciente(data):
    r = requests.get(settings.PATH_PACIENTE, headers={"Accept":"application/json"})
    pacientes = r.json()
    for paciente in pacientes:
        if data["paciente"] == paciente["id"]:
            return True
    return False