import os 
os.system("clear")

# ======================================== Funções =========================================

def verifica_lista_inteiro(l:list):
    for i in range(len(l)):
        l_str = str(l[i])
        if not l_str.isnumeric():
            return False
    return True

def verifica_negativo (l:list) -> bool:
    for i in range(len(l)):
        elem = l.split

# ====================================Programa Principal =======================================

lista = [5, 8, 4, "Edson", 12, 44]
if verifica_lista_inteiro(lista):
    print("Todos os elementos contidos na lista são inteiros")
else:
    print("Nem todos os elementos contidos no laço são inteiros")

lista = [5, 8, 4, 12, 44]
if verifica_lista_inteiro(lista):
    print("Todos os elementos contidos na lista são inteiros")
else:
    print("Nem todos os elementos contidos no laço são inteiros")

