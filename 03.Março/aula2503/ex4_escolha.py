import os 
os.system("clear")

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
operacao = str(input("Digite um sinal +, -, *, /, %, ou //: "))
match operacao:
    case "+":
        resultado = n1 + n2
        print(f"Resultado: {resultado}")
    case "-":
        resultado = n1 - n2
        print (f"Resultado: {resultado}")
    case "*":
        resultado = n1 * n2
        print(f"Resultado: {resultado}")
    case "/":
        resultado = n1 / n2
        print(f"Resultado: {resultado}")
    case "%": 
        resultado = n1 % n2
        print(f"Resultado: {resultado}")
    case "//":
        resultado = n1 // n2
        print (f"Resultado: {resultado}")