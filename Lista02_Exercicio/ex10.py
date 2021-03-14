distância = int(input("Digite a distância percorrida em metros: ").replace(',', '.'))
tempo = float(input("Digite o tempo em segundos: ").replace(',', '.'))

vmm_s = distância/tempo # velocidade média m/s

vmk_h = (distância/1000)/(tempo/3600) # velocidade média km/h

print(str(
    f"Se um corredor percorrer {distância}m em {tempo}s\n"
    f"A sua velocidade média em km/h é de {vmk_h:.2f}km/h\n"
    f"E sua velocidade média em m/s é de {vmm_s:.2f}m/s"
    ).replace('.', ','))