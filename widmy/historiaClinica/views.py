import imp
from django.shortcuts import render
from .models import Paciente
from .logic import historiaClinica_logic as hcl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from .services import historiaClinica_services as serv
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from widmy.auth0backend import getRole

# Create your views here.
"""
def hclinica_list(request):
    historiaclinica = hcl.get_historiaclinica
    context = {
        'historiaclinica_list':historiaclinica
    }
    return render(request, 'historiaclinica.html',context)
"""


@csrf_exempt
@login_required
def historiasclinicas_view(request):
    role = getRole(request)
    if role == "Doctor":
        if request.method == 'GET':
            historiasclinicas_dto = hcl.get_historiasclinicas()
            historiasclinicas = serializers.serialize('json', historiasclinicas_dto)
            return HttpResponse(historiasclinicas, 'application/json')       
        if request.method == 'POST':
            historiaclinica_dto = hcl.create_historiaclinica(json.loads(request.body))
            historiaclinica = serializers.serialize('json', [historiaclinica_dto,])
            return HttpResponse(historiaclinica, 'application/json')
    else:
        return HttpResponse("Usted no salva vidas")
    
@csrf_exempt
def historiaclinica_view(request, pk):
    if request.method == 'GET':  
        historiaclinica_dto = hcl.get_historiaclinica(pk)
        historiaclinica = serializers.serialize('json', [historiaclinica_dto,])
        return HttpResponse(historiaclinica, 'application/json') 
    if request.method == 'PUT':
        historiaclinica_dto = hcl.udpdate_historiaclinica(pk, json.loads(request.body))
        historiaclinica = serializers.serialize('json', [historiaclinica_dto,])
        return HttpResponse(historiaclinica, 'application/json')
    if request.method == 'DELETE':
        historiaclinica_dto= hcl.delete_historiaclinica(pk)
        historiaclinica = serializers.serialize('json', [historiaclinica_dto,])
        return HttpResponse(historiaclinica, 'application/json')
    
@csrf_exempt
def activas(request):
    cantidad = hcl.get_activas()
    return HttpResponse(cantidad, 'application/json')

@csrf_exempt  
def alta_prioridad(request):
    cantidad = hcl.get_alta_prioridad()
    return HttpResponse(cantidad, 'application/json')
    
    
