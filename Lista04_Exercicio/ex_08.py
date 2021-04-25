n = int(input("Digite um numero: "))
div = 1
cont = 0

while div < n:
    if n % div == 0:
        cont += 1
    div += 1

if cont < 2:
    print(f"{n} é um número primo!")
else:
    print(f"{n} não é um número primo!")

"""
8. Um número inteiro positivo n é denominado primo se existirem apenas dois divisores inteiros
positivos dele: o 1 e o próprio n . Escreva um algoritmo que recebe um inteiro n e verica
se n é primo ou não.
"""