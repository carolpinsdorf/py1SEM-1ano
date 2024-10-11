"""" Dada a idade de pessoas umas em dias, informar quantos dias, 
meses e anos elas tem """

import os
os.system("clear")

idade_dias = int(input("Quantos dias de vida você tem? "))
idade_anos = idade_dias // 365
rest_anos = idade_dias % 365
idade_meses = rest_anos // 30
idade_dias = rest_anos % 30
print(f"Você tem {idade_anos} anos, {idade_meses} meses e {idade_dias} dias.")
