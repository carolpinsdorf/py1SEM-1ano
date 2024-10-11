import os 
os.system ("clear")

#Dado um numero pelo usurio, exibir os seus 10 primeiros multiplos:
"""
inicial = int(input("Digite um número: "))
num = inicial
final = inicial * 10
while inicial <= final:
    print(f"{inicial}", end=" ")
    inicial = inicial + num
print("Fim do programa")
"""
volta = 1
num = int(input("Digite um número: "))

while volta <=10:
    mult = num * volta
    print(f"{num} x {volta} = {mult}")