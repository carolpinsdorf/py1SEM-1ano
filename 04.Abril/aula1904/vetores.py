import os
os.system ("cls")
# são homogêneos, são predefinidos pelo programador
#    0    1   2   3   4      
v = [45, -89, 32, -12, 33]
print(f"Exibe a posição 2 do vetor: v[2] = {v[2]}")
print(f"Exibe o vetor inteiro: V = {v}")

#usando laço
# for i in range (0, 5,1):
    #print(f"{v[i]}")

# 1 - exibir primeiro elemento do vetor
print(f"exibir primeiro elemento do vetor: v[0] = {v[0]}")

# 2- exibir somente os números negativos
for i in range (0, 5, 1):
    if v[i]< 0:
        print(f"Os números negativos são: {v[i]}")

# 3 - exibir a somas dos elementos
soma = 0    # é uma variavel acumuladores, deve ser sempre inicializada                                                  
for i in range (0, 5, 1):
    soma += v[i]
print(f"A soma dos números : {soma}")

soma = 0
# 4 - exibir a média 
for i in range(0, 5, 1):
    soma += v[i]
med = soma / 5
print(f"A média dos elementos é: {med}")

# 5 - exibir os numeros ímpares
for i in range (0,5,1):
    resto = v[i] % 2
    if resto != 0:
        print(f"Os número ímpares: {v[i]}")

