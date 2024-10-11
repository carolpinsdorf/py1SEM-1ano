import os
os.system("clear")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
if n1 > n2:
    print(f"Maior número:{n1}")
    #print(f"O número {n1:.0f} é maior que {n2:.0f}")
else:
    print(f"Maior número:{n2}")
    #print(f"O número {n2:.0f} é maior que {n1:.0f}")
