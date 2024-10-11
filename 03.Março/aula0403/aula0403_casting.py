import os
os.system("clear")   #para comcecar com a tela limpa
"""Entrada de dados: input()
Saida de dados: print (valor1, valor2)"""

#Casting - mudança de tipo de variável
"""int-inteira
float - real
string - texto
bool - logica"""
#input  sempre le dado texto, entao para processamento tem que fazer a "correcao"
conteudo = input("digite algo ")
conteudo = int (conteudo)       #casting
resp = conteudo + conteudo
print (" a resposta é: ", resp)
#   num1 = int(input("Digite algo: "))    - input com casting na mesma linha


