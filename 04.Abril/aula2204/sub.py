import os 
os.system("clear")

#                                   BIBLIOTECA FEITA EM AULA


# SUBALGORITMOS - FUNCOES E PROCEDIMENTOS ==> MÉTODOS

#===================== subalgoritmoss
# ------ PROCEDIMENTOS --------- nao retornam valor ao programa chamdor
def saudacao1() -> None:                #sem parâmetro
    print("Bom dia usuário")

def saudacao2(nome: str) ->  None:            #com parâmetro
    print(f"Bom dia {nome}")

def saudacao3(nome: str, hora: int) -> None:
    if hora < 12:
        msg = "Bom dia"
    elif hora < 18:
        msg = "Boa tarde" 
    else:
        msg = "Boa noite" 
    print(f"{msg} {nome}")

# --------- FUNCOES ----------- retornam valoer ao programa chamador
def raiz2(num:float) -> float:
    resp = num **(1/2)
    return resp

def raizn(num: float, raiz: int) -> float:
    resp = num **(1/raiz)
    return resp