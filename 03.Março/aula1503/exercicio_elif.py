import os
os.system("cls")

# Dado um número, apresente o mes correspondente. EX: Sefor digitado 5, aparecer "Maio"

n = int(input("Digite uma número: "))
if n==1:
    print("Janeiro")
elif n==2:
    print("Fevereiro")
elif n==3:
    print("Março")
elif n==4:
    print("Abril")
elif n==5:
    print("Maio")
elif n==6:
    print("Junho")
elif n==7:
    print("Julho")
elif n==8:
    print("Agosto")
elif n==9:
    print("Setembro")
elif n==10:
    print("Outubro")
elif n==11:
    print("Novembro")
elif n==12:
    print("Dezembro")
else:
    print("Mês inválido")