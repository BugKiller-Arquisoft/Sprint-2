from webbrowser import get
#import historiaClinica
from ..models import Paciente
#from ...historiaClinica.logic import historiaClinica_logic as hcl

def get_pacientes():
    pacientes = Paciente.objects.all()
    return pacientes

def get_paciente(pa_pk):
    paciente = Paciente.objects.get(pk=pa_pk)
    return paciente

def update_paciente(pa_pk, new_pa):
    paciente = get_paciente(pa_pk)
    paciente.id = new_pa["id"]
    paciente.nombre = new_pa["nombre"]
    paciente.edad= new_pa["edad"]
    paciente.eps = new_pa["eps"]
    paciente.prioridad = new_pa["prioridad"]
    #paciente.historiaclinica = hcl.get_historiaClinica(new_pa["historiaclinica"])
    paciente.save()
    return paciente

def create_paciente(pa):
    paciente = Paciente(id=pa["id"],nombre=pa["nombre"],edad=pa["edad"],eps=pa["eps"],prioridad=pa["prioridad"])#,
                        #historiaclinica=hcl.get_historiaclinica(pa["historiaclinica"]))
    paciente.save()
    return paciente

def delete_paciente(pa_pk):
    paciente= get_paciente(pa_pk)
    paciente.delete()
    return paciente
