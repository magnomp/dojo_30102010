def processa_cedula(valor, cedula, cedulas):
    notas, valor = divmod(valor, int(cedula))
    if notas > 0:
        cedulas[cedula] = notas

    return valor

def conta_notas(valor):
    cedulas = {}
    if valor<0:
        raise ValueError()
    cedulas_todas = ('100','50','20','10','5','2','1')

    for cedula_corrente in cedulas_todas:
        valor = processa_cedula(valor, cedula_corrente, cedulas)
    
    return cedulas
