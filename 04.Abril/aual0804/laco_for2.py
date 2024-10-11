import os 
os.system("clear")

num = int(input("Digite um número: "))
for volta in range (num, num*11, num):
    print(f"{volta}", end = " ")

print()

for volta in range (1,11,1):
    tab = num * volta
    print(f"{tab}", end = " ")