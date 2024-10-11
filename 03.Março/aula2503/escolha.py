import os
os.system ("clear")
print(f"""
    1 - Cadastrar
    2 - Consultar
    3 - Alterar
    4 - Excluir
""")
opcao = int(input("Escolha: "))

match opcao:
    case 1:
        print("Cadastrando...")
    case 2:
        print("Consultando...")
    case 3:
        print("Alterando...")
    case 4:
        print("Excluindo...")
