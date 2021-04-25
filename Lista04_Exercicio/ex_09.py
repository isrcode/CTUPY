import time as ti

d = float(input("Valor a ser aplicado: (R$) ").replace(',','.'))
t = float(input("Taxa de juros: (%) ").replace(',','.'))
j = int(input("Tempo que ficara aplicado: (Meses) "))
aux = d
contador = 1

while contador <= j:
    aux = aux + (aux * (t/100))
    contador += 1
    
print("Cauculando...")
ti.sleep(2)
print(
    f"R${d:.2f} aplicado com juros de {t}% ao mês, em {j} meses você tera um montante de R${aux:.2f}".replace('.',',')
)

"""
9. Dados um montante em dinheiro inicial d , uma taxa de juros mensal j e um período de
tempo em meses t , escreva um algoritmo que calcula o valor nal em dinheiro se d car
aplicado a taxa de juros j durante t meses.
"""