# Dada uma lista passada por parâmetro, verificar se nela consta somente valores inteiros.
# Se sim, retornar True, se não, retornar False.
import os
os.system("Clear")
# INÍCIO do subalgoritmo PRINCIPAL ---------
def eh_lista_int(l: list) -> bool:
 
    # INÍCIO subalgoritmo ENCADEADO -----------------
    def transforma_str(l: list) -> None: # [2, "FIAP", 9]
        for i in range(len(l)):
            l[i] = str(l[i]) # ["2", "FIAP", "9"]
    # FIM subalgoritmo ENCADEADO --------------------
 
    transforma_str(l)  # [2, "FIAP", 9]
                       # ["2", "FIAP", "9"]
    lista_int = True
    for i in range(len(l)):
        if not l[i].isnumeric(): # if not "FIAP".isnumeric()  => not False
            lista_int = False # False
            break
    return lista_int # False
# FIM do subalgoritmo PRINCIPAL ------------
 
 
 
# ---------- PROGRAMA PRINCIPAL
lista = [54, 3, 7, 1, 23]
if eh_lista_int(lista):
    print("Todos os valores são int")
else:
    print("Tem valor não int nesta lista")
 
 
lista = [54, "Edson", 7, 1, 23]
if eh_lista_int(lista):
    print("Todos os valores são int")
else:
    print("Tem valor não int nesta lista")