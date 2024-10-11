import os 
os.system ("clear")

#                                            Cadastro dos candidatos:
candidatos = ['', '', '']
print("Digite os nomes dos candidatos")
for i in range (3): # inicio = 10 e incremento de 1 é default
    candidatos[i] = input(f"{i+1}: ")

#                                                 CONTADOR:
cand1 = 0 
cand2 = 0
cand3 = 0
nulo = 0
# ou cand1 = cand2 = cand3 = nulo = 0

#                                                    Votacao:
while True:
    import os 
    os.system ("clear")

    print(f"""CANIDATOS:\n1 - {candidatos[0]}\n2 - {candidatos[1]}\n3-{candidatos[2]}""")
    
    voto = int (input("VOTO:"))

    match voto:
        case 0:
            break
        case 1:
            cand1 +=1
        case 2 :
            cand2 +=2
        case 3:
            cand3 +=1
        case _: # "_" = qualquer outra coisa  digitada
            nulo +=1

#                                           Apuração:
total_votos = cand1+cand2+cand3+nulo
perc1 = cand1/total_votos *100
perc2 = cand2/total_votos *100
perc3 = cand3/total_votos *100
perc_nulo = nulo/total_votos *100

print(f"""
CANDIDATOS
TOTAL DE VOTOS: {total_votos}
1 - {candidatos[0]:15} -> {cand1:3d} -> {perc1:5.1f}%
2 - {candidatos[1]:15} -> {cand2:3d} -> {perc2:5.1f}%
3 - {candidatos[2]:15} -> {cand3:3d} -> {perc3:5.1f}%
    {"NULOS":15} -> {nulo:3d} -> {perc_nulo}%
""")
