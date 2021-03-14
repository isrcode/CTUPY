nmTime1 = input("Nome do primeiro time: ")
nmTime2 = input("Nome do segundo time: ")
golsT1 = int(input("Quantidade de gols: "))
golsT2 = int(input("Quantidade de gols: "))

if golsT1 > golsT2:
    print(f"O time {nmTime1} é o vencedor com {golsT1} gols marcados.")
elif golsT2 > golsT1:
    print(f"O time {nmTime2} é o vencedor com {golsT2} gols marcados.")
else:
    print("EMPATE")