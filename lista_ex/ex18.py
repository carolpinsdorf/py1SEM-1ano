import os 
os.system ("clear")

n1 = float(input("Digite um numero: "))
n2 = float(input("Digite um numero: "))
n3 = float(input("Digite um numero: "))
if n1 != n2 and n2 != n3  and n1 !=n3:
    if n1>n2 and n1<3:
        print(n1)
    elif n2>n1 and n2<n3:
        print(n2)
    else:
        print(n3)
else:
    print("Os números não são diferentes")