nmFunc = input("Qual o nome do funcionário: ").strip().title()
slAtual = float(input("Qual o valor do salário atual:R$ ").replace(',', '.'))
slAumento = float(input("Qual o valor do salário com aumento:R$ ").replace(',', '.'))

aumento = (slAumento - slAtual)/slAtual*100

print(f"O funcionário {nmFunc} recebeu {aumento:.2f}% de aumento.")
