import os
os.system("clear")

# faca um sub algoritmo de nome vogal_maiuscula(string) que passe uma string por parametro e a retorne
# com as vogais em maiusculo

#-------------------- subalgoritmo
def vogal_maiuscula(s: str) -> str:
    vogal = "aeiou"
    for i in range(len(s)):
        if s[i] in vogal:
            s = s.replace(s[i], s[i].upper())
    return s

def vogal_maiuscula2(s:str) -> str:
    vogal = "aeiou"
    for i, carac in enumerate(s):
        if carac in vogal:
            s = s.replace(carac, carac.upper())
    return s


#--------------------- programa principal
texto = "Edson de oliveira"
new_texto = vogal_maiuscula(texto)
print(new_texto)
