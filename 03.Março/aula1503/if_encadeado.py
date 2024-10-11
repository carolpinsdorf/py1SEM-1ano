import os
os.system("cls")

n = int(input("Número:"))

if n > 0:
    print(f"Positivo")
else:                                       #juntar else com if = elif
    if n < 0:
        print("Negativo")
    else:
        print("Nulo")
