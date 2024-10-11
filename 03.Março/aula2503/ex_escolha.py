import os
os.system ("clear")

dia = int(input("Digite o número do dia da semana: "))
match dia:
    case 1:
        print("Segunda")
    case 2:
        print("Terça-feira")
    case 3:
        print("Quarta-feira")
    case 4:
        print("Quinta-feira")
    case 5: 
        print("Sexta-feira")
    case 6: 
        print("Sábado")
    case 7 :
        print("Domingo")
    case _:
        print(f"Valor {dia} inválido")