# 1. Dada uma nota, exibir se ela é válida ou inválida
import os
os.system ("clear")

nota = float(input("Nota: "))
if nota >= 0 and nota <=10:
    print("Nota válida")            #resolucao com op lógico
else:
    print("Nota inválida")

""""
Outra solução:
if nota <=0:
    if nota <=10:
        print("nota válida")
    else:
        print ("nota inválida")     resolucao c/ if encadeado
else:
    print ("nota inválida")
"""
