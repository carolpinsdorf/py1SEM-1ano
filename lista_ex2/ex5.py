

#5. EXERCÍCIO COMPLETO
#Uma turma tem 10 alunos. Um professor desenvolveu uma rotina para ter um melhor 
#gerenciamento o dos alunos. A média anual se dá por:
"""- Checkpoint:
    - São 3 avaliações
    - Calcula-se a média comum das duas maiores notas
    - Vale 20% da média final
- Challenge:
    - São 2 sprints
    - O cálculo é a média simples das duas notas
    - Vale 20% da média final
- Global solution:
    - Apenas uma nota que
    - Vale 60% da média final.
Requisitos:
- A média final para passar é ao menos 6, senão estará reprovado
- Toda vez que for digitada uma nota inválida (fora de 0 e 10), advertir
  e pedir novamente a digitação da mesma nota.
Relatório:
- para cada aluno exibir as médias calculadas e se ele está aprovado ou não.
- no final da digitação das notas dos dez alunos, exibir:
    - quantos foram aprovados
    - quantos foram reprovados
    - quantos tiraram a media final maxima (nota 10)"""

# CONTADOR:
aprovado = 0
reprovado = 0
media_maxima = 0

for i in range (1,3,1):
    # limpar a tela
    import os
    os.system("clear")

    print(f"Aluno {i}")

    #cálculo CP: (verificar se a nota é válida)
    print("---------------CHECKPOINTS---------------")
    cp1 = float (input("CheckPoint 1: "))
    while cp1 <0 or cp1>10:
        print("Digite uma nota válida")
        cp1 = float (input("CheckPoint 1: "))
    cp2 = float (input("CheckPoint 2: "))
    while cp2 <0 or cp2>10:
        print("Digite uma nota válida")
        cp2 = float (input("CheckPoint 2: "))
    cp3 = float (input("CheckPoint 3: "))
    while cp3 <0 or cp3>10:
        print("Digite uma nota válida")
        cp3 = float (input("CheckPoint 3: "))
    #verificar qual é a menor:
    menor = cp1
    if cp2 < menor:
            menor = cp2
    elif cp3<menor:
            menor = cp3
    # calcular a média:
    medCP = (cp1 + cp2 + cp3 - menor) / 2
    propCP = medCP * 0.2

    #cálculo CHALLENGE: (verificar se a nota válida = OUTRA FORMA)
    print("---------------CHALLENGE----------------")
    sp1 = float(input("Sprint 1: "))
    nota_invalida = sp1 <0 or sp1>10
    while nota_invalida:
        print("Digite uma nota válida")
        sp1 = float(input("Sprint 1: "))
        nota_invalida = sp1 <0 or sp1>10      #fazer o casting da variável
    sp2 = float(input("Sprint 2: "))
    nota_invalida = sp2 <0 or sp2>10
    while nota_invalida:
        print("Digite uma nota válida")
        sp2 = float(input("Sprint 2: "))
        nota_invalida = sp2 <0 or sp2>10
    medChallenge = (sp1 + sp2) / 2
    propChallenge = medChallenge * 0.2

    #GLOBAL SOLUTION: (verificar se ée válida)
    print("-------------GLOBAL SOLUTION-------------")
    gs = float(input("Global Solution: "))
    while not (gs >= 0 and gs <= 10):
        print("Digite uma nota válida")
        gs = float(input("Global Solution: "))
    propGs = gs * 0.6

    # exibir médias:
    print(f"""------------------Médias------------------
    CheckPoint: {medCP:.1f} 20% = {propCP:.2f}
    Challenge: {medChallenge:.1f} 20% {propChallenge:.2f}
    Global Solution: {gs:.1f} 40% = {propGs:.2f}""")

    # MÉDIA FINAL:
    medFinal = (propCP + propChallenge + propGs)
    print("----------------Média Final----------------")
    if medFinal >= 6:
        print(f"{medFinal:.1f} - Aprovado")
        aprovado += 1
        if medFinal == 10:
            media_maxima += 1
    else:
        print(f"{medFinal:.1f} - Reprovado")
        reprovado +=1

    
# RELATÓRIO:
print(f"""----------------Relatório----------------
Aprovados: {aprovado}
Reprovado: {reprovado}
Nota máxima: {media_maxima}""")