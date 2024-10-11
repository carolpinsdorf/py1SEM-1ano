# 3. Dadas 3 notas, calcular a média simples das duas maiores.
import os
os.system ("clear")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

""""
menor = nota1
if nota2 <menor:
    nota2 = menor
elif nota3 < menor:
    nota3 = menor
med = (nota1 + nota2 + nota3 - menor) /2
"""

if nota1>nota3 and nota2>nota3:
    med = (nota1 + nota2)/2
    print (f"Média: {med}")
elif nota1>nota2 and nota3>nota2:
    med = (nota1 + nota3)/2
    print (f"Média: {med}")
else:
    med = (nota2 + nota3)/2
    print(f"Média:{med}")


