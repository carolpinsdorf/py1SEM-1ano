""" 4. Dada a quilometragem parcial de um carro e a quantidade de litros gastos para percorrer, fazer um algoritmo que calcule 
 o quanto esse carro consumiu"""

import os
os.system("clear")

km = float(input("Quantos kilomentros você percorreu? "))
litros = float (input("Quantos litros seu carro consumiu? "))
consumo = km/litros
print(f"O consumo do seu carro é {consumo:.2f}")
