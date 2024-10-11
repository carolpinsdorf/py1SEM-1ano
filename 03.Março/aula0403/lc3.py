"""" 5. Dado o preço do maço de cigarros, a quantidade consumida por dia,
e o tempo em anos que a pessoa fuma, calcular o quanto essa pessoa gastou
"""
import os
os.system("clear")

preco_maco = float(input("Quanto você paga em um maço? "))
qtd_dia = float(input("Quantos maços voce fuma por dia? "))
anos_fumante = float(input("Há quantos anos você fuma? "))
dias_fumante = 365 * anos_fumante
qtd_total = dias_fumante *qtd_dia
consumo = qtd_total * preco_maco
print(f"Você já gastou R${consumo:.2f} fumando")
