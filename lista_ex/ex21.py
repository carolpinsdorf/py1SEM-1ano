import os 
os.system ("clear")

ano = int(input("Digite o ano: "))
if  ((ano % 4) == 0) and ((ano % 100) != 0) and ((ano % 400) != 0):
    print("Ano bissexto")
else:
    print ("Ano não bissexto")