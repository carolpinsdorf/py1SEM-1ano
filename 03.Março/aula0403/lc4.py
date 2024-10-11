import os
os.system("clear")
"""" 6. Um caixa eletrônico dispensa cédulas de 50, 20, 10 reais, fazer um
algoritmo que exiba um relatório de quantas cédulas são necessárias para
compor a quantia.
"""
import os
os.system("clear")

num = int(input("Qual valor deseja retirar? (múltiplo de 10) "))
ced50 = num // 50
num2 = num % 50
ced20 = num2 // 20
num3 = num2 % 20
ced10 = num3 // 10
print(f"Você vai receber {ced50} cédulas de R$50, {ced20} cédulas de R$20 e {ced10} céculas de R$10.")


