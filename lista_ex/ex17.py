import os 
os.system ("clear")

prova1 = float(input("Nota da prova 1: "))
prova2 = float(input("Nota da prova 2: "))
atvd1 = int(input("Nota da atividade 1: "))
atvd2 = int(input("Nota da atividade 2: "))
atvd3 = int(input("Nota da atividade 3: "))
atvd4 = int(input("Nota da atividade 4: "))
media_prova = ((prova1+prova2)/2)*0.6
atvds = atvd1 + atvd2 + atvd3 + atvd4
av1 = media_prova + atvds
if av1>6:
    print(f"A1 = {av1:.1f} Você está acima da média")
elif av1<6: 
    print(f"A1 = {av1:.1f} Você está abaixo da média")
else:
    print(f"A1 = {av1:.1f} Você está na média")


