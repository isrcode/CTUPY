salario = float(input("Digite o salario: ").replace(',','.'))

if salario < 1100:
    inss_075 = salario * 0.075
    inss = inss_075
elif salario > 1100 and salario < 2203.22:
    inss_075 = 1100 * 0.075 
    inss_09 = (salario - 1100) * 0.09
    inss = inss_09 + inss_075
elif salario > 2203.48 and salario < 3305.22:
    inss_075 = 1100 * 0.075
    inss_09 = (2203.48 - 1100) * 0.09
    inss_12 = (salario - 2203.48) * 0.12
    inss = inss_075 + inss_09 + inss_12
elif salario > 3305.22 and salario < 6433.57:
    inss_075 = 1100 * 0.075
    inss_09 = (2203.48 - 1100) * 0.09
    inss_12 = (3305.22 - 2203.48) * 0.12
    inss_14 = (salario - 3305.22) * 0.14
    inss = inss_075 + inss_09 + inss_12 + inss_14


print(
    f"Com base no salario de R${salario:.2f} a sua contribuição será de aproximadamente R${inss:.2f}".replace('.',',')
)
