from ..logic import historiaClinica_logic as hcl

def get_hc_Activas():
    hcs= hcl.get_historiasclinicas
    return hcs.__sizeof__