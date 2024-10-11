""" Dada a tabela do INSS, fazer um algoritmo que leia o salário do contribuinte e
quanto ele irá pagar de INSS
        Tabela do INSS:
até R$1.247,70 ................8%
de R$1.247,71 a R$2.097,50.....9%
de R$2.97,51 a R$4.159.........11%
acima de R$4.159...............Teto = R$468
"""

import os 
os.system ("clear")

salario = float(input("Salário: "))
if salario > 4159:
    inss = 468
elif salario>1247.70 and salario<=2097.50:
    inss = salario * 0.09
elif salario>=2097.50 and salario<=4159:
    inss = salario * 0.11
else:
    inss = salario * 0.08

print(f"INSS: R${inss:.2f}")