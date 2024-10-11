import os 
os.system ("clear")

# CONTADOR:
a0 = 0
delta0 = 0
delta_neg = 0
delta_positv = 0

# ler a, b, c
while True:
    print(f"""\nConsidere a equação ax**2 + bx + c = 0\nDigite os valores de a, b, c:\n""")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    
    """a = input("a = ")                               usando isnumeric, mas nao aceita negativo
    while not a.isnumeric():
        print("Digite apenas números!")
        a = input("a = ")
    b = input("b = ")
    while not b.isnumeric():
        print("Digite apenas números!")
        b = input("b = ")
    c = input("c = ")
    while not c.isnumeric():
        print("Digite apenas números!")
        c = input("c = ")
    a = float(a)
    b = float(b)
    c = float(c)"""

    # se a = 0 - eq de 1o grau:
    if a == 0:
        x = - c / b
        a0 += 1
        print(f"""\n======= RESULTADO ======\nA = 0, equação de 1o Grau:\nx = {x:.1f}\n""")
    else:                       # calcular delta - b**2 - 4ac
        delta = ((b) ** 2) - (4 * a * c)
        print(delta)
        while delta < 0:                                           #  enquanto delta <0
            delta_neg += 1
            print("Valores inválido, delta = 0, não há solução")
            print(f"""  Considere a equação ax**2 + bx + c = 0\nDigite os valores de a, b, c:""")
            a = float(input("A = "))
            b = float(input("B = "))    
            c = float(input("C = "))

        if delta == 0:                                             #  se delta == 0
            x = -b / (2*a)
            delta0 += 1
            print(f"""======= RESULTADO ======\nDelta = 0, portando\nx1 e x2 = {x}\n""")

        else:                                                        #  se delta > 0 
            x1 = (- (b) + delta ** (1/2)) / (2 * a)
            x2 = (- (b) - delta ** (1/2)) / (2 * a)
            delta_positv += 1
            print(f"""======= RESULTADO ======\nx1 = {x1:.1f}\nx2 = {x2:.1f}\n""")

    print(f"""Deseja continuar?\n1. Sim, Quero continuar\n2.Não, quero relatório\n""")
    opcao = int(input("Digite opção: "))
    if opcao == 2:
        print("Gerando relatório...\n")
        break
    else:
        import os 
        os.system ("clear")
# calculando as porcentagens
total_voltas = a0 + delta0 + delta_neg + delta_positv
porc_a0 = a0/total_voltas *100
porc_delta0 = delta0 / total_voltas * 100
porc_delta_neg = delta_neg / total_voltas * 100
porc_delta_positiv = delta_positv / total_voltas * 100
print(f"""========= Relatório =======
Quantidade total de voltas: {total_voltas}
'a' igual à zero:
Quantidade:...................{a0}
Porcentagem:..................{porc_a0:.0f}
\n
Delta igual à zero:
Quantidade:...................{delta0}
Porcentagem:..................{porc_delta0:.0f}
\n
Delta negativo:
Quantidade....................{delta_neg}
Porcentagem...................{porc_delta_neg:.0f}
\n
Delta positivo:
Quantidade....................{delta_positv}
Porcentagem...................{porc_delta_positiv:.0f}
""")  






