consumo = float(input("Digite o cosumo mensal: ").replace(",","."))
kWh = 14
icms = 0

if consumo > 50:
    kWh = (consumo * 0.25) + 14

if consumo >= 100 and kWh <= 200:
    icms = kWh * 0.13

elif consumo >= 201:
    icms = kWh * 0.33

print(
    f"Consumo kWh    => R${kWh:.2f}\n"
    f"ICMS           => R${icms:.2f}\n"
    f"Total da conta => R${kWh + icms:.2f}\n".replace('.',',')

)
