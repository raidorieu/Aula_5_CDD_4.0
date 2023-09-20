#divisão
primeirovalor=float(input("Digite o primeiro valor: "))
segundovalor=float(input("Digite o segundo valor: "))

tentativas=1
while segundovalor==0:
    if tentativas<5:
        segundovalor=int(input("Digite um número que não seja 0, por favor: "))
        tentativas+=1
    else:
        print("Limite de tentativas esgotado.")
        break

else:
    divisao=primeirovalor/segundovalor
    print(f"o resultado é: {divisao}")