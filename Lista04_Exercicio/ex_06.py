nota = 0
condição = 1
maior_nota = 0
menor_nota = 70
candidatos_20 = 0
candidatos_21_50 = 0
candidatos_50 = 0

while condição <= 20:
    nota = int(input(f"Digite a {condição}º nota: "))
    if nota >= maior_nota:
        maior_nota = nota

    if nota <= menor_nota:
        menor_nota = nota
    
    if nota < 20:
        candidatos_20 += 1
    elif nota > 21 and nota < 50:
        candidatos_21_50 += 1
    else:
        candidatos_50 += 1


    condição += 1

print(
    f"A maior nota foi {maior_nota}\n"
    f"A menor nota foi {menor_nota}\n"
    f"{candidatos_20*100/20:.0f}% dos candidatos tiram notas menor que 20.\n"
    f"{candidatos_21_50*100/20:.0f}% dos candidatos tiram notas entre 21 e 50.\n"
    f"{candidatos_50*100/20:.0f}% dos candidatos tiram notas maior que 50.\n"
)