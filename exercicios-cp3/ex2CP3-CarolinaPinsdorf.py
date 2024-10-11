import os
os.system("clear")

# ------------------------------ Subalgoritmos

# Definicao: Aprimora a função isdigit/isnumeric e retorna T quando o numero 
# começa com + ou -
# Nome: eh_numero
# Tipo: função
def eh_numero(s: str) -> bool:
    numero = "0123456789"
    if s[0] == "-" or s[0] == "+":
        for i, elem in enumerate(s):
            if elem not in numero:
                return False     
        else:
            return True
    else:
        for i, elem in enumerate(s):
            if elem not in numero:
                return False
        else: 
            return True           
# ----------------------------- Programa principal
x = "B2A3"
print(eh_numero(x))
        