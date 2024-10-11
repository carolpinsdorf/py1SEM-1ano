import os 
os.system("clear")
# ============== CONCEITOS================
"""
procedimento: trecho de codigo que nao retorna valor || saudacao(x) ==> procedimento
funcao: trecho de codigo que retorna valor  || len(x) ==> funcao
metodo que nao retorna valor: dependente de um objeto || y = math.sqrt(x) ==> metodo que retorna valor
metodo que retorna valor: dependente de um objeto || design.background("green") ==> metodo que nao retorna valor
"""



#        0    1   2   3   4   5   6   7   8   Índice positivo (0 é sempre o primeiro)
lista = [10, 20, 30, 40, 50, 60, 70, 80, 90]
#        -9  -8  -7  -6  -5  -4  -3  -2  -1   Índice negativo (-1 é sempre o último)

print(lista[2])
print(lista[-7])
print(lista[2:5]) # exibe um período da lista 
print(lista[9:0:-1]) # o último é o "passo" ou intervalo, entao exibirá decrescente
print(lista[::-1])
print(lista[::2])

# ============== TUPLAS ===========  não é interável como as listas
tupla = tuple()
# ou
tupla = () # em vez de chavez é parentesis

#============== MÉTODOS ===========
frase = "Hoje é segunda e eu já estou cansada"
print(frase.find("segunda"))     # se achar retorna o índice, se não retorna -1

lista_nome = ["Carolina", "Dias", "Pinsdorf"]
new_lista_nome = " ".join(lista_nome)
print(lista_nome)
print(new_lista_nome)  #juntas cada elemento e coloca entre eles o que estiver dentro das " "

nome = "Gabriela Dias Pinsdorf"
new_nome = nome.split()
new2_nome = nome.split("a")
print(nome)
print(new_nome) # transforma uma string em lista, e usa o espaco como default pra quebra
print(new2_nome) # usa o "a" para a quebra

# Replce ver no ppt

#Strip ver no ppt

# in ver no ppt 