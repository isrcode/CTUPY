dUteis = int(input("Dias uteis do mês: "))
htrabalhada = float(input("Horas trabalha: ").replace(',', '.'))
slHora = float(input("Salário/hora: ").replace(',', '.'))

hExtra = (htrabalhada - (dUteis*8)) * (slHora/2)
salário = (dUteis*8)*slHora

if htrabalhada < (dUteis*8):
    print("O funcionario não tem horas extras a receber este mês")
elif htrabalhada > (dUteis*8):
    print(str(
    f"Este mês o funcionario tem R${hExtra:.2f} em horas extras a receber.\n"
    f"Salário do mês é de -> R${salário:.2f}").replace('.', ','))
