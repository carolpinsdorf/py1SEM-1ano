import os
os.system ("cls")

 # forca o while virar um repita, por que necessariamente vai entrar no while

"""
opcao = 's'            
while opcao == 's':
    print('Vou arrasar no CP2')
    opcao = input ("continuar, <s>im ou >n>ao?")
    ou
"""
while True:
    print("Vou arrasar no checkpoint")
    opcao = input("Continuar? <s>im ou <n>ao")
    if opcao =='n':
        break

