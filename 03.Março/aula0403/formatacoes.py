import os
os.system("clear")

# '+'para concatenar textos apenas, com numero nao funciona; usar virgula
nome = "Carol"
idade = 25
salario =  0
print ("Senhorita", nome, "você tem", idade, "anos")

#funcao format()
print("Senhorita {0} você tem {1} anos".format(nome, idade))
print("Senhorita {} você tem {} anos".format(nome, idade))

print("Senhorita {0} você tem {1} anos e ganha R${2}".format(nome, idade, salario))   #indices
print("Senhorita {} você tem {} anos e ganha R${}".format(nome, idade, salario))       #ordem respct
print("Senhorita {n} você tem {i} anos e ganha R${s}".format(n=nome, i=idade, s=salario))     #álias
print("Senhorita {n}\nvocê tem {i}\nanos \ne ganha R${s}".format(n=nome, i=idade, s=salario))   # \n muda de linha  


#usando f print
print(f"Senhorita {nome} você tem {idade} anos e ganha R${salario}")

print("""
      Olha que legal
      da  pra colocar
      varias linhas de texto
      Pode ser usado para colcar textos!
      """)



os.system("clear")

valor1 = 424.524 
valor2 = 74839
valor3 = 848.857

print(f"Arroz \t\tR${valor1:.2f}")       #:.2f (2f)para quant (2) de casa decimal | f so para dados float
print(f"Memoria \tR${valor2:.2f}")
print(f"Uno \t\tR${valor3:.2f}")

print(f"Arroz \t\tR${valor1:10.2f}")     #:10.2f  para alinhar por espacos (10 espacos)
print(f"Memoria \tR${valor2:10.2f}")
print(f"Uno \t\tR${valor3:10.2f}")

print(f""" 
Arroz     R${valor1:.2f}
Memória   R${valor2} 
Uno       R${valor3:.3f}
""")








