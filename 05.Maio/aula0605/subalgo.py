import os
os.system("clear")

# subalgoritmos
def preenche_lista(l:list) -> None:
    while True:
        elem = input("Digite algo: ")
        if elem != '.':
            l.append(elem)
        else:
            break

def exibir_lista(l:list) -> None:
    for i in range(len(l)):
        print(f"{i} - {l[i]}, ", end="")

#funcoes: 
def procurar_valor(l:list) -> None:
    

# programa principal
lista = [23, "FIAP", 1.65, "Carolina"]
print(lista)
exibir_lista(lista)