from webbrowser import get
import historiaClinica
import paciente
from ..models import HistoriaClinica
from ...paciente.logic import pacientes_logic as pl

def get_historiasclinicas():
    historiasclinicas = HistoriaClinica.objects.all()
    return historiasclinicas

def get_historiaclinica(hcl_pk):
    historiaclinica = HistoriaClinica.objects.get(pk=hcl_pk)
    return historiaclinica

def udpdate_historiaclinica(hcl_pk, new_hcl):
    historiaclinica = get_historiaclinica(hcl_pk)
    historiaclinica.id= new_hcl["id"]
    historiaclinica.paciente= pl.get_paciente(new_hcl["paciente"])
    historiaclinica.informacion= new_hcl["informacion"]
    historiaclinica.save()
    return historiaclinica

def create_historiaclinica(hcl):
    historiaclinica= HistoriaClinica(id=hcl["id"],paciente= pl.get_paciente(hcl["paciente"]),
                                     informacion=hcl["informacion"])
    historiaclinica.save()
    return historiaclinica

def delete_historiaclinica(hcl_pk):
    historiaclinica = get_historiaclinica(hcl_pk)
    historiaclinica.delete()
    return historiaclinica
