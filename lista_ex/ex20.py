import os 
os.system ("clear")

lado1 = float(input("Digite um numero: "))
lado2 = float(input("Digite um numero: "))
lado3 = float(input("Digite um numero: "))

if ((lado1+lado2)>lado3) and ((lado2+lado3)>lado1) and ((lado3+lado1)>lado2):
    print("Forma trinângulo")
    if lado1 == lado2 == lado3:
        print("Triângulo equilátero")
    elif lado1==lado2 or lado2==lado3 or lado1==lado3:
        print("Triângulo Isóceles")
    else:
        print("Triângulo Escaleno")
else: 
    print("Não forma trinângulo")

