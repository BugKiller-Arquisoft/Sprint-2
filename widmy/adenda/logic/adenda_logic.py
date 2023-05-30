from hmac import new
from webbrowser import get
import historiaClinica
import paciente
from ..models import Adenda
from paciente.models import Paciente
from historiaClinica.logic import historiaClinica_logic as hcl
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json

def get_adendas():
    adendas = Adenda.objects.all()
    return adendas

def get_adenda(ad_pk):
    adenda = Adenda.objects.get(pk=ad_pk)
    return adenda

def create_adenda(ad):
     if check_hclinica(ad) == True:
        adenda= Adenda(hClinica= ad["hClinica"],fecha=ad["fecha"],diagnostico=ad["diagnostico"],
                       informacionAdicional=ad["informacionAdicional"])
        adenda.save()
        return adenda
     else:
        return HttpResponse("unsuccessfully created adenda. Historia Clinica does not exist")

def delete_adenda(ad_pk):
    adenda = get_adenda(ad_pk)
    adenda.delete()
    return adenda
def check_hclinica(data):
    r = requests.get(settings.PATH_HCL, headers={"Accept":"application/json"})
    hclinicas = r.json()
    for hclinica in hclinicas:
        if data["hClinica"] == hclinica["id"]:
            return True
    return False


