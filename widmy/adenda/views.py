import imp
from django.shortcuts import render
from .models import Paciente
from .logic import adenda_logic as al
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from .services import historiaClinica_services as serv
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
@csrf_exempt
def adendas_view(request):
    if request.method == 'GET':
        adendas_dto = al.get_adendas()
        adendas = serializers.serialize('json', adendas_dto)
        return HttpResponse(adendas, 'application/json')       
    if request.method == 'POST':
        adenda_dto = al.create_adenda(json.loads(request.body))
        adenda = serializers.serialize('json', [adenda_dto,])
        return HttpResponse(adenda, 'application/json')  
    
@csrf_exempt
def adenda_view(request, pk):
    if request.method == 'GET':  
        adenda_dto = al.get_adenda(pk)
        adenda = serializers.serialize('json', [adenda_dto,])
        return HttpResponse(adenda, 'application/json') 
    if request.method == 'DELETE':
        adenda_dto= al.delete_adenda(pk)
        adenda = serializers.serialize('json', [adenda_dto,])
        return HttpResponse(adenda, 'application/json')
