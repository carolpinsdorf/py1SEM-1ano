""""
Dada a tabela de cálculo do IR, fazer um algoritmo que leia o salário e calcule o IR.
Tabela de IR
até 1710.78.................isento
de 1710.79 a 2563.91.........7.5%
de 2563.92 a 3418.59..........15%
de 3418.60 a 4271.59..........22.5%
a cima de 4271.59..............27.5%
"""

import os
os.system ("clear")

salario = float (input("Salário: R$ "))
if salario > 4271.59:
    deducao = 790.58
    ir = salario * 0.275 - deducao
    print(f"IR: R${ir:.2f}")
elif salario>3418.60 and salario<=4271.59:
    deducao = 577
    ir = (salario * 0.225) - deducao
    print(f"IR: R${ir:.2f}")
elif salario<3418.59 and salario>2563.92:
    deducao = 320.60
    ir = (salario * 0.15) - deducao
    print(f"IR: R${ir:.2f}")
elif salario< 2563.91 and salario>1710.79:
    deducao = 128.31
    ir = (salario * 0.075) - deducao
    print(f"IR: R${ir:.2f}")
else:
    print("IR: Isento")
