import os 
os.system("clear")

lista = list()
while True:
    elem = input("Digite algo: ")
    if elem != '.':
        lista.append(elem)
    else:
        break

print(lista)