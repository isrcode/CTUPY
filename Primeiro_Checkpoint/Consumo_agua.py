media_cosumo = float(input("Digite a media de consumo do ano anterior: ").replace(',','.'))
consumo_mes = float(input("Digite o cosumo do mes atual: ").replace(',','.'))

valor_consumo = consumo_mes * 2

if consumo_mes > 20 and consumo_mes <= 35:
    valor_consumo = consumo_mes * 3.5
elif consumo_mes > 35 and consumo_mes <= 50:
    valor_consumo = consumo_mes * 5.50
elif consumo_mes > 50:
    valor_consumo = consumo_mes * 7

if consumo_mes < media_cosumo:
    print(
        "O seu consumo este mês foi menor que a media de consumo do ano passado, será concedido um desconto de 20% na sua conta.\n"
        f"Consumo do mês => R${valor_consumo:.2f}\n"
        f"Desconto       => R${valor_consumo * 0.20:.2f}\n"
        f"Total da conta => R${valor_consumo - valor_consumo * 0.20:.2f}\n"
    )
elif consumo_mes > media_cosumo:
    dez = media_cosumo * 0.10 # 10% do consumo da média do ano anterior. 
    maior = consumo_mes - media_cosumo # valor que ecedeu ao consumo do ano anterior
    
    if maior > dez:
        print(
        "O seu consumo este mês ultrapassou a media de consumo do ano passado em mais de 10%, na sua conta terá um acrecimo de 30% de multa.\n"
        f"Consumo do mês => R${valor_consumo:.2f}\n"
        f"Multa          => R${valor_consumo * 0.30:.2f}\n"
        f"Total da conta => R${valor_consumo + valor_consumo * 0.30:.2f}\n"
    )

    else:
        print(
        "O seu consumo este mês está dentro dos limites com relação a média de consumo do ano passado.\n"
        f"Total da conta => R${valor_consumo:.2f}\n"
    )