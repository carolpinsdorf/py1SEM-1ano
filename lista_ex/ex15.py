import os 
os.system ("clear")

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))

if num1 == num2 == num3:
    print("Os três números são iguais")
elif num1 == num2 != num3:
    print("Os 2 dos três números são iguais")
elif num1 != num2 == num3:
    print("Os 2 dos três números são iguais")
else:
    print("Os 3 números são diferentes")