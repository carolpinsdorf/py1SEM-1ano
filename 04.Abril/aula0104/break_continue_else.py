import os
os.system("clear")

#continue break e else
resp = "s"
while resp == "s":
    resp = input("Continuar? <s>im ou <n>ão?")
    if resp == "n":
        break                     #força encerrar o programa

    if resp != 's' and resp != 'n':
        print("Amigão, digite s ou n!")
        resp = 's'
        continue                  #força continuar o programa

    if resp == "s":
        print("Bom dia")
else: # executa o else somente se o laço não for interrompido
    print("Terminou o programa!")