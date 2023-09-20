senhasecreta=1987
senha=int(input("Digite sua senha: "))

tentativas=1
while senha!=senhasecreta:
    if tentativas<3:
        senha = int(input("Senha incorreta, digite novamente: "))
        tentativas+=1
    else:
        print("Limite de tentativas alcançado")
        break

else:
    print("Senha correta.")