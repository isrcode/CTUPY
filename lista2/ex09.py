p = float(input("Qual o preço do produto? ").replace(',', '.'))
d = float(input("Qual o percentual de desconto a ser aplicado? ").replace(',', '.'))

pn = p - (p/100*d)

print(str(f"O produto custa R${p:.2f} com desconto de {d}% fica por R${pn:.2f}").replace('.', ','))
