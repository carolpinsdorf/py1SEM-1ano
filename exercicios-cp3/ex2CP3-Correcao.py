import os
os.system("clear")
 
def eh_inteiro(s: str) -> bool:
    digito = "0123456789"
    valido = True
    if s[0] == '-' or s[0] == '+' or s[0] in digito:
    #  False       or False       or False    
        for i in range(1, len(s)):
            if s[i] not in digito:
                valido = False
                break
    else:
        valido = False # False
    
    return valido
 
 
 
#                0123
print(eh_inteiro("B234"))
print(eh_inteiro("gg"))
print(eh_inteiro("-45"))
print(eh_inteiro("+44."))
print(eh_inteiro("+434"))