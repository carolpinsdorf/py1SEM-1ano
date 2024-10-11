import os
os.system("clear")

# Dado o valor da venda e se o usuário tem cupom de desconto, aplicar o desconto
# de R$20 caso a venda seja a partir de R$20. Exibir o valor da venda com desconto.

"""valor = float(input("Valor da venda: R$"))
cupom = str(input("Tem cupom? ")) 
if cupom == ("sim" or "Sim") and valor>20:
    valor_desconto  = valor - 20
    print(f"Valor com desconto: R$ {valor_desconto:.2f}")
else:
    print(f"Valor final: R${valor}")
"""

valor = float(input("Valor da venda: R$"))
if valor>20:
    cupom = str(input("Tem cupom? ")) 
    if cupom == "Sim" or "sim":
        valor_desc = valor-20
        print(f"Valor com descont: R${valor_desc:.2f}")
else:
    print(f"Valor final:{valor}")
       
