import os 
os.system("clear")

nota1 = float(input("Digite sua nota: "))
if nota1<0 or nota1>10:
    print("Nota inválida")
else:
    print("Nota válida")
    nota2 = float(input("Digite sua nota: "))
    if nota2 >=0 and nota2 <= 10:
        print("Nota válida")
        med = (nota1 + nota2)/2
        if med>5:
            print(f"Média: {med} \nVocê está aprovado")
        elif med<5:
            print(f"Média: {med} \nVocê está reprovado")
    else:
        print("Nota inválida")
    

