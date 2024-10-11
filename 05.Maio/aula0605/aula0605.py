import os 
os.system ("clear")

# usando len com for = percorrer uma lista que nao se sabe o tamamnho 
lista = [22, 22, "Edson", 57.7, "lógica", "Fiap"]

for i in range (len(lista)):       #captura indice e elemento
    print(f"{lista[i]}")
# OU
for dado in lista:                 #captura somente o elemento
    print(f"{dado}")

# soma todos os elementos de um lista, porem da erro se nao tiver um dado nao numérico
lista  = [1, 2, 3, 4]
print(sum(lista))

# concatenar listas "+"
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(f"{lista3}")

# .extende(elemento) adiciona a ele mesmo um elemento, no final
lista2.extend(lista1)
print(lista2)

# .copy() copia um elemento no outro e os deixa independentes

# .sort() ordena em ordem crescente apenas vetores numericos, ou listas apenas numericas
# .sort(reverse=True) mesma coisa em ordem descrescnte
# != reverse que muda os elementos da lista
# clear limpa a lista, apenas os elementos
# del deleta a lista
