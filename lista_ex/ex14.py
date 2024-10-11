import os 
os.system ("clear")

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))
if num1 <= num2 <= num3:
    print("Os números em ordem crescente são:", num1, num2, num3)
elif num1 <= num3 <= num2:
    print("Os números em ordem crescente são:", num1, num3, num2)
elif num2 <= num1 <= num3:
    print("Os números em ordem crescente são:", num2, num1, num3)
elif num2 <= num3 <= num1:
    print("Os números em ordem crescente são:", num2, num3, num1)
elif num3 <= num1 <= num2:
    print("Os números em ordem crescente são:", num3, num1, num2)
else:
    print("Os números em ordem crescente são:", num3, num2, num1)

