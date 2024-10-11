# 2. Dadas duas notas, calcular a média e exibir se está aprovado,
# reprovado, ou exame
import os 
os.system ("clear")

nota1 = float(input("Nota 1: "))
nota2 = float (input ("Nota 2: "))
med = (nota1 + nota2)/2
if med >= 6:
    print("Aprovado")
elif med < 6 and med >= 4: #med<6 fica redundante por conta do 1o if
    print("Exame")
else:
    print("Reprovado")