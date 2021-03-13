p = float(input("Qual o preço do produto? ").replace(',', '.'))
d = float(input("Qual o percentual de desconto a ser aplicado? ").replace(',', '.'))

pn = p - (p/100*d)

print(str(f"O produto custa R${p:.2f} com desconto de {d}% fica por R${pn:.2f}").replace('.', ','))

""" 
Se ao invés de um desconto fosse um aumento,
o que mudaria no codigo seria pn = p + (p/100*d)
e a mensagem no print descrevendo um almento e não
um desconto.
"""