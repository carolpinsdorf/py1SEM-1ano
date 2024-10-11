""""
Juntar os dois exercicio anteriores, ou seja, pedir a digitação do salário bruto, 
calcular o INSS e IR devido. Exibir o salário bruto, INSS, IR e salário líquido.

"""
import os 
os.system ("clear")

salario = float(input("Salário:R$ "))
print (f"Salário bruto: R${salario}")
if salario > 4159:
    inss4 = 468
    print (f"INSS: R${inss4:.2f}")
elif salario>1247.70 and salario<=2097.50:
    inss2 = salario * 0.09
    print (f"INSS: R${inss2:.2f}")
elif salario>=2097.50 and salario<=4159:
    inss3 = salario * 0.11
    print (f"INSS: R${inss3:.2f}")
else:
    inss1 = salario * 0.08
    print (f"INSS: R${inss1:.2f}")
if salario > 4271.59:
    deducao = 790.58
    ir5 = (salario * 0.275) - deducao
    print(f"IR: R${ir5:.2f}")
elif salario>3418.60 and salario<=4271.59:
    deducao = 577
    ir4 = (salario * 0.225) - deducao
    print(f"IR: R${ir4:.2f}")
elif salario<3418.59 and salario>2563.92:
    deducao = 320.60
    ir3 = (salario * 0.15) - deducao
    print(f"IR: R${ir3:.2f}")
elif salario< 2563.91 and salario>1710.79:
    deducao = 128.31
    ir2 = (salario * 0.075) - deducao
    print(f"IR: R${ir2:.2f}")
else:
    ir1 = 0
    print("IR: Isento")
if salario > 4271.59 and salario>4159:
    sal_liquido = salario - ir5 - inss4
    print(f"Salário líquido: R${sal_liquido:.2f}")
elif (salario>3418.60 and salario<=4271.59) and (salario>=2097.50 and salario<=4159):
    sal_liquido = salario - ir4 - inss3
    print(f"Salário líquido: R${sal_liquido:.2f}")
elif (salario<3418.59 and salario>2563.92) and (salario>1247.70 and salario<=2097.50):
    sal_liquido = salario - ir3 - inss2
    print(f"Salário líquido: R${sal_liquido:.2f}")
elif (salario< 2563.91 and salario>1710.79) and (salario<=1270):
    sal_liquido = salario - ir2 - inss1
    print(f"Salário líquido: R${sal_liquido:.2f}")
else:
    ir1 = 0
    inss1 = salario * 0.08
    sal_liquido = salario - ir1 - inss1
    print(f"Salário líquido: R${sal_liquido:.2f}")