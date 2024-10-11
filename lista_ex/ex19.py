import os 
os.system ("clear")

lado1 = float(input("Digite um numero: "))
lado2 = float(input("Digite um numero: "))
lado3 = float(input("Digite um numero: "))

if ((lado1+lado2)>lado3) and ((lado2+lado3)>lado1) and ((lado3+lado1)>lado2):
    print("Forma trinângulo")
else: 
    print("Não forma trinângulo")