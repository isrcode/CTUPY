num = int(input("Digite numero: "))
aux = num
invertido = 0

while aux != 0:
  resto = aux % 10
  aux = aux // 10
  invertido = invertido * 10 + resto

if num == invertido:
  print(f"O número {num} é um palindrome")
else:
  print(f"O número {num} não é um palindrome")

"""
7. A conversão de graus Fahrenheit para centígrados é obtida pela fórmula C = 9 5 (F − 32) .
Escreva um algoritmo que calcule e escreva uma tabela de graus centígrados em função de
graus Fahrenheit que variem de 50 a 150 Fahrenheit de 1 em 1.
"""