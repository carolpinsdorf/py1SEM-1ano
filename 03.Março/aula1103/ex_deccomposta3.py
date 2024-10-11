import os
os.system("clear")

#Dado pelo usuário o valor da compra, calcular 12% de desconto caso a venda seja maior
# que R$500 ou 6% se for até R$500.Se o usuário tem cupom de desconto, aplicar o 
# desconto de R$20 caso a venda seja a partir de R$20.
#Exibir o valor da venda com desconto.

valor = float(input("Valor da venda R$: "))
if valor>20:
    cupom = str(input("Tem cupom? ")) 
    if (valor>500) and cupom == "Sim" or "sim":
        valor_desc = valor - 20 -(12/100*valor)
        print(f"Valor com desconto: R$ {valor_desc:.2f}")
        if (valor<500) and cupom == "Sim"or "sim":
            valor_desc = valor - 20 -(6/100*valor)
            print(f"Valor com desconto: R$ {valor_desc:.2f}")
        else: 
            valor_final = valor   
            print(f"Valor da venda: R${valor_final:.2f} ")             
    else: 
        valor_final = valor   
    print(f"Valor da venda: R${valor_final:.2f} ")
else: 
    valor_final = valor   
    print(f"Valor da venda: R${valor_final:.2f} ")    

