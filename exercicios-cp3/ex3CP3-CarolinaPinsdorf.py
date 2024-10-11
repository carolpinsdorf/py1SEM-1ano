import os
os.system("clear")
 
# Descrição: retorna True caso a str seja um valor numerico(considerando decimal e negativo)
# Nome: eh_numero
# Tipo: Função

def is_number(s: str) -> bool:
    def is_int(s: str) ->  bool:
        digito = "0123456789"
        valido = True
        if s[0] == '-' or s[0] == '+' or s[0] in digito:  
            for i in range(1, len(s)):
                if s[i] not in digito:
                    valido = False
                    break
        else:
            valido = False 
        return valido
    
    def is_float(s:str) -> bool:
        digito = "0123456789."
        valido = True
        pontos = 0
        if s[0] == '-' or s[0] == '+' or s[0] in digito or s[0] == '.':  
            if s[0] == '.':
                pontos += 1
            for i in range(1, len(s)):
                if s[i] not in digito:
                    valido = False
                    break
                if s[i] == '.':
                    pontos += 1  
            if pontos > 1 or valido == False:
                valido = False
            else:
                valido = True
        else:
            valido = False
        return valido
        
    return is_int(s) or is_float(s)

# ----------------- PROGRAMA PRINCIPAL
resp = is_number("Edson")
print(resp)
resp = is_number("45.78") #T
print(resp)
resp = is_number("78") #T
print(resp)
resp = is_number("234.") # T
print(resp)
resp = is_number("234,67") # F
print(resp)
resp = is_number("12.567.32") # F
print(resp)
resp = is_number("-12.5") # T
print(resp)
resp = is_number(".1.23") # F
print(resp)
