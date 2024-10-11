import os
os.system ("clear")

# Dados 10 numeros, exibir qual o maior:

volta = 1
print("Digite 10 números:")
numero = int(input())
maior_numero = numero

while volta < 10:
    if maior_numero is None or numero > maior_numero:
        maior_numero = numero
        
    volta += 1
print(f'O maior número digitado é: {maior_numero}')