import os
os.system ("clear")

nota = float(input("Digite uma nota: "))
if nota >0 and nota < 10:
    print("Nota válida")
else:
    print("Nota inválida")
