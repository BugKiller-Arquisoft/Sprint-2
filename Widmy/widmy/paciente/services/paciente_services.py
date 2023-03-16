from ..logic import pacientes_logic as pl

def get_alta_prioridad():
    contador = 0
    pacientes = pl.get_pacientes
    for paciente in pacientes:
        if paciente["prioridad"] == 'alta':
            contador+=1
    return contador
    