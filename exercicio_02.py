#média
contador=1
soma=0
print("Vamos realizar uma média mas quantos valores você quer contar?")
quantidade=int(input("quantos valores? "))
while contador<=quantidade:
    numero=float(input("Digite um valor: "))
    soma=soma+numero
    contador+=1
media=soma/quantidade
print(f"A média dos números é: {media}")