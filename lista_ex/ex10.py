import os 
os.system ("clear")

n1 = float(input("Digite um numero: "))
n2 = float(input("Digite um numero: "))
n3 = float(input("Digite um numero: "))

maior = n1
if n2>n1:
    maior = n2
    if n3>n2:
        maior=n3
print(f"O maior é", maior)