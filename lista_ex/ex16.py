import os 
os.system ("clear")

salario = float(input("Digite seu saláio: R$ "))
sexo = int (input("Qual seu sexo biológico?\n(1) Masculino | (2) Feminino\n"))
idade = int (input("Digite sua idade: "))
if sexo ==1 and idade < 20:
    convenio = salario * 0.0534
    print(f"Valor do convênio: R${convenio:.2f}")
elif sexo ==1 and (idade > 20 and idade <40):
    convenio = salario * 0.0844
    print (f"Valor do convênio: R${convenio:.2f}")
elif sexo ==1 and idade > 40:
    convenio = salario *0.1012
    print(f"Valor do convênio: R${convenio:.2f}")
elif sexo ==2 and idade < 20:
    convenio = salario * 0.0356
    print(f"Valor do convênio: R${convenio:.2f}")
elif sexo ==2 and (idade > 20 and idade <40):
    convenio = salario * 0.0643
    print (f"Valor do convênio: R${convenio:.2f}")
elif sexo ==2 and idade > 40:
    convenio = salario *0.082
    print(f"Valor do convênio: R${convenio:.2f}")
    