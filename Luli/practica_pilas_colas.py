from queue import LifoQueue as Pila
from queue import Queue as Cola

# PRACTICA 8 - PILAS

def copiar_pila(p: Pila) -> Pila:
    pAux: Pila = Pila()
    res: Pila = Pila()

    while not p.empty():
        elemento = p.get()
        pAux.put(elemento)
    
    while not pAux.empty():
        elem = pAux.get()
        p.put(elem)
        res.put(elem)

    return res