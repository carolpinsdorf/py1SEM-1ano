import os 
os.system("clear")

av1 = float(input("Digita a nota 1: "))
av2 = float(input("Digita a nota 2: "))
av3 = float(input("Digita a nota 3: "))

menor = av1
if av2<av1:
    menor = av2
elif av3<menor:
    menor = av3
else:
    med = (av1+av2+av3-menor)/2
    if med>6:
        print(f"Média: {med} \nVocê está aprovado")
    else:
        print(f"Média: {med} \nVocê está reprovado")


