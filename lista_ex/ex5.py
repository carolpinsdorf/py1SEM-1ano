import os
os.system("clear")

nota1 = float(input("Digite a 1a nota: "))
nota2 = float(input("Digite a 2a nota: "))
med = (nota1 + nota2) / 2
print(f"Média: {med}")
if med < 5:
    print("Você está reprovado")
else: 
    print("Você está aprovado")
