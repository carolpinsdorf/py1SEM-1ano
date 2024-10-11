import os 
os.system("cls")

#    0    1   2   3   4      
v = [45, -89, 32, -12, 33]
print("Forma bruta: ", v)

# Exibir 1o e último elemento 
print(f"Exibindo 1o e último elementos do vetor:\nV[0] = {v[0]}\nV[4] = {v[4]}\n")

# Exibir os elementos cujos indices sejam impares. Exibe índice e valor
print("Exibindo números com índices pares")
for i in range (0, 5, 1):
    resto = i % 2
    if resto ==0:
        print(f'V{i} = {v[i]}')

# Fazer uma função que retorne TRUE se o valor estiver no vetor, se não retorne FALSE:
num = int(input("\nDigite um número: "))
for i in range (0,5,1):
    if v[i] == num:
        retorno = "True"  
    else:
        retorno = "False"
if retorno == "False":
    print ("False")
else:
    print("True")





  