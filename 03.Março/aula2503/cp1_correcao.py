import os 
os.system("clear")

salario = float(input("Salário: "))
salario_min = 1302
if salario<0:
    print("\nERRO! Digite um salário positivo!")
else:
    faltas = int(input("Qtd. de faltas: "))
    if salario < (2*salario_min):
        ajustado = (salario * 0.0645) + salario
        print(f"Salario: {salario:.2f}\nSalario Reajustado: {ajustado:.2f}")
    elif salario > (2*salario_min) and salario < (5*salario_min):
        ajustado = (salario * 0.0455) + salario
        print(f"Salario: {salario:.2f}\nSalario Reajustado: {ajustado:.2f}")
    else:    
        ajustado = (salario * 0.0289) + salario
        print(f"Salario: {salario:.2f}\nSalario Reajustado: {ajustado:.2f}")
    if faltas == 0:         #faltas <=0 (por conta do enunciado!!!!) 
        bonus = 1000
        print(f"Bônus: {bonus:.2f}")
    else: 
        print("Bônus: 0.00")

#DÚVIDA:
        # até x = inclui valor
        # a cima de x = nao inclui valor