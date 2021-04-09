soma = 0
num = int(input("Digite um numero:"))

while num != 0:
    if num % 2 == 0: # teste logico para saber se o valor é par
        soma += num
    num = int(input("Digite um numero:"))
print(soma)


"""
Algoritimo que recebe uma sequência de números inteiros
e faz a soma dos números que são pares até que o usúario digite 0.
"""
