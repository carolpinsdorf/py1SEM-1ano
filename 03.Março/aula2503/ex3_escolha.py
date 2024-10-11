import os 
os.system("clear")

placa = int(input ("Digite os 4 últimos da placa: "))
ultimo_num = placa % 10
match ultimo_num:
    case 1 | 2:
        print("Segunda-feira")
    case 3 | 4:
        print("Terça-feira") 
    case 5 | 6:
        print("Quarta-feira")
    case 7 | 8:
        print("Quinta-feira") 
    case 9 | 0:
        print("Sexta-feira")
  


