""""
FEED BACK SPRINT 1:
apagar a tela quando abrir uma nova tela 
usar match case
evitar pedir que o usario escreva palavras ex('s'para sim)
nao ser redundate, e colocar o recurso de sair no final da acao
nao permitir deixar campos importantes em branco

"""
import os
os.system("clear")

# Cria uma lista vazia
lista = list()

# adiciona uma elemento NO FINAL da lista
lista.append (22)
lista.append('Logica')
print(lista)

# adiciona um dado numa posicao especifica da lista (posicao, elemento)
lista.insert(1,"Edson")
print(lista)

# remove o elemento na POSICAO informada, se nao colocar posicao remove o ultimo pop(posicao)
lista.pop(2)
print(lista)

# remove o elemento pelo CONTEUDO informada, remove(elemento)
lista.remove("Logica")
print(lista)

# retorna o indica do elemento .index(conteudo)
# retorna a qtd de elementos pelo conteudo .count(conteudo)
# retorna a qtd de elementos na lista, ou tamanho de um stringg len(lista ou string)