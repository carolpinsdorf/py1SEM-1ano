import os 
os.system ("clear") 

#                                           PROGRAMA PRINCIPAL

# ========= importando jeito 3 - importa TUDO
from sub import *
saudacao1()
saudacao2("Carol")
saudacao3("Maria", 16)

print(raiz2(16))
print(raizn(16,2))

# ========= importando  jeito 2 - importa os subalgoritmos
from sub import saudacao1, saudacao2, saudacao3, raiz2, raizn
saudacao1()
saudacao2("Carol")
saudacao3("Maria", 16)

print(raiz2(16))
print(raizn(16,2))

# =========  importando jeito 1 - importa ao passo que usa o subalgoritmo
import sub
sub.saudacao1()
sub.saudacao2("Carol")
sub.saudacao3("Maria", 17)

print(sub.raiz2(16))
print(sub.raizn(16,2))