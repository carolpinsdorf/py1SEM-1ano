# 1. Fazer um algoritmo que peça um numero ao usuário e calcule o seu quadrado. 
#	Entrada: 4		Saída: 16

# NARRATIVA
# - Pedir um numero ao usuário
# - Calcular o quadrado
# - Exibir o resultado

import os
os.system("clear")

# - Pedir um numero ao usuário
num = int(input("Digite um numero: "))
# - Calcular o quadrado
result = num ** 2
# - Exibir o resultado
print(f"O quadrado de {num} é {result}")
