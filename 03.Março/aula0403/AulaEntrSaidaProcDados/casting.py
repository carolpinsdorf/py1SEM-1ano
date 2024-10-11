import os
os.system("clear") # cls
"""

# Entrada de dados: input()
valor = input("Digite algo: ")
# Saída de dados
print(valor, type(valor))
"""

valor = 56
print(valor, type(valor))

valor = 85.9
print(valor, type(valor))

valor = "Edson"
print(valor, type(valor))

valor = True
print(valor, type(valor))

# Casting - mudança de tipo de variável
"""
int()   - inteira
float() - real
str()   - texto
bool()  - lógica
"""
os.system("clear")
conteudo = float(input("Digite algo: ")) # o input sempre lê dado texto (str)
#conteudo = int(conteudo) # casting

resposta = conteudo + conteudo

print("Resposta: ", resposta, type(resposta))

