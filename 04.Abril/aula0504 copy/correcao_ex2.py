import os
os.system ("cls")

# dado dois numero exibir os numero entre eles em ordem crescente
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

n1 += 1                          # nao vai printar o n1 do input
n2 += 2                          # nao vai printar o n2 do input
while n1 < n2:         
    print(n1)
    n1 = n1 +1
