from django.shortcuts import render
from .models import Paciente
from .logic import pacientes_logic as pl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from .services import paciente_services as serv
from .forms import PacienteForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
"""
def pacientes_list(request):
    pasientes = pl.get_pacientes()
    context = {
        'paciente_list':pasientes
    }
    return render(request, 'pacientes.html', context)

def paciente_create(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            pl.create_paciente(form)
            messages.add_message(request, messages.SUCCESS, 'Paciente create successful')
            return HttpResponseRedirect(reverse('pacienteCreate'))
        else:
            print(form.errors)
    else:
        form = PacienteForm()

    context = {
        'form': form,
    }
    return render(request, 'pacienteCreate.html', context)
"""

@csrf_exempt
def pacientes_view(request):
    if request.method == 'GET':
        pacientes_dto = pl.get_pacientes()
        pacientes = serializers.serialize('json', pacientes_dto)
        return HttpResponse(pacientes, 'application/json')       
    if request.method == 'POST':
        paciente_dto = pl.create_paciente(json.loads(request.body))
        paciente = serializers.serialize('json', [paciente_dto,])
        return HttpResponse(paciente, 'application/json')  
    
@csrf_exempt
def paciente_view(request, pk):
    if request.method == 'GET':    
        paciente_dto = pl.get_paciente(pk)
        paciente = serializers.serialize('json', [paciente_dto,])
        return HttpResponse(paciente, 'application/json')
    if request.method == 'PUT':
        paciente_dto = pl.update_paciente(pk, json.loads(request.body))
        paciente = serializers.serialize('json', [paciente_dto,])
        return HttpResponse(paciente, 'application/json')
    if request.method == 'DELETE':
        paciente_dto= pl.delete_paciente(pk)
        paciente = serializers.serialize('json', [paciente_dto,])
        return HttpResponse(paciente, 'application/json')


    
    

    
