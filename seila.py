c = True

while c:
    resposta = input("sabe oq colocar aqui? True/False ")

    if resposta.lower() == "false":
        print("pensa melhor ent")

    elif resposta.lower() == "true":
        print("legal, eu n sei n")
        c = False