import os
os.system ("clear")

joao = 0
clara = 0
guilherme = 0

while True:
    print((f"""
    Digite o número do seu candidato:
        1. Joao
        2. Clara
        3. Guilherme
    """))
    voto = (input("Digite aqui:"))
    while not voto.isnumeric():
        print

    match voto:
        case 1:
            joao+=1
        case 2:
            clara+=1
        case 3 :
            guilherme +=1
    print("Voto computado.")



