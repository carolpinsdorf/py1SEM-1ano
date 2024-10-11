import os
os.system ("clear")

# Numa loja, a compra a cima de R$100 terá desconto de 10%. Pedir o valor do pedido
# e exibir o valor final

valor = float(input("Digite o valor: R$"))
if valor>100:
    valor_desconto = valor - (10/100*valor)
print(f"Valor final: R${valor_desconto:.2f}")

      