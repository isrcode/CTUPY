sequencia = int(input("Quantos numero terá a sequência? "))
num = 0
contator = 0
positivos = 0
negativos = 0

while sequencia > contator:
    num = int(input("Digite um número: "))
    if num > 0:
        positivos += 1
    else:
        negativos += 1
    contator += 1

print(
    f"Na sequência de {sequencia} números foram digitados {positivos} números positivos e {negativos} numeros negativos."
)

