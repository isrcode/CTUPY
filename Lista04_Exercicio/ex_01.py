soma = 0
num = int(input("Digite um numero:"))

while num != 0:
    if num % 2 == 0: # teste logico para saber se o valor é par
        soma += num
    num = int(input("Digite um numero:"))
print(soma)


"""
1. Dada uma sequência de números inteiros onde o último elemento é o 0 , escreva um algoritmo
que calcula a soma dos números pares da sequência.
"""
