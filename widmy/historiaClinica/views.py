import imp
from django.shortcuts import render
from .models import Paciente
from .logic import historiaClinica_logic as hcl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from .services import historiaClinica_services as serv
# Create your views here.
@csrf_exempt
def historiasclinicas_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            historiaclinica_dto = hcl.get_historiaclinica(id)
            historiaclinica = serializers.serialize('json', [historiaclinica_dto,])
            return HttpResponse(historiaclinica, 'application/json')
        else:
            historiasclinicas_dto = hcl.get_historiasclinicas
            historiasclinicas = serializers.serialize('json', historiasclinicas_dto)
            return HttpResponse(historiasclinicas, 'application/json')       
    if request.method == 'POST':
        historiaclinica_dto = hcl.create_historiaclinica(json.loads(request.body))
        historiaclinica = serializers.serialize('json', [historiaclinica_dto,])
        return HttpResponse(historiaclinica, 'application/json')  
    
@csrf_exempt
def historiaclinica_view(request, pk):
    if request.method == 'PUT':
        historiaclinica_dto = hcl.udpdate_historiaclinica(pk, json.loads(request.body))
        historiaclinica = serializers.serialize('json', [historiaclinica_dto,])
        return HttpResponse(historiaclinica, 'application/json')
    if request.method == 'DELETE':
        historiaclinica_dto= hcl.delete_historiaclinica(pk)
        historiaclinica = serializers.serialize('json', [historiaclinica_dto,])
        return HttpResponse(historiaclinica, 'application/json')

def activas():
    cantidad = serv.get_hc_Activas
    return HttpResponse(cantidad, 'application/json')
    
    