import time as t
f = 50


while f <= 150:
    c = 9/5 * (f -32)
    print(f"{f}°F <-> {c:.2f}°C")
    f += 1
    t.sleep(0.1)

"""
7. A conversão de graus Fahrenheit para centígrados é obtida pela fórmula C = 9/5 (F − 32) .
Escreva um algoritmo que calcule e escreva uma tabela de graus centígrados em função de
graus Fahrenheit que variem de 50 a 150 Fahrenheit de 1 em 1.
"""