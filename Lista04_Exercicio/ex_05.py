n = int(input("Digite um numero: "))
div = 1
contador = 0

while div <= n:
    if n % div == 0:
        print(f"Divisor -> {div} resultado -> {n/div:.0f}")
        contador += 1
    div += 1
print(
    f"O numero {n} tem {contador} divisores.\n"
    "Fim."
)

"""
5. Escreva um algoritmo que, dados um número inteiro positivo n , imprime na tela a contagem
de todos os divisores positivos de n .
"""
