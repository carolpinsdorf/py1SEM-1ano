import os
os.system("clear")
# print("Nome:" + valor)
# print("Nome:", valor)
nome = "Edson"
idade = 49
salario = 848484.94
print("Senhor ", nome, ", você tem ", idade, "anos e ganha R$ ", salario)
# função format()                              0    1
print("Senhor {0}, você tem {1:.2f} anos e ganha R$ {2}".format(nome,idade, salario)) # usando indices
print("Senhor {}, você tem {} anos e ganha R$ {}".format(nome,idade, salario)) # usando a ordem respectiva
print("Senhor {n}, você tem {i} anos e ganha R$ {s}".format(n=nome,i=idade, s=salario)) # usando alias (pseudonimo)
print("Senhor {n}\nvocê tem {i} anos \ne ganha R$ {s}\n".format(n=nome,i=idade, s=salario)) # usando alias (pseudonimo)
# o \n muda a sequencia da frase de linha
# usando o f print
print(f"Senhor {nome}, você tem {idade} anos e ganha R$ {salario}")



os.system("clear")
valor1 = 34.7775
valor2 = 393.3
valor3 = 49499.64
print(f"Arroz \t\tR$ {valor1:010.2f}")
print(f"Memória \tR$ {valor2:10.2f}")
print(f"Uno \t\tR$ {valor3:10.2f}")

print(f"""
Arroz   R$ {valor1}
Memória R$ {valor2}
Uno     R$ {valor3}
      """)

valor4 = 4856
print(f"Valor 4: {valor4:010}")

