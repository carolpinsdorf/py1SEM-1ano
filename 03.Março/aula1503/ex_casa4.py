# 4. Junte todos os exercicios. A cada nota digitada, se forem válidas, calcule a
# média e mostre o status.
import os
os.system ("clear")

nota1 = float(input("Nota 1: "))
if nota1 < 0 or nota1 > 10:
    print("Nota inválida")
else:
    print("Nota válida")
    nota2 = float(input("Nota 2: "))
    if nota2 < 0 or nota2 > 10:
        print("Nota inválida")
    else:
        print("Nota válida")
        nota3 = float(input("Nota 3: "))
        if nota3 < 0 or nota3 > 10:
            print("Nota inválida")
        else:
            print ("Nota válida")
            if nota1>nota3 and nota2>nota3:
                med = (nota1+ nota2)/2
                print (f"Média: {med}")
            elif nota1>nota2 and nota3>nota2:
                med = (nota1 + nota3)/2
                print (f"Média: {med}")
            else:
                med = (nota2 + nota3)/2
                print(f"Média:{med}")
            if med >= 6:
                print("Aprovado")
            elif med < 6 and med >= 4:
                print("Exame")
            else:
                print("Reprovado")

                