n = int(input("Digite um numero: "))

condição = 1
contador = 0
compara = 0

while condição <= n:
    sequencia = int(input(f"Digite o {condição}º numero da sequencia: "))
    if sequencia != compara:
        contador += 1
    compara = sequencia
    condição += 1

print(f"{contador}")
