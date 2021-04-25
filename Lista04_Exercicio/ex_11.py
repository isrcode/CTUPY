n = int(input("Digite um numero: "))
condicao = 1
primeiro_n = 0
segundo_n = 1
sequencia = 1

while condicao <= n:
    print(sequencia)
    sequencia = primeiro_n + segundo_n # sequencia = 1
    primeiro_n = segundo_n #primeiro_n = 1
    segundo_n = sequencia #segundo_n = 1
    condicao += 1
    


"""
Escreva um algoritmo que dado n , calcula o n -ésimo número da sequência de Fibonacci.
"""
