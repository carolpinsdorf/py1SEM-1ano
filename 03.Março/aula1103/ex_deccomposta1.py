import os
os.system("clear")

# Dado pelo usuário o valor da compra, calcular 12% de desconto caso a venda seja maior
# que R$500 ou 6% se for até R$500. Exbir valor da venda com desconto

valor = float(input("Valor da compra: R$"))
if valor>500:
    valor_desconto = valor - (12/100*valor)
else:
    valor_desconto = valor -(6/100*valor)
print(f"Valor com desconto: R${valor_desconto:.2f}")
