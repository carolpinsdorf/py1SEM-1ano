import os
os.system("clear")

# 2. Fazer um algoritmo que calcule o dobro de um número dado pelo usuário. 
# 	Entrada: 20		Saída: 40

# NARRATIVA:
# - Pedir um numero ao usuario
# - calcular o dobro
# - Exibir o resultado



# - Pedir um numero ao usuario
num = float(input("Digite um numero: "))
# - calcular o dobro
result = num + num # ou num * 2
# - Exibir o resultado
print(f"O dobro de {num:.3f} é {result:.3f}")

print("O dobro de {0:.3f} é {1:.3f}".format(num, result))
